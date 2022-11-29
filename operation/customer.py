from api.customer import customer
from config.config import get_data
from testcases.common.common_params import my_common_params


def add_customer():
    """
    新增用户
    :return: 自定义的关键字返回结果 result
    """
    base_data = get_data("api_customer_data.yml")
    data = base_data["test_api_add_customer"]["req_data"]
    headers = base_data["test_api_add_customer"]["headers"]
    headers["Authorization"] = "Bearer " + my_common_params.token
    result = customer.add_customer(data=data, headers=headers)
    return result
