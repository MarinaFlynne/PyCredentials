#!/usr/bin/env python
"""
This is a small program that automates the creation of an initial database
"""
import sqlite3
import os
import db_tools


def main():
    """
    Main function of the program
    """
    # get the filename of the database
    database_filename = db_tools.get_database_filename()

    # Check if users.db already exists
    connection = sqlite3.connect(database_filename)
    cursor = connection.cursor()
    if os.path.exists(database_filename):
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
            os.remove(database_filename)
            print(f"Deleted database '{database_filename}'.")
        else:
            print("Exited database setup.")
            return

    # recreate database
    connection = sqlite3.connect(database_filename)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (username VARCHAR,password_hash VARCHAR);")
    connection.commit()
    connection.close()
    print(f"Created database '{database_filename}'.")


if __name__ == "__main__":
    main()
