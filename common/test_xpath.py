import json

from json_utils import jsonparse

a = '''{
    "ver": "6.8",
    "dcid": "477",
    "head": {
        "cid": "",
        "ctok": "",
        "cver": "1.0",
        "lang": "01",
        "sid": "1",
        "syscode": "09",
        "auth": "",
        "extension": []
    },
    "contentType": "json"
}'''
with open('test.json', encoding='utf-8') as j:
    demo_json = json.loads(j.read())
print(demo_json["data"]["token"])
print("\n")
print(a)
token = jsonparse(json.dumps(demo_json)).find_json_node_by_xpath('/data/token')
print(token)
