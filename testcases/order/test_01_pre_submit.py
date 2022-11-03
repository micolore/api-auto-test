import pytest
import allure
import jsonpath
from operation.order import pre_submit
from operation.user import login_user_op
from testcases.conftest import login_data
from common.logger import logger
import requests


@allure.step("步骤1 ==>> 运营中心登录")
def step_1(loginName, cookies):
    logger.info("步骤1 ==>> 运营中心登录:{}".format(loginName,cookies))


@allure.epic("新建订单")
@allure.feature("场景：运营中心登录-打开新建订单页面-查询添加产品-提交订单")
class TestOrder():
    @allure.story("登录后，打开新建订单页面")
    @allure.description("新建订单页面获取uuid")
    @allure.title("新建订单页面获取uuid")
    def test_pre_submit(self, login_op_fixture):
        logger.info("*************** 开始执行用例 ***************")
        cookies = login_op_fixture.cookies
        logger.info(cookies)
        result = pre_submit(cookies1)
        print(result)
        assert result.status_code == 200
        assert result.code == 0
        uuid = jsonpath.jsonpath(result.data, '$.data.uuid')
        print(uuid)
