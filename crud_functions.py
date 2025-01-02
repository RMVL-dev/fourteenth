import sqlite3
from Vitamin import vitamin


def initiate_db():
    connection = sqlite3.connect("bot_database.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            img_url TEXT,
            price INTEGER
        ) 
    '''
                   )

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
            ) 
        '''
                   )

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("bot_database.db")
    cursor = connection.cursor()
    cursor.execute("Select title,description,img_url,price from Products")
    products_raw = cursor.fetchall()
    products = []
    for product in products_raw:
        products.append(vitamin(product))
    connection.close()
    return products


def add_user(email, age, username):
    connection = sqlite3.connect("bot_database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)", (username, email, age, 1000))
    connection.commit()
    connection.close()


def check_user_in_database(username):
    connection = sqlite3.connect("bot_database.db")
    cursor = connection.cursor()
    cursor.execute("Select username from Users where username = ?", (username,))
    user_in_database = True
    if len(cursor.fetchall()) == 0:
        user_in_database = False
    connection.close()
    return user_in_database
