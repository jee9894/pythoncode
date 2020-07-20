import pymysql

conn = pymysql.connect( host = 'localhost', 
                        user = 'root',
                        password = 'qwer1234',
                        db = 'test',
                        charset = 'utf8',
                        cursorclass = pymysql.cursors.DictCursor)
c = conn.cursor()
sql = 'SELECT * FROM stocks WHERE symbol = %s'
t = ('RHAT',)
c.execute(sql, t)
print(c.fetchall())
conn.close()