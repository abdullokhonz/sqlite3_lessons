import sqlite3
from tkinter import *

con = sqlite3.connect('lesson5.db')
cursor = con.cursor()

window = Tk()
window.geometry('300x300+100+100')
window.title('Work with database')


def getrow():
    cursor.execute('SELECT name, surname FROM  WHERE grade<5')
    rows = cursor.fetchall()
    for row in rows:
        text = ''
        for el in row:
            text = text + str(el) + ' '
        LBinfo.insert(END, text)


LBinfo = Listbox(window, width=30)
LBinfo.pack()

B = Button(text='Получить запись', width=15, height=2, command=getrow)
B.pack()

window.mainloop()
