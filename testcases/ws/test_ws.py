import json

import requests
from core.rest_client import RestClient
from requests.cookies import RequestsCookieJar


def test_login_and_list():
    wa = WebApi("https://demo.xxx.com")
    data = {
        "loginName": "上海哆啦A梦创新技术有限公司",
        "password": "d0919",
        "returnUrl": "/",
        "operation": False,
    }
    header = {"Content-Type": "application/json"}
    result = wa.login(data=data, headers=header)
    last_cookie = result.cookies

    # 在原来cookie的基础上新增一个cookie值
    new_cookies = RequestsCookieJar()
    new_cookies.set("hello", "dan", domain="demo.xxx.com")
    new_cookies.update(last_cookie)

    print(new_cookies)
    print("new 登录成功 cookies:" + str(new_cookies) + "\n\n\n")

    new_data = {
        "_": "1667374310699",
    }
    new_header = {
        "Content-Type": "application/json",
    }
    new_result = wa.recently_order(data=new_data,
                                   headers=new_header,
                                   cookies=new_cookies)
    print("new recently_order接口返回值:" + new_result.data + "\n\n\n")


class WebApi(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(WebApi, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/user/login", **kwargs)

    def recently_order(self, **kwargs):
        return self.get("/user/home/recently-order", **kwargs)
