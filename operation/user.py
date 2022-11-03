from api.user import user
from core.result_base import ResultBase


def login_user(login_name, password):
    """
    登录A
    :return: 自定义的关键字返回结果 result
    """
    payload = {
        "loginName": login_name,
        "password": password,
    }
    header = {"Content-Type": "application/json"}
    result = user.login(json=payload, headers=header)
    return ResultBase(result)
