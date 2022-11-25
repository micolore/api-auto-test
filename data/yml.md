# yml

## 测试用户登陆

> 统一处理,静态提取返回值、静态断言返回值、请求参数的动态赋值（需要连续的业务测试 case）

- yml 结构
  - api_config_key api 接口的唯一标识
  - url 接口地址
  - headers header 头
  - req_data 请求参数
  - extract 需要提取的返回值信息
  - validate 断言的内容

```txt
test_login:
  api_config_key: test_login
  headers:
    {
      'Content-Type': 'application/json',
      'Origin': 'http://se-login-web:8001',
      'Referer': 'http://se-login-web:8001',
    }
  req_data:
    {
      'nickname': 'moppo1103',
      'userType': 2,
      'phone': '18217331512',
      'email': '471304402@qq.com',
      'username': 'moppo221103',
      'pass': 'XWgAjO20tBAcPn6hT9J9jA==',
      'salerId': 621501,
      'salesName': '621501',
      'territory': 1,
      'address': 'shanghai',
      'industryType': 2,
      'companyScope': 1,
      'tag': 'normal',
      'status': 1,
      'creditedAccount': 'SHANGHAI',
      'description': 'hello',
      'prefix': 86,
      'customerSuccessIdList': [],
    }
  extract:
    token: $.token
  validate:
    - eq: [$.msg, login success!]
    - eq: [$.code, 0]
```
