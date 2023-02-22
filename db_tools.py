"""
small package of useful db functions
"""
import yaml
from hashlib import sha256

CONFIG_FILENAME = "config.yaml"


def get_database_filename() -> str:
    # open config file and get dict of values
    config_file = open(CONFIG_FILENAME)
    config_dict = yaml.safe_load(config_file)[0]
    config_file.close()

    # get database filename from the config
    database_filename = config_dict['database_filename']
    return database_filename


def hash_string(string: str) -> str:
    string = string.encode('utf-8')
    string = sha256(string).hexdigest()
    return string
