from api.customer import customer
from config.config import get_data
from core.utils import json_by_key


def add_customer(login_user):
    """
    新增用户
    :return: 自定义的关键字返回结果 result
    """
    r = login_user
    access_token = json_by_key(r.data, "access_token")
    base_data = get_data("api_customer_data.yml")
    data = base_data["test_api_add_customer"]["req_data"]
    headers = base_data["test_api_add_customer"]["headers"]
    headers["Authorization"] = "Bearer " + access_token
    result = customer.add_customer(data=data, headers=headers)
    return result
