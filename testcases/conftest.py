import pytest
from api.customer import customer
from api.user import user
from common.logger import logger
from config.config import get_data
from core.utils import json_add_kv, json_by_key


@pytest.fixture(scope="session")
def login_user():
    """
    登录,返回access_token
    :return: 自定义的关键字返回结果 result
    """
    base_data = get_data("api_login_data.yml")
    username = base_data["test_user_login"]["req_data"]["username"]
    password = base_data["test_user_login"]["req_data"]["password"]
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
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://se-login-web:8001",
        "Referer": "http://se-login-web:8001",
    }
    result = user.login(data=payload, headers=header)
    return result


@pytest.fixture(scope="session")
def add_customer(login_user):
    """
    新增用户
    :return: 自定义的关键字返回结果 result
    """
    r = login_user
    access_token = json_by_key(r.data, "access_token")
    base_data = get_data("api_customer_data.yml")
    payload = base_data["test_api_add_customer"]["req_data"]
    headers = base_data["test_api_add_customer"]["headers"]
    # header头加 token
    # Authorization: Bearer 95a67fc3-6a6a-4a2b-9b40-261a00c10a13
    headers["Authorization"] = "Bearer " + access_token
    result = customer.add_customer(data=payload, headers=headers)
    return result
