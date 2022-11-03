from api.user import user
from common.logger import logger
from config.config import get_data


def mid_login_user(username, password):
    """
    登录,返回access_token
    :return: 自定义的关键字返回结果 result
    """
    base_data = get_data("api_login_data.yml")
    logger.info("test_login username:{},password:{}".format(
        username, password))

    payload = {
        "username": username,
        "password": password,
        "client_secret": "123456",
        "grant_type": "password",
        "captchaVerification": "",
        "client_id": "center"
    }
    headers = base_data["test_user_login"]["headers"]
    result = user.login(data=payload, headers=headers)
    return result
