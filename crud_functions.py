import sqlite3
from Vitamin import vitamin


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
