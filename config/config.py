import os

import pytest
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data_file_path():
    """
    获取测试数据文件的路径
    """
    data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
    return data_file_path


def get_api_bus_root_url():
    """
    获取API_BUS_ROOT_URL
    """
    api_root_url = data.load_ini(
        get_data_file_path())["host"]["api_bus_root_url"]
    return api_root_url


def get_api_root_url():
    """
    获取API_ROOT_URL
    """
    api_root_url = data.load_ini(get_data_file_path())["host"]["api_root_url"]
    return api_root_url


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data
