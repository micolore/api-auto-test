import ast
import json as complexjson
from urllib.parse import urlencode

import requests
from common.logger import logger
from requests.cookies import RequestsCookieJar


class RespResult():
    """
        data: 响应体.
        cookies: cookie值(RequestsCookieJar类型),更加方便调用者操作cookie,其本身提供了一些方法。
        status_code http状态码
    """
    data = ""
    cookies = None
    status_code = 0

    def __init__(self, data, cookies, status_code):
        self.data = data
        self.cookies = cookies
        self.status_code = status_code

    def get_cookie_str(self):
        cookies_dict = requests.utils.dict_from_cookiejar(self.cookies)
        cookie_str = handler_cookie_str(cookies_dict)
        return cookie_str


def handler_cookie_str(cookie):
    pp = ''
    for (key, value) in cookie.items():
        pp = pp + (key + '=' + value + ";")
    return pp


class RestClient():

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        """
        1、cookie类型的传值、取值需要封装(cookie有几种类型,requests响应返回的是RequestsCookieJar类型,requests参数可以是rcj 或者dict类型,prepare_cookies源码有处理逻辑)
           主要是传递的时候可以由多种设置方式
           1、直接放header头里面 
           2、使用session进行设置 
           3、使用requests设置方式
           4、追加or全量,调用者处理还是默认处理,都要考虑,最好还是调用者处理
        2、**kwargs类似java的可变参数,但是比java的更强大,类似map的结构。
        """
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("data")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")
        self.request_log(url, method, data, json, params, headers, files,
                         cookies)

        if method == "GET":
            return self.http_get(url,
                                 headerdata=headers,
                                 interface_param=data,
                                 cookies=cookies)
        if method == "POST":
            return self.http_post(url,
                                  headerdata=headers,
                                  interface_param=data,
                                  cookies=cookies)
        if method == "PUT":
            if json:
                data = complexjson.dumps(json)
            return self.handle_resp(self.session.put(url, data, **kwargs))
        if method == "DELETE":
            return self.handle_resp(self.session.delete(url, **kwargs))
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.handle_resp(self.session.patch(url, data, **kwargs))

    def handle_resp(self, response):
        return RespResult(response.text, response.cookies,
                          response.status_code)

    def request_log(self,
                    url,
                    method,
                    data=None,
                    json=None,
                    params=None,
                    headers=None,
                    files=None,
                    cookies=None,
                    **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        logger.info("接口请求头 ==>> {}".format(
            complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数 ==>> {}".format(
            complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(
            complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数 ==>> {}".format(
            complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(cookies.__str__))

    def http_get(self, interface_url, headerdata, interface_param, cookies):
        """
        :param interface_url: 接口地址
        :param headerdata: 请求头文件
        :param interface_param: 接口请求参数
        :return: 字典形式结果
        """
        try:
            if interface_url != '':
                requrl = interface_url
                response = self.session.get(url=requrl,
                                            headers=headerdata,
                                            verify=False,
                                            timeout=40,
                                            params=interface_param,
                                            cookies=cookies)
                if response.status_code == 200:
                    result = response.text
                if response.status_code == 404:
                    result = complexjson.dumps(
                        {'接口返回状态': response.status_code}, ensure_ascii=False)
            elif interface_url == '':
                result = complexjson.dumps({"get params error!": ''},
                                           ensure_ascii=False)
            else:
                result = complexjson.dumps({"url error!": ''},
                                           ensure_ascii=False)
        except Exception as e:
            result = complexjson.dumps({"未知错误": e}, ensure_ascii=False)
        logger.info("result:" + result)
        return RespResult(response.text, response.cookies,
                          response.status_code)

    def http_post(self, interface_url, headerdata, interface_param, cookies):
        """
        :param interface_url: 接口地址
        :param headerdata: 请求头文件
        :param interface_param: 接口请求参数
        :return: 字典形式结果
        """
        print("headers", type(headerdata))
        print("interface_param", type(interface_param))
        try:
            if interface_url != '':
                if 'application/x-www-form-urlencoded' in headerdata.get(
                        "Content-Type"):
                    req_data = urlencode(interface_param)
                    response = requests.post(url=interface_url,
                                             headers=headerdata,
                                             cookies=cookies,
                                             data=req_data,
                                             verify=False,
                                             timeout=40)
                if 'application/json' in headerdata.get("Content-Type"):
                    response = requests.post(url=interface_url,
                                             headers=headerdata,
                                             cookies=cookies,
                                             json=interface_param,
                                             verify=False,
                                             timeout=40)
                if 'multipart/form-data' in headerdata.get("Content-Type"):
                    response = requests.post(url=interface_url,
                                             headers=headerdata,
                                             cookies=cookies,
                                             files=interface_param,
                                             verify=False,
                                             timeout=40)

                if response.status_code == 200:
                    result = response.text
                if response.status_code == 404:
                    result = complexjson.dumps(
                        {'接口返回状态:%s': response.status_code},
                        ensure_ascii=False)
            elif interface_url == '':
                result = complexjson.dumps({"params error": ''},
                                           ensure_ascii=False)
            else:
                result = complexjson.dumps({"url error": ''},
                                           ensure_ascii=False)
        except Exception as e:
            result = complexjson.dumps({"unknow error!": e},
                                       ensure_ascii=False)
        logger.info("result:" + result)
        return RespResult(response.text, response.cookies,
                          response.status_code)
