import sqlite3

conn = sqlite3.connect('sqlite/example.db')
c = conn.cursor()

# symbol = 'RHAT'
# c.execute('''SELECT * FROM stocks
#                     WHERE symbol = "%s" ''' % symbol)

# t = ('RHAT',)
# sql = 'SELECT * FROM stocks WHERE symbol=?'
# c.execute(sql, t)
# print(c.fetchone())

# items = [
#     ('2020-07-09', 'BUY', 'IMB', 1000.0, 45.00), 
#     ('2020-07-10', 'SELL', 'RHAT', 100.0, 35.14), 
#     ('2020-07-11', 'BUY', 'MSFT', 500.0, 72.00), 
#     ('2020-07-12', 'SELL', 'APPLE', 200.0, 80.00),
# ]
# sql = "INSERT INTO stocks VALUES(?,?,?,?,?)"
# c.executemany(sql, items)
# conn.commit()

sql = "SELECT * FROM stocks ORDER BY price"
c.execute(sql)
rows = c.fetchall()
for row in rows:
    print(row)

c.close()
conn.close()
