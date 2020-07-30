import os
import sys
from test import movieDate
import urllib.request
import json
import datetime, time

movieDate = time.strftime('%Y%m%d', time.localtime(time.time()))
datetimeObj = datetime.datetime.strptime('%Y%m%d', movieDate).date()
movieDate = (datetimeObj - datetime.timedelta(days=1)).strftime('%Y%m%d')

key = '3180a828a229d025fdf5b16af475063f'
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=%s&targetDt=%s&multiMovieYn=%s&repNationCd=%s" % (key,movieDate,'N', 'K')# json 결과
request = urllib.request.Request(url)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    result = json.loads(response_body)
    # print(result['boxOfficeResult']['dailyBoxOfficeList'])
    for movie in result['boxOfficeResult']['dailyBoxOfficeList']:
        print("순위 : " + movie['rank'])
        print("제목 : " + movie['movieNm'])
        print()

else:
    print("Error Code:" + rescode)

