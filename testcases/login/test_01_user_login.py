import allure
import pytest
from operation.user import login_user, login_user_op
from testcases.conftest import login_data


@pytest.mark.user
class TestUserLogin():

    @allure.description("mid登录")
    @allure.title("mid登录")
    @pytest.mark.smoke
    @pytest.mark.parametrize('loginName, password', login_data["test_login"])
    def test_login(self, login_name, password):
        result = login_user(loginName, password)
        assert result.status_code == 200
        assert result.code == 0
