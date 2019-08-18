# -*- coding: utf-8 -*-

from crawler import Crawler
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from collections import Counter
import datetime as dt
from pandas import DataFrame
import os


#------------------------------------------------------------
# 1) 접속조건 설정하기
#------------------------------------------------------------
# 크롤링 모듈 객체
crawler = Crawler()

# 접속할 URL
URL = "https://movie.naver.com/movie/running/current.nhn?order=reserve"

#------------------------------------------------------------
# 2) 수집할 뉴스기사의 URL 조사하기
#------------------------------------------------------------
# 본문 URL을 저장할 리스트
url_list = []

# 가져온 URL에서 링크에 대한 셀렉터를 크롤링 -> 반환결과는 List형태
# -> 여러 형식의 셀렉터를 동시에 처리해야 할 경우 콤마(,)로 구분하여 지정한다.
link_list = crawler.select(URL, encoding="utf-8", selector=".tit > a")

# 리스트의 원소들에 대한 반복 처리
for item in link_list:
    print(type(item.attrs))
    # 각 원소(링크)에 속성들(attrs) 중에
    # href 속성이 있다면 그 속성값을 별도로 준비한 리스트에 추가
    if "href" in item.attrs:
        # href속성은 링크를 클릭했을 때의 URL을 의미한다.
        # URL에 뉴스 상세 페이지의 파일명인 "read.nhn"이 포함되어 있다면
        # 해당 주소를 url_list에 추가한다.
        if "basic.nhn" in item['href']:
            url = item['href']
            title = item.text.strip()
            p = url.rfind("=")
            code = url[p+1:]
            item_dict = {"title": title, "code": code, "url": url}
            url_list.append(item_dict)

df = DataFrame(url_list)
print(df)
