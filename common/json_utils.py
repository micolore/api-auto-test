import json

import xmltodict
from jsonpath import jsonpath


def json_to_dict(data):
    """
    json to dict
    """
    return json.loads(data)


def dict_to_json(data):
    """
    dict to json
    """
    return json.dumps(data)


def json_add_kv(data, key, value):
    """
    json string add k,v
    """
    d = json.loads(data)
    d[key] = value
    return json.dumps(d)


def json_by_key(data_str, key):
    """
    json get value by key
    """
    return json.loads(data_str)[key]


def json_extract_value(obj, partten, flag):
    """
    flag true=single or false=list
    """
    if flag:
        r = jsonpath(obj, partten)
        if r == False:
            return r
        else:
            return r[0]
    else:
        return jsonpath(obj, partten)


# 解析json字符串
class jsonparse(object):

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
