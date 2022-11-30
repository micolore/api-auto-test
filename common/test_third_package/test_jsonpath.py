import json

from jsonpath import jsonpath

with open('test.json', encoding='utf-8') as j:
    demo_json = json.loads(j.read())

# 配合JSONPath表达式提取数据
name = jsonpath(demo_json, '$.name')
print(name)

token = jsonpath(demo_json, '$[data][token]')
print(token)

