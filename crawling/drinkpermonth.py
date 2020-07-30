from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome('./crawling/data/chromedriver')
driver.get('http://taas.koroad.or.kr/sta/acs/exs/typical.do?menuId=WEB_KMP_OVT_UAS_TSA')
# time.sleep(3)

driver.find_element_by_css_selector('#Navside .all-open').click() 
time.sleep(1)

# 사이드바에서 종류선택
driver.find_element_by_id('sdMenuTree85').click()
time.sleep(1)

year = '2005'

for i in range(1,13):
    # 시작연도선택
    select = Select(driver.find_element_by_id('startYear'))
    select.select_by_value(year)

    # 시작월선택
    select = Select(driver.find_element_by_id('startMonth'))
    select.select_by_value('%02d' % i)

    # 끝연도선택
    select = Select(driver.find_element_by_id('endYear'))
    select.select_by_value(year)

    # 끝월선택
    select = Select(driver.find_element_by_id('endMonth'))
    select.select_by_value('%02d' % i)

    # 조회 클릭
    driver.find_element_by_css_selector('#searchDiv > .top01-03 .rightBtn02').click()   
    # driver.find_element_by_class_name('ico_mail').click()
    time.sleep(8)

    # 확인된 ifrime으로 변경합니다.
    # driver.switch_to_frame('eosFrame')
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="eosFrame"]'))

    # driver.find_element_by_xpath('//*[@id="controlContainer"]/div[2]/div/div[3]').click()
    driver.find_element_by_css_selector('#controlContainer .ovToolbar .ovButtonContainer:nth-of-type(3)').click()

    Alert(driver).accept()
    time.sleep(2)

    # ifrime에서 원래 frame으로 돌아옵니다.
    driver.switch_to_default_content()

driver.close()