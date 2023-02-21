#!/usr/bin/env python
"""
This is a small progeam that creates a database
"""
import sqlite3
import os

DATABASE_FILENAME = "users.db"


def does_table_exist(table_name: str, cursor) -> bool:
    """
    Checks if the given table exists in the database
    :param table_name: name of the table to be checked
    :param cursor: cursor for the database
    :return: whether the given table name exists in the database
    """
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def main():
    """
    Main function of the program
    """
    # Check if users.db already exists
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()
    if os.path.exists(DATABASE_FILENAME):
        # Check if users table exists
        if does_table_exist("users", cursor):
            print("Database exists already")

            # get every table in database and print the name of the table along with the number of rows
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table_list = cursor.fetchall()
            for table in table_list:
                table_name = table[0]
                cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
                row_count = cursor.fetchone()[0]
                print(f"Table '{table_name}' has {row_count} rows.")

            # get input from user
            prompt = "Would you like to erase database" \
                     " and create a new one? (y/n): "
            answer = input(prompt).lower()
            if answer == "y":
                # delete database and create new one
                connection.close()
                os.remove(DATABASE_FILENAME)
                print(f"Deleted database '{DATABASE_FILENAME}'.")
            else:
                print("Exited database setup.")
                return

    # recreate database
    connection = sqlite3.connect(DATABASE_FILENAME)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (username VARCHAR,password_hash VARCHAR);")
    connection.commit()
    connection.close()
    print(f"Created database '{DATABASE_FILENAME}'.")


if __name__ == "__main__":
    main()
