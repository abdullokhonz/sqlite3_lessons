import sqlite3
# from tkinter import *

con = sqlite3.connect('lesson7.db')
cursor = con.cursor()

# cursor.execute('CREATE TABLE Books(ID INTEGER PRIMARY KEY AUTOINCREMENT, Author TEXT, Name TEXT, Year INTEGER)')
# cursor.execute('UPDATE  SET ID_Book = 2')

id_book = cursor.execute('SELECT id FROM books WHERE name = "Scared by assault"').fetchall()[0][0]
student = cursor.execute('SELECT name, surname FROM  WHERE id_book = (?)', (id_book,)).fetchall()[0]
print(*student)

# con.commit()
