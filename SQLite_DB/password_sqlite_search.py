import sqlite3
conn = sqlite3.connect('password.sqlite')

cursor = conn.execute('SELECT * FROM password')
rows = cursor.fetchall()
print(rows)