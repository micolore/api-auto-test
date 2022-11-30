import json

import xmltodict


# 解析json字符串
class jsonprase(object):

    def __init__(self, json_value):
        try:
            eval(json_value)
            self.json_value = json.loads(json_value)
        except AttributeError:
            raise ValueError('must be a json str value')

    def find_json_node_by_xpath(self, xpath):
        elem = self.json_value
        nodes = xpath.strip("/").split("/")
        for x in range(len(nodes)):
            try:
                elem = elem.get(nodes[x])
            except AttributeError:
                elem = [y.get(nodes[x]) for y in elem]
        return elem

    def datalength(self, xpath="/"):
        return len(self.find_json_node_by_xpath(xpath))

    @property
    def json_to_xml(self):
        try:
            root = {"root": self.json_value}
            xml = xmltodict.unparse(root, pretty=True)
        except AttributeError:
            print("json_to_xml error")
        return xml


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
token = jsonprase(json.dumps(demo_json)).find_json_node_by_xpath('/data/token')
print(token)
