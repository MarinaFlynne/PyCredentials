#!/usr/bin/env python
"""
This program allows one to add a user to the database.
"""
from hashlib import sha256
import sqlite3

DATABASE_FILENAME = "users.db"


def hash_string(string: str) -> str:
    string = string.encode('utf-8')
    string = sha256(string).hexdigest()
    return string


def add_to_database(username, hashed_password):
    # establish connection to database
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()




def main():
    print("Adding a user to the database:")
    username: str = input("Enter username: ")
    password: str = input("Enter password")
    hashed_password: str = hash_string(password)
    add_to_database(username, hashed_password)


if __name__ == "__main__":
    main()
