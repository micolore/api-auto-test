# api auto test

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

## 关键字封装说明

关键字应该是具有一定业务意义的，在封装关键字的时候，可以通过调用多个接口来完成。在某些情况下，比如测试一个充值接口的时候，
在充值后可能需要调用查询接口得到最新账户余额，来判断查询结果与预期结果是否一致，那么可以这样来进行测试：

- 1, 首先，可以把 **`充值-查询`** 的操作封装为一个关键字，在这个关键字中依次调用充值和查询的接口，并可以自定义关键字的返回结果。
- 2, 接着，在编写测试用例的时候，直接调用关键字来进行测试，这时就可以拿到关键字返回的结果，那么断言的时候，就可以直接对关键字返回结果进行断言。

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
