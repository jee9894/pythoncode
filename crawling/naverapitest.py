import os
import sys
import urllib.request
import json

client_id = "YfRxYuAHCvwEe2oepzVW"
client_secret = "HlA4DXMlW8"
encText = urllib.parse.quote("아이언")
url = "https://openapi.naver.com/v1/search/movie.json?query=%s&display=10&genre=19" % (encText)# json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    result = json.loads(response_body)
    for movie in result['items']:
        print(movie['title'])
        print(movie['userRating'])
        print()

else:
    print("Error Code:" + rescode)

