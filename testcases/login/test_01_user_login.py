from operation.user import login_user
from operation.user import login_user_op
import allure
import pytest
from testcases.conftest import login_data


@pytest.mark.user
class TestUserLogin():
    @allure.description("商城客户登录")
    @allure.title("商城客户登录")
    @pytest.mark.smoke
    @pytest.mark.parametrize('loginName, password, returnUrl, operation', login_data["test_login"])
    def test_login(self, loginName, password, returnUrl, operation):
        result = login_user(loginName, password, returnUrl, operation)
        assert result.status_code == 200
        assert result.code == 0

    @allure.description("运营中心登录")
    @allure.title("运营中心登录")
    @pytest.mark.smoke
    @pytest.mark.parametrize('loginName, password, returnUrl, operation, validateCode, deviceId',
                             login_data["test_login_op"])
    def test_login_op(self, loginName, password, returnUrl, operation, validateCode, deviceId):
        result = login_user_op(loginName, password, returnUrl, operation, validateCode, deviceId)
        assert result.status_code == 200
        assert result.code == 0