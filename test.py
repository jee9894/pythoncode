import time, datetime

movieDate = time.strftime('%Y%m%d', time.localtime(time.time()))
print(movieDate)

movieDate = '2020-02-02'
datetimeEx = datetime.datetime.strptime(movieDate, '%Y-%m-%d').date()
print(datetimeEx)