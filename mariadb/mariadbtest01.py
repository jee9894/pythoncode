import pymysql

conn = pymysql.connect( host = 'localhost', 
                        user = 'root',
                        password = 'qwer1234',
                        db = 'test',
                        charset = 'utf8',
                        cursorclass = pymysql.cursors.DictCursor)

c = conn.cursor()
sql = '''
    CREATE TABLE IF NOT EXISTS stocks (
        data text,
        trans text,
        symbol text,
        qty real,
        price real
    )'''
c.execute(sql)

c.execute('''INSERT INTO stocks VALUES('2020-07-08','BUY','RHAT',100,35.14)''')
conn.commit()
conn.close()