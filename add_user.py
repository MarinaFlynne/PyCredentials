#!/usr/bin/env python
"""
This program allows one to add a user to the database.
"""
from hashlib import sha256
import sqlite3
import getpass
import db_tools


def does_user_exist(username: str) -> bool:
    """
    Checks whether the given username exists in the database
    :param username: username to check
    :param cursor: cursor for the database to check
    :return: whether the username exists in the database
    """
    database_filename = db_tools.get_database_filename()
    # establish connection to database
    connection = sqlite3.connect(database_filename)
    cursor = connection.cursor()

    # check if username exists in users table
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    row = cursor.fetchone()

    connection.close()
    # return result
    if row is not None:
        return True
    else:
        return False


def add_to_database(username, hashed_password):
    """
    adds the given username and hashed password to the database
    :param username:
    :param hashed_password:
    """
    database_filename = db_tools.get_database_filename()
    # establish connection to database
    connection = sqlite3.connect(database_filename)
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO users (username, password_hash) VALUES ('{username}', '{hashed_password}')")
    connection.commit()


def main():
    print("Adding a user to the database...")

    username: str = input("Enter username: ")
    # keep asking if user already exists
    while does_user_exist(username):
        print("Error: user already exists.")
        username: str = input("Enter Username: ")
    password: str = getpass.getpass("Enter Password: ")
    hashed_password: str = db_tools.hash_string(password)
    add_to_database(username, hashed_password)

    print("User successfully added.")


if __name__ == "__main__":
    main()
