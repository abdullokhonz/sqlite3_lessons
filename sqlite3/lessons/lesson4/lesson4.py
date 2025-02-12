import tkinter
import sqlite3

root = tkinter.Tk()
root.geometry('500x500+500+150')
root.resizable(False, False)
root.title('DataBase')

conn = sqlite3.connect('lesson4.db')
cursor = conn.cursor()

cursor.execute('SELECT name, surname, grade, [group] FROM ')

for i in cursor.fetchall():
    label = tkinter.Label(text=i, font=16)
    label.pack(anchor='nw')

root.mainloop()
conn.close()
