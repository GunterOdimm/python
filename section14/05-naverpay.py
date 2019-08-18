from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from matplotlib import pyplot
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(10)

driver.get('https://nid.naver.com/nidlogin.login')
#아이디 , 비빌번호 입력을 위한 JavaScript 구문 사용하기
user_id = 'sejew'
user_pw = 'dnjs1352@'

#전체문서 에서 id값에 의해 (ById) 요소 (Element)를 가져온 후(get) 입력값(value)를 지정
script = "document.getElementById('id').value='%s'"
driver.execute_script(script % user_id)

script = script = "document.getElementById('pw').value='%s'"
driver.execute_script(script % user_pw)

#로그인 버튼 클릭
btn = driver.find_element_by_css_selector(".btn_global")

#취득한 버튼을 클릭시킴 ==> 로그인
btn.click()

#로그인을 하는데 딜레이는 여러 가지 변수에 의해 느려질수도 빠를수도 있다
#그래서 아래 로그아웃이라는 버튼이 생길때까지 10초를 기다려라 하는
#혹은 특정 값이 나올때까지 임의의 시간동안 기다리라는 코드를 추가해준다.

WebDriverWait(driver,10).until(lambda x : x.find_element_by_id("account"))

driver.get("https://order.pay.naver.com/home?tabMenu=POINT_TOTAL")

WebDriverWait(driver,10).until(lambda x : x.find_element_by_id("content"))

while True:
    more_button = driver.find_element_by_css_selector("#_moreButton")

    attrs={}
    for item in more_button.get_property('attributes'):
        attrs[item['name']] = item['value']

        if ' style' in attrs:
            break

        driver.find_element_by_css_selector("#_moreButton").click()

        time.sleep(2)