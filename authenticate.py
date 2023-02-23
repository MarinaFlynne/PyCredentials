#!/usr/bin/env python
"""
Program that prompts the user for their credentials and checks if the given credentials are valid (exist in database)
"""
import sqlite3
import db_tools


def main():
    username = input("Username: ")
    password = input("Password: ")
    if is_valid_credentials(username, password):
        print("Valid Credentials")
    else:
        print("Invalid Credentials")


def is_valid_credentials(username: str, password: str) -> bool:
    database_filename = db_tools.get_database_filename()

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

    if password_hash == db_tools.hash_string(password):
        return True


if __name__ == "__main__":
    main()
