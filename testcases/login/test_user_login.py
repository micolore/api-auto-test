import allure


class TestUserLogin():

    @allure.description("mid登录")
    @allure.title("mid登录")
    def test_login(self, login_user_pf):
        result = login_user_pf
        print(result.data)
        assert result.status_code == 200
