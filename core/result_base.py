from common.logger import logger


class ResultBase():
    def __init__(self, result):
        self.response = result
        self.status_code = result.status_code
        self.code = result.json()["code"]
        self.message = result.json()["message"]
        self.data = result.json()["data"]
        self.cookies = result.cookies
        if self.code == 0:
            logger.info("登录成功 ==>> {}".format(self.message))
        else:
            logger.info("登录失败 ==>> {}".format(self.message))
