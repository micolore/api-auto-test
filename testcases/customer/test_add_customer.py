import allure

from common.yaml_utils import get_data
from pojo.CasePojo import Cacses


class TestCustomer():

    @allure.description("测试新增用户")
    @allure.title("测试新增用户")
    def test_add_customer(self):

        yaml_data = get_data("add_customer_case.yml")
        print(yaml_data)
        Cacses.from_yaml(
            "/Users/kubrick/Documents/kubrick/ower-code/python/api-auto-test/data/add_customer_case.yml"
        )
        """
        测试新增用户
        """
        # 加载case yaml 文件
        # 生成case
        # 执行case
        # 生成测试报告
        print("\n我在测试新增客户")
