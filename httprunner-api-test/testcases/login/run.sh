# 编译自定义插件，输出到项目的根目录下面
hrp build testcases/login/plugin/debugtalk.go -o .
# 测试登陆
hrp run testcases/login/requests.yml