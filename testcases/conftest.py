import pytest
from config.config import get_data
from core.utils import json_by_key
from operation.customer import add_customer as ops_add_customer
from operation.user import mid_login_user as ops_mid_login_user


@pytest.fixture(scope="session")
def login_user_pf():
    """
    登录,返回access_token
    :return: 自定义的关键字返回结果 result
    """
    base_data = get_data("api_login_data.yml")
    username = base_data["test_user_login"]["req_data"]["username"]
    password = base_data["test_user_login"]["req_data"]["password"]
    result = ops_mid_login_user(username=username, password=password)
    return result
