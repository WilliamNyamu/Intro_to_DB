from getpass import getpass
import mysql.connector

try:
    with mysql.connector.connect (
        host = "127.0.0.1",
        port = 3303,
        user = input("Enter username: "),
        password = getpass("Enter password: ")
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            connection.commit()
            print("Database 'alx_book_store' created successfully.")
except mysql.connector.Error as e:
    print(e)