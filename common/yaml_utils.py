import inspect
import os
import re
from dataclasses import dataclass
from inspect import getmembers
from pathlib import Path
from string import Template
from typing import Any, Dict, List

import pytest
import yaml

from common.file_load import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    """
     from yaml get data
    """
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


def _map_kv_to_yaml():
    '''
    映射key到yaml(test)
    '''
    data_file_path = os.path.join(BASE_PATH, "data", "common.yml")
    with open(data_file_path, encoding='utf-8') as fp:
        read_yml_str = fp.read()
        temp_template = Template(read_yml_str)
        c = temp_template.safe_substitute({
            "token": "20221125",
            "user_id": "1001"
        })
        print("c: " + c)
        yaml_data = yaml.safe_load(c)
        print(yaml_data["common"]["token"])


@dataclass
class CodeGenerator:

    @classmethod
    def from_yaml(cls, config_file: str):
        """
        yaml to class
        """
        if not os.path.exists(config_file):
            raise FileNotFoundError(
                f"Could not find YAML file at {config_file}")
        with open(config_file, "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            data = {} if data is None else data

        cls._update_code(data)

        old_fields = list([
            value for key, value in getmembers(cls)
            if key == '__dataclass_fields__'
        ][0].keys())
        dummy_data = {field: None for field in old_fields}

        c = cls(**dummy_data)
        cls._update_data(c, data)

        return c

    @classmethod
    def _update_data(cls, obj: object, data: Dict[str, Any]):

        obj.__dict__.clear()
        obj.__dict__.update(data)

        for key, value in data.items():
            if not isinstance(value, dict):
                continue

            subclass = type(cls._to_class_name(key), (), {})
            obj.__dict__[key] = cls._update_data(subclass(), value)

        return obj

    @classmethod
    def _update_code(cls, data: Dict[str, Any]):
        code_file = Path(inspect.getfile(cls))
        lines = code_file.read_text().split("\n")

        start_pos_list = [
            idx for idx, line in enumerate(lines) if
            ("class" in line and cls.__name__ in line and "Class" not in line)
        ]
        if len(start_pos_list) != 1:
            raise ValueError("Malformed config file! Cannot modify file!")

        # find indentation
        pos = start_pos_list[0] + 1

        if lines[pos] == "":
            return
        match = re.match(pattern=r"^(?P<indentation>\s+)", string=lines[pos])
        if match is None:
            raise ValueError("Malformed config file! Cannot modify file!")
        indentation = match.groupdict()["indentation"]

        # clear old keys
        while pos < len(lines):
            lines.pop(pos)

        # add new keys
        lines[pos:pos] = [
            indentation + line for line in cls._create_code(data, indentation)
        ] + [""]

        # add import
        cls._add_import(lines)

        code_file.write_text('\n'.join(lines))

    @classmethod
    def _add_import(cls, lines: List[str]):
        pattern = r"^\s*import\s*dataclasses\s*$"
        if any(re.match(pattern=pattern, string=line) for line in lines):
            return

        lines.insert(0, "import dataclasses")

    @classmethod
    def _create_code(cls, data: Dict[str, Any], indentation: str) -> List[str]:
        if len(data.keys()) == 0:
            return [f"pass"]

        dict_keys = [
            key for key, value in data.items() if isinstance(value, dict)
        ]

        lines = []
        for key in dict_keys:
            lines.append(f"@dataclasses.dataclass")
            lines.append(f"class {cls._to_class_name(key)}:")
            lines.extend([
                indentation + line
                for line in cls._create_code(data[key], indentation)
            ])
            lines.append(f"")

        for key, value in data.items():
            if key in dict_keys:
                lines.append(f"{str(key)}: {cls._to_class_name(key)}")
            else:
                lines.append(f"{str(key)}: {type(value).__name__}")

        return lines

    @staticmethod
    def _to_class_name(key: str):
        return ''.join(x.title() for x in key.split('_')) + "Class"
