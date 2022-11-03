import os
from common.read_data import data
from core.rest_client import RestClient

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url_mac"]


class Order(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Order, self).__init__(api_root_url, **kwargs)

    def pre_submit(self, **kwargs):
        return self.get("/order/operation/manual-order/v2/pre-submit", **kwargs)
        

    def batch_match_by_material_no(self, **kwargs):
        return self.post("/order/operation/manual-order/v2/pre-submit", **kwargs)

    def submit_manual_order(self, **kwargs):
        return self.post("/order/operation/manual-order/submit-manual-order", **kwargs)

    def get_company_info(self, **kwargs):
        return self.get("/order/operation/manual-order/get-company-info?companyId=131255", **kwargs)


order = Order(api_root_url)
