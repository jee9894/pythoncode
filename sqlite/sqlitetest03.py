import sqlite3, csv

input_file = 'sqlite/input.csv'

conn = sqlite3.connect('sqlite/supplier.db')
c = conn.cursor()

sql = '''
    create table if not exists suppliers(
        supplier_name varchar(20),
        invoice_number varchar(20),
        part_number varchar(20),
        cost float,
        purchase_date varchar(20)
    )'''
c.execute(sql)

sql = "delete from suppliers"
c.execute(sql)

conn.commit()

file_reader =  csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
print(type(file_reader))
print(header)
data = []
for row in file_reader:
    data.append(row)
print(data)
print(type(data))

sql = 'insert into suppliers values(?,?,?,?,?)'
c.executemany(sql, data)
conn.commit()

c.close()
conn.close()
