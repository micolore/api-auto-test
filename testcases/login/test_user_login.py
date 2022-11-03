import allure
from common.logger import logger
from config.config import get_data
from operation.user import login_user


class TestUserLogin():

    @allure.description("mid登录")
    @allure.title("mid登录")
    def test_login(self):
        base_data = get_data("api_login_data.yml")
        username = base_data["test_user_login"]["req_data"]["username"]
        password = base_data["test_user_login"]["req_data"]["password"]
        logger.info("test_login username:{},password:{}".format(
            username, password))
        result = login_user(username, password)
        assert result.status_code == 200
