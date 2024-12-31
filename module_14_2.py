import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("Select COUNT(*) From Users")
count = cursor.fetchone()[0]
cursor.execute("Select SUM(balance) From Users")
balance_sum = cursor.fetchone()[0]
cursor.execute("Select AVG(balance) From Users")
avg_balance_auto = cursor.fetchone()[0]

print(f"auto average balance = {avg_balance_auto}\nmanual average balance = {balance_sum / count}")

connection.close()
