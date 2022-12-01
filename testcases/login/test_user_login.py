import json

import allure
from jsonpath import jsonpath
from logger import logger

from common.json_utils import json_extract_value
from core.rest_client import RestClient
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
        cl = Cacses.from_yaml("../../data/api_login_data.yml")
        print(cl.cases[0])
        for case in cl.cases:
            print("\n-------")
            case_name = case["name"]
            case_config_key = case["api_config_key"]
            case_url = case["url"]
            case_method = case["method"]
            case_headers = case["headers"]
            case_req_data = case["req_data"]
            case_extract_token = case["extract"]["token"]["key"]
            case_extract_token_flag = case["extract"]["token"]["flag"]

            logger.info(
                "case_info case_name:{},case_config_key:{},case_url:{},case_headers:{},case_req_data:{},case_req_token:{},"
                .format(case_name, case_config_key, case_url, case_headers,
                        case_req_data, case_extract_token))

        rc = RestClient("")
        rs = rc.request(url=case_url,
                        method=case_method,
                        data=case_req_data,
                        headers=case_headers)
        print("响应值:----\n")
        print(rs.data)
        print(case_extract_token)
        jsd = json.loads(rs.data)
        print(jsonpath(jsd, case_extract_token))
        print(
            json_extract_value(jsd, case_extract_token,
                               case_extract_token_flag))
        print(json_extract_value(jsd, case_extract_token, False))
        print("\n我在测试新增客户")
