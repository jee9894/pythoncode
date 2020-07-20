import pymysql

conn = pymysql.connect( host = 'localhost', 
                        user = 'root',
                        password = 'qwer1234',
                        db = 'test',
                        charset = 'utf8',
                        cursorclass = pymysql.cursors.DictCursor)
c = conn.cursor()

items = [
    ('2020-07-09', 'BUY', 'IMB', 1000.0, 45.00), 
    ('2020-07-10', 'SELL', 'RHAT', 100.0, 35.14), 
    ('2020-07-11', 'BUY', 'MSFT', 500.0, 72.00), 
    ('2020-07-12', 'SELL', 'APPLE', 200.0, 80.00),
]
sql = '''INSERT INTO stocks VALUES(%s,%s,%s,%s,%s)'''
c.executemany(sql, items)
conn.commit()
conn.close()