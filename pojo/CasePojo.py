import dataclasses

import yaml2pyclass


class Cacses(yaml2pyclass.CodeGenerator):

    @dataclasses.dataclass
    class CaseConfigClass:
        name: str
        api_config_key: str
        url: str

    cases: list
