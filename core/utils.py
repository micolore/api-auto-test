import json


def json_to_dict(data):
    return json.loads(data)


def dict_to_json(data):
    return json.dumps(data)


def json_add_kv(data, key, value):
    """
    json字符串增加k,v
    """
    d = json.loads(data)
    d[key] = value
    return json.dumps(d)


def json_by_key(data_str, key):
    return json.loads(data_str)[key]
