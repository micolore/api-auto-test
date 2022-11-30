import json

from jsonpath import jsonpath

with open('test.json', encoding='utf-8') as j:
    demo_json = json.loads(j.read())

# get data by jsonpath
name = jsonpath(demo_json, '$.name')
print(name)

token = jsonpath(demo_json, '$[data][token]')
print(token)
