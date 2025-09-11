from getpass import getpass
import mysql.connector

try:
    with mysql.connector.connect (
        host = "127.0.0.1",
        port = 3303,
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database = "alx_book_store"
    ) as connection:
        create_book_table_query = """
        CREATE TABLE IF NOT EXISTS Books (
            book_id INT PRIMARY KEY,
            title VARCHAR(130),
            author_id INT,
            FOREIGN KEY (author_id) REFERENCES Authors(author_id),
            price DOUBLE,
            publication_date DATE
        );
        """
        create_authors_table_query = """
        CREATE TABLE IF NOT EXISTS Authors (
            author_id INT PRIMARY KEY,
            author_name VARCHAR(215)
        );
        """
        create_customers_table_query = """
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(215),
            email VARCHAR(215),
            address TEXT
        );
        """
        create_orders_table_query = """
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INT PRIMARY KEY,
            customer_id INT,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
            order_date DATE
        );
        """
        create_order_details_table_query = """
        CREATE TABLE IF NOT EXISTS Order_Details (
            orderdetailid INT PRIMARY KEY,
            order_id INT,
            book_id INT,
            quantity DOUBLE,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id),
            FOREIGN KEY (book_id) REFERENCES Books(book_id)
        );
        """
        with connection.cursor() as cursor:
            cursor.execute(create_authors_table_query)
            print("Table 'Authors' created successfully.")
            cursor.execute(create_book_table_query)
            print("Table 'Books' created successfully.")
            cursor.execute(create_customers_table_query)
            print("Table 'Customers' created successfully.")
            cursor.execute(create_orders_table_query)
            print("Table 'Orders' created successfully.")
            cursor.execute(create_order_details_table_query)
            print("Table 'Order_Details' created successfully.")
            connection.commit()
except mysql.connector.Error as e:
    print(e)