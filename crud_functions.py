import sqlite3


def initiate_db():
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()

    cursor.execute('''
    SELECT * FROM Products
    ''')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products
