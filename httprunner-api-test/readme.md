# api test by httprunner

## 安装 httprunner

> bash -c "\$(curl -ksSL https://httprunner.com/script/install.sh)"
> 参考: https://httprunner.com/docs/quickstart/

## hello world

- 生成 demo 项目

  > hrp startproject demo
  > 参考: https://httprunner.com/docs/quickstart/

- 运行测试 case
  > hrp run demo/testcases/demo*requests.yml demo/testcases/demo_ref_testcase.yml --gen-html-report
  > 运行选择 xx_case*文件 后面是一些 httprunner 的命令

## 配置文件

- request.yml （testcase yaml 数据格式）
- requests.json（testcase json 数据格式）
- ref_testcase.yml (依赖某一个 test-case 文件)
- demo.json （仅仅是 demo）
- debugtalk.py （httprunner 插件，go 与 python 只会用到一个）
- proj.json（项目描述 json）
- .env（环境变量）

## 其他

> 一定要会用这个 httprunner，即使你用 python 做了很多的接口自动化的工作。但是最终你还是可能会用到这个工具，因为它的兼容性（支持更多协议、更多的测试场景）、扩展性都很不错。通过读它的文档，你还可以知道接口自动化还有哪些事情是要做的（有些重复性的工作真的不需要花大量的时间去做，我的意思是等你了解了常规的接口自动化测试之后。就要花精力去研究更多更专业的自动化测试业务的领域）
