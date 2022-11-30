import os

from file_load import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

data_file_path = os.path.join(BASE_PATH, "common", "test.yaml")
yaml_data = data.load_yaml(data_file_path)
