import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    ) 
'''
               )

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
"""
#Создание 10 записей
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?,?,?,?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))


#Обновление баланса у каждой второй записи начиная с первой
for i in range(1, 11, 2):
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

#Удаление каждой третьей записи начная с первой
for i in range(1, 11,3):
        cursor.execute("DELETE FROM Users WHERE id = ?", (i,))
"""

cursor.execute("Select username,email,age,balance from Users where age != 60")
users = cursor.fetchall()

for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")


connection.commit()
connection.close()
