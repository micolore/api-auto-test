from api.user import user


def login_user(username, password):
    """
    登录A
    :return: 自定义的关键字返回结果 result
    """
    payload = {
        "username": username,
        "password": password,
        "client_secret": "123456",
        "grant_type": "password",
        "captchaVerification": "",
        "client_id": "center"
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://se-login-web:8001",
        "Referer": "http://se-login-web:8001",
    }
    result = user.login(data=payload, headers=header)
    return result
