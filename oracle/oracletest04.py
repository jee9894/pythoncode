import cx_Oracle

conn = cx_Oracle.connect("HR/HR@localhost:1521/xe")
c = conn.cursor()
sql = '''select * from books where book_id=:id'''
c.execute(sql, id=1)
print(c.fetchall())
conn.close()