#!/usr/bin/env python
"""
Checks if the given credentials exist in the database
"""
import yaml
from hashlib import sha256
import sqlite3

CONFIG_FILENAME = "config.yaml"


def main():
    username = input("Username: ")
    password = input("Password: ")
    if is_valid_credentials(username, password):
        print("Valid Credentials")
    else:
        print("Invalid Credentials")


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


def is_valid_credentials(username: str, password: str) -> bool:
    database_filename = get_database_filename()

    connection = sqlite3.connect(database_filename)
    cursor = connection.cursor()

    # get password
    cursor.execute(f"SELECT password_hash FROM users WHERE username = '{username}'")
    row = cursor.fetchone()

    password_hash = ""
    if row is not None:
        password_hash = row[0]
    else:
        return False

    if password_hash == hash_string(password):
        return True


if __name__ == "__main__":
    main()
