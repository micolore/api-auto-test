import requests
from common.logger import logger


class ResultBase():

    def __init__(self, result):
        self.response = result
        self.status_code = result.status_code
        self.code = result.json()["code"]
        self.message = result.json()["message"]
        self.data = result.json()["data"]
        self.cookies = result.cookies
        if self.code == 0:
            logger.info("请求成功 ==>> {}".format(self.message))
        else:
            logger.info("请求失败 ==>> {}".format(self.message))


class RespResult():
    """
        http_cookies: cookie值(RequestsCookieJar类型),更加方便调用者操作cookie,其本身提供了一些方法。
        http_status_code http状态码
        http_resp http状态码
        data: 响应体.
        message: 消息.
        code: code.
    """
    http_resp = None
    htt_cookies = None
    http_status_code = 0
    data = None

    def __init__(self, result):
        self.http_resp = result
        self.htt_cookies = result.cookies
        self.http_status_code = result.status_code
        self.data = result.text

    def get_cookie_str(self):
        cookies_dict = requests.utils.dict_from_cookiejar(self.htt_cookies)
        cookie_str = handler_cookie_str(cookies_dict)
        return cookie_str


def handler_cookie_str(cookie):
    pp = ''
    for (key, value) in cookie.items():
        pp = pp + (key + '=' + value + ";")
    return pp
