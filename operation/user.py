from api.user import user
from core.result_base import ResultBase


def login_user(loginName, password, returnUrl, operation):
    """
    登录商城
    :return: 自定义的关键字返回结果 result
    """

    payload = {
        "loginName": loginName,
        "password": password,
        "returnUrl": returnUrl,
        "operation": operation
    }
    header = {"Content-Type": "application/json"}
    result = user.login(json=payload, headers=header)
    return ResultBase(result)


def login_user_op(loginName, password, returnUrl, operation, validateCode,
                  deviceId):
    """
    登录运营中心
    :return: 自定义的关键字返回结果 result
    """
    payload = {
        "loginName": loginName,
        "password": password,
        "returnUrl": returnUrl,
        "operation": operation,
        "validateCode": validateCode,
        "deviceId": deviceId
    }
    header = {"Content-Type": "application/json"}
    result = user.login(json=payload, headers=header)
    return ResultBase(result)
