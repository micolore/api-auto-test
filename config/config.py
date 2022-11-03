import os

from common.read_data import data


def get_data_file_path():
    """
    获取测试数据文件的路径
    """
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
    return data_file_path


def get_api_root_url():
    """
    获取API_ROOT_URL
    """
    api_root_url = data.load_ini(get_data_file_path())["host"]["api_root_url"]
    return api_root_url
