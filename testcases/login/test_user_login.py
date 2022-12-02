import json
import os

import allure
from jsonpath import jsonpath
from logger import logger

from common.json_utils import json_extract_value
from core.rest_client import RestClient
from data import BASE_PATH
from pojo.CasePojo import Cacses


class TestUserLogin():

    @allure.description("mid登录")
    @allure.title("mid登录")
    def test_login(self):
        """
        测试新增用户
        # 加载case yaml 文件
        # 生成case
        # 执行case
        # 生成测试报告
        """
        data_file_path = os.path.join(BASE_PATH, "data", "api_login_data.yml")
        cl = Cacses.from_yaml(data_file_path)
        for case in cl.cases:
            print("\n-------")
            case_url = case["url"]
            case_method = case["method"]
            case_headers = case["headers"]
            case_req_data = case["req_data"]
            case_extract_token = case["extract"]["token"]["key"]
            case_extract_token_flag = case["extract"]["token"]["flag"]

        rc = RestClient("")
        rs = rc.request(url=case_url,
                        method=case_method,
                        data=case_req_data,
                        headers=case_headers)
        jsd = json.loads(rs.data)
        print(
            json_extract_value(jsd, case_extract_token,
                               case_extract_token_flag))
        print("\n我在测试新增客户")
