import allure
from logger import logger

from pojo.CasePojo import Cacses


class TestAddCustomer():

    @allure.description("测试新增用户")
    @allure.title("测试新增用户")
    def test_add_customer(self):

        cl = Cacses.from_yaml("../../data/add_customer_case.yml")
        print(cl.cases[0])
        for case in cl.cases:
            print("\n-------")
            case_name = case["name"]
            case_config_key = case["api_config_key"]
            case_url = case["url"]
            case_headers = case["headers"]
            case_req_data = case["req_data"]
            case_req_token = case["extract"]["user_id"]
            logger.info(
                "case_info case_name:{},case_config_key:{},case_url:{},case_headers:{},case_req_data:{},case_req_token:{},"
                .format(case_name, case_config_key, case_url, case_headers,
                        case_req_data, case_req_token))
        """
        测试新增用户
        """
        # 加载case yaml 文件
        # 生成case
        # 执行case
        # 生成测试报告
        print("\n我在测试新增客户")
