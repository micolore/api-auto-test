# Api Auto Test

**Python、Requests、Pytest、YAML、Allure** ，通过 Python+Requests 来发送和处理 HTTP 协议的请求接口，使用 Pytest 作为测试执行器，使用 YAML 来管理测试数据，使用 Allure 来生成测试报告。

## 项目结构

- api ====>> 接口封装层，如封装 HTTP 接口为 Python 接口
- common ====>> 各种工具类
- core ====>> requests 请求方法封装、关键字返回结果类
- config ====>> 配置文件
- data ====>> 测试数据文件管理
- operation ====>> 关键字封装层，如把多个 Python 接口封装为关键字
- pytest.ini ====>> pytest 配置文件
- requirements.txt ====>> 相关依赖包文件
- testcases ====>> 测试用例

## 使用的第三方包

> https://github.com/vinta/awesome-python

- 数据模拟-faker https://github.com/joke2k/faker
- 时间处理-arrow https://github.com/arrow-py/arrow
- orm https://github.com/encode/orm
- pytest https://docs.pytest.org/en/latest/
- 断言库 sure
- 行为测试 pytest-bdd
- yaml2class
- jsonpath
- xmltodict support by attribute get value

## 未来方向

- 1、跨语言执行 case（golang）
- 2、web 端自动化测试
- 3、服务端接口修改自动同步

## 关于接口自动化的思考
