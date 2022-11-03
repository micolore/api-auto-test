import allure
from operation.customer import add_customer


class TestCustomer():

    @allure.description("新增用户")
    @allure.title("新增用户")
    def test_add_customer(self, login_user_pf):
        result = add_customer(login_user_pf)
        assert result.status_code == 200
