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

> 如何提高效率，减少日常的工作量，可能需要开发方要考虑更多

### case 方面

- case 文件类型的选择，json、yml、excel 如何进行考量
- case 文件与接口的一致性如何进行保持？
- case 文件的自动生成方式

### 测试结果相关

> 如何保证结果的清晰性、可靠性

### yaml 文件的处理

- 场景 1:
  连续的测试 case，参数的传递问题。第一个 case 的返回值在后续的 case 使用到的情况下，可以提取当前 case（yaml 公共的参数，赋值的规则可以定义成各种来源，或自动生成或接口返回），参考 api_login_data_v1.yml data 部分

### 压力测试相关

> 如果仅仅是正常的接口测试，可能满足不了一些极端的 case，比如某个接口需要压测，我们的框架是否支持呢。
> https://github.com/httprunner/httprunner 这个项目“可能”就是我心中的自动测试框架了
> https://httprunner.com/blog/user-survey-report/ 里面的需求应该是自动化测试全部需求形态了
