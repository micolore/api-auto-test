import allure


class TestCustomer():

    @allure.description("新增用户")
    @allure.title("新增用户")
    def test_add_customer(self, add_customer):
        result = add_customer
        assert result.status_code == 200
