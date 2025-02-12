import sqlite3

conn = sqlite3.connect('lesson3.db')
cursor = conn.cursor()

for i in range(int(input('Enter count: '))):
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    grade = int(input('Enter grade: '))
    group = input('Enter group: ')
    cursor.execute("INSERT INTO  VALUES (?, ?, ?, ?)",
                   (name, surname, grade, group))
    conn.commit()

cursor.execute('SELECT grade FROM ')

conn.close()
