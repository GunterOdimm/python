from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from crawler2 import Crawler
import time
import datetime as dt
import os
# 크롤러 클래스 만들기
crawler = Crawler()

# 크롬이 모바일 장치로 인식되도록 속성을 변경
options = webdriver.ChromeOptions()
mobile_emulation = {"deviceName": "Nexus 5"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

# 준비된 옵션을 적용한 상태로 크롬브라우저 열기
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

# 모든 동작마다 크롬브라우저가 준비될 때 까지 최대 10초씩 대기
driver.implicitly_wait(10)

  # Remove the CWD from sys.path while we load stuff.
# 수집을 원하는 페이지로 이동
# --> https://www.instagram.com/아이디/feed/
driver.get("https://www.instagram.com/kim_bora95/feed/")
time.sleep(2)
# 앱 설치 안내 영역 닫기
driver.find_element_by_css_selector(".glyphsSpriteWhite_Close").click()
# 이미지 URL 목록을 저장할 리스트
img_list = []

# 지정된 회차 동안 반복하면서 스크롤을 화면 맨 아래로 이동한다.
for i in range(0, 50):
    # 현재 페이지의 컨텐츠를 먼저 수집한다.
    
    while True:
        driver.find_element_by_css_selector(".coreSpriteRightChevron").click()
     
     img = crawler.select(driver.page_source, "img")
     for t in img:
        if 'srcset' in t.attrs:
            srcset = t.attrs['srcset']
            srcset_list = srcset.split(",")
            item = srcset_list[len(srcset_list)-1]
            url = item[:item.find(" ")]
            img_list.append(url)
    
     
    
     if not 'coreSpriteRightChevron' in img:
        break

    # 스크롤을 맨 아래로 이동
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     time.sleep(3)

    # 다음 컨텐츠가 로딩되는 동안 3초씩 대기
     
datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")
dirname = "%s_%s" % ('인스타이미지', datetime)

if not os.path.exists(dirname):
    os.mkdir(dirname)
    
for i, v in enumerate(img_list):
    fname = "%s/%04d.jpg" % (dirname, i+1)
    result = crawler.download(v, fname)
    
    if result:
        print("저장성공 >> ", fname)
    else:
        print("저장실패 >> ", fname)