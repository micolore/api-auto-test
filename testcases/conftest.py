import pytest
from api.user import user
from common.logger import logger
from config.config import get_data

base_data = get_data("api_login_data.yml")


@pytest.fixture(scope="session")
def login_op_fixture():
    """
    后台登录
    """
    username = base_data["test_user_login"]["req_data"]["username"]
    password = base_data["test_user_login"]["req_data"]["password"]
    payload = {
        "username": username,
        "password": password,
    }
    header = {"Content-Type": "application/json"}
    login_op = user.login(data=payload, headers=header)
    yield login_op
    logger.info(login_op)
    logger.info(login_op.cookies)
