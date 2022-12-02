from service.user_service import user_login


class CommonParams():
    """
    公用参数存储
    1、登陆获取token
    """

    def __init__(self):
        self.token = user_login()


common_params = CommonParams()
