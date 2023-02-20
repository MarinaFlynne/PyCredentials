#!/usr/bin/env python
"""
TODO write desription of file
"""
import yaml

def main():
    username = input("Username: ")
    password = input("Password: ")
    if is_valid_credentials(username, password):
        print("Valid Credentials")
    else:
        print("Invalid Credentials")


def is_valid_credentials(username: str, password: str) -> bool:
    if username == "Marina" and password == "1234":
        return True
    else:
        return False


if __name__ == "__main__":
    main()