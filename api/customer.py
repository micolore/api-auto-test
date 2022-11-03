import os

from config.config import get_api_bus_root_url, get_api_root_url
from core.rest_client import RestClient


class Customer(RestClient):
    """
    客户
    """

    def __init__(self, api_root_url, **kwargs):
        super(Customer, self).__init__(api_root_url, **kwargs)

    def add_customer(self, **kwargs):
        return self.post("/api/se/system/user", **kwargs)


customer = Customer(get_api_bus_root_url())
