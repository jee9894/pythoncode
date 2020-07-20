from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./crawling/data/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(3)

id = 'jee9894'
pw = 'exercisehard3%%'

# driver.find_element_by_id('id').send_keys(id)
# driver.find_element_by_id('pw').send_keys(pw)
# driver.find_element_by_id('log.login').click()

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="new.dontsave"]').click()
time.sleep(1)

driver.find_element_by_class_name('ico_mail').click()
time.sleep(1)

# mails = driver.find_element_by_class_name('mailList')
# mails = mails.find_elements_by_css_selector('li')
# for mail in mails:
#     title = mail.find_element_by_css_selector('.mTitle a:nth-of-type(1)').text
#     summ = mail.find_element_by_css_selector('.subject a:nth-of-type(1) strong').text
#     print('제목 : ' + title)
#     print('요약 : ' + summ)

driver.get('https://mail.naver.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
mails = soup.select('#list_for_view .mTitle')
# print(mails)
for mail in mails:
    # print(mail.prettify())
    title = mail.select_one('.name a:nth-of-type(1)').get_text()
    summ = mail.select_one('.subject a:nth-of-type(1) strong').get_text()
    print('제목 : ' + title)
    print('요약 : ' + summ)
    print()
    # break

driver.close()