import pytest
import os
import allure
from api.user import user
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
scenario_data = get_data("scenario_test_data.yml")
login_data = get_data("login_data.yml")
order_data = get_data("order_data.yml")


@pytest.fixture(scope="session")
def login_op_fixture():
    """
    mac运营中心登录
    """
    loginName = base_data["mac_login_op"]["loginName"]
    password = base_data["mac_login_op"]["password"]
    returnUrl = base_data["mac_login_op"]["returnUrl"]
    operation = base_data["mac_login_op"]["operation"]
    validateCode = base_data["mac_login_op"]["validateCode"]
    deviceId = base_data["mac_login_op"]["deviceId"]
    payload = {
        "loginName": loginName,
        "password": password,
        "returnUrl": returnUrl,
        "operation": operation,
        "validateCode": validateCode,
        "deviceId": deviceId
    }
    header = {
        "Content-Type": "application/json"
    }
    login_op = user.login(data=payload, headers=header)
    # assert login_op.json()["code"] == 0
    yield login_op
    logger.info("===========登录后打印返回值===========")
    logger.info(login_op)
     logger.info(login_op.cookies)
    logger.info("===========登录后打印返回值===========")






