#!/usr/bin/env python
"""
Checks if the given credentials exist in the database
"""
import yaml
from hashlib import sha256

CREDENTIAL_FILE = "credentials.yaml"


def main():
    username = input("Username: ")
    password = input("Password: ")
    if is_valid_credentials(username, password):
        print("Valid Credentials")
    else:
        print("Invalid Credentials")


def hash_string(string: str) -> str:
    string = string.encode('utf-8')
    string = sha256(string).hexdigest()
    return string


def get_credential_dict() -> dict:
    file = open(CREDENTIAL_FILE, "r")
    credential_list: list = yaml.safe_load(file)
    file.close()

    username_to_password_hash = {}
    for credential in credential_list:
        username_to_password_hash[credential["username"]] = credential["password_hash"]

    return username_to_password_hash


def is_valid_credentials(username: str, password: str) -> bool:
    username_to_password_hash: dict = get_credential_dict()

    if username_to_password_hash[username] == hash_string(password):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
