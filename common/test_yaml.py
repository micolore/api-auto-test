import os

from common.yaml_utils import ObjectConverter
from data import BASE_PATH


def test_yaml_to_obj():
    data_file_path = os.path.join(BASE_PATH, "data", "api_login_data_v1.yml")
    y_to_obj = ObjectConverter().from_yaml(data_file_path)
    assert y_to_obj.cases[0].name == 'api_mid_login'
    print(y_to_obj.cases[0].headers.ContentType)
    print(y_to_obj.cases[0].req_data.client_id)
    print(y_to_obj.cases[0].req_data.client_secret)
    print(y_to_obj.cases[0].req_data.username)
    print(y_to_obj.cases[0].req_data.password)
    print(len(y_to_obj.cases))
    print(y_to_obj.cases[0].validate.msg.key)


test_yaml_to_obj()
