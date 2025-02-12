import sqlite3
from tkinter import *

con = sqlite3.connect('lesson6.db')
cursor = con.cursor()

window = Tk()
window.geometry('300x350+100+100')
window.title('Work with database')


def getrow():
    cursor.execute('SELECT name, surname FROM  WHERE grade<5')
    rows = cursor.fetchall()
    for row in rows:
        text = ''
        for el in row:
            text = text + str(el) + ' '
        LBinfo.insert(END, text)


def add_student():
    def save():
        name = ent_name.get()
        surname = ent_surname.get()
        grade = ent_grade.get()
        group = ent_group.get()

        cursor.execute('INSERT INTO  VALUES (?, ?, ?, ?)', (name, surname, grade, group))
        con.commit()

        new_window.grab_release()
        new_window.destroy()

    new_window = Tk()
    new_window.geometry('300x300+100+100')
    new_window.title('Work with database')

    lab_name = Label(new_window, text='Имя:')
    ent_name = Entry(new_window, )
    lab_name.pack()
    ent_name.pack()

    lab_surname = Label(new_window, text='Фамилия:')
    ent_surname = Entry(new_window, )
    lab_surname.pack()
    ent_surname.pack()

    lab_grade = Label(new_window, text='Класс:')
    ent_grade = Entry(new_window, )
    lab_grade.pack()
    ent_grade.pack()

    lab_group = Label(new_window, text='Группа:')
    ent_group = Entry(new_window, )
    lab_group.pack()
    ent_group.pack()

    btn_save = Button(new_window, text='Сохранить', width=15, height=2, command=save)
    btn_save.pack()

    new_window.grab_set()
    new_window.mainloop()


LBinfo = Listbox(window, width=30)
LBinfo.pack()

B = Button(text='Получить запись', width=15, height=2, command=getrow)
B.pack()

del_b = Button(text='Удалить строку', width=15, height=2, command=lambda: LBinfo.delete(END))
del_b.pack(pady=15)

add_b = Button(text='Добавить студента', width=15, height=2, command=add_student)
add_b.pack()

# cursor.execute('DELETE FROM  WHERE grade = 6')
# cursor.execute('UPDATE  SET name = "Base" WHERE grade = 11')
# cursor.execute('SELECT name FROM ')

# con.commit()

# rows = cursor.fetchall()
# print(rows)

window.mainloop()
