import os

from common.file_load import data

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
