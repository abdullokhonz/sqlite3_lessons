import sqlite3

conn = sqlite3.connect('lesson2.db')
cursor = conn.cursor()

cursor.execute('SELECT grade FROM ')

# fetchone
# print(cursor.fetchone())
# print(cursor.fetchone())

# fetchall
# print(*cursor.fetchall(), sep='\n')

for row in cursor.fetchall():
    print(int(*row) + int(*row))

# [print(row[0], row[1]) for row in cursor.fetchall()]
