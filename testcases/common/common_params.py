from config.config import get_data
from core.utils import json_by_key
from operation.user import mid_login_user as ops_mid_login_user


class CommonParams():
    """
    公用参数存储
    1、登陆获取token
    """

    def __init__(self):
        base_data = get_data("api_login_data.yml")
        username = base_data["test_user_login"]["req_data"]["username"]
        password = base_data["test_user_login"]["req_data"]["password"]
        result = ops_mid_login_user(username=username, password=password)
        token = json_by_key(result.data, "access_token")
        self.token = token


my_common_params = CommonParams()