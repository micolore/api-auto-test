import os

from config.config import get_api_root_url
from core.rest_client import RestClient


class User(RestClient):
    """
    用户
    """

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/oauth/token", **kwargs)


user = User(get_api_root_url())
