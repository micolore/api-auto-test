import json
import os

from common.json_utils import json_extract_value
from core.rest_client import RestClient
from data import BASE_PATH
from pojo.CasePojo import Cacses


def user_login():
    """
    用户登陆
    """
    data_file_path = os.path.join(BASE_PATH, "data", "api_login_data.yml")
    cl = Cacses.from_yaml(data_file_path)
    for case in cl.cases:
        case_url = case["url"]
        case_method = case["method"]
        case_headers = case["headers"]
        case_req_data = case["req_data"]
        case_extract_token = case["extract"]["token"]["key"]
        case_extract_token_flag = case["extract"]["token"]["flag"]
        rc = RestClient("")
        rs = rc.request(url=case_url,
                        method=case_method,
                        data=case_req_data,
                        headers=case_headers)
        jsd = json.loads(rs.data)
        token = json_extract_value(jsd, case_extract_token,
                                   case_extract_token_flag)
        return token
