import sqlite3

# connect BD
con = sqlite3.connect("data.db")
cursor = con.cursor()

p = cursor.execute(
    '''SELECT * FROM books INNER JOIN
            teachers ON books.year = teachers.id''')
k = p.fetchall()
print(k)

con.commit()
