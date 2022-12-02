import dataclasses

import yaml2pyclass


class Cacses(yaml2pyclass.CodeGenerator):

    @dataclasses.dataclass
    class CaseConfigClass:
        name: str
        api_config_key: str
        url: str
        method: str
        headers: str
        req_data: str
        extract: str
        validate: list

    cases: CaseConfigClass
