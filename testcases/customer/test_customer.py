import allure

from operation.customer import add_customer


class TestCustomer():

    @allure.description("新增用户")
    @allure.title("新增用户")
    def test_add_customer(self):
        result = add_customer()
        assert result.http_status_code == 200
