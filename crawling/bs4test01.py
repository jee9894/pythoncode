from platform import python_branch
import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

# req = requests.get('https://www.starbucks.co.kr/store/store_map.do')
# soup = BeautifulSoup(req.text, 'html.parser')

driver = webdriver.Chrome('./crawling/data/chromedriver')
driver.get('https://www.starbucks.co.kr/store/store_map.do')
time.sleep(1)

# source = driver.page_source
# st_bs = BeautifulSoup(source, 'html.parser')
# print(st_bs.select('#mCSB_1_container li'))

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(1)

sido = driver.find_element_by_class_name('sido_arae_box')
# print(sido)
li = sido.find_elements_by_tag_name('li')
# print(li)
li[3].click()
time.sleep(1)

gugun = driver.find_element_by_class_name('gugun_arae_box')
li = gugun.find_elements_by_tag_name('li')
li[2].click()
time.sleep(1)

# result = driver.find_element_by_class_name('quickSearchResultBoxSidoGugun')
# li = result.find_elements_by_tag_name('li')
# print(len(li))
# i=0
# for l in li:
#     title = l.find_element_by_tag_name('strong')
#     addr = l.find_element_by_tag_name('p')
#     print("매장명 :", title.text)
#     print("상세 :", addr.text)
#     i+=1
# print(i)

source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
result = soup.find('ul', {'class':'quickSearchResultBoxSidoGugun'})
for i in result.find_all('li'):
    title = i.find('strong')
    addr = i.find('p')
    print("매장명 :", title.string)
    print("상세 :", addr.string)