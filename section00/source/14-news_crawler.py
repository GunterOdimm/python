# -*- coding: utf-8 -*-

from crawler import Crawler
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
import datetime as dt
import os


#------------------------------------------------------------
# 1) 접속조건 설정하기
#------------------------------------------------------------
# 크롤링 모듈 객체
crawler = Crawler()

# 접속할 URL
URL = "https://news.naver.com/"

# 뉴스기사의 본문 URL을 저장할 리스트
url_list = []

# 뉴스 기사가 저장될 폴더이름 구성
datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")
dirname = "%s_%s" % ('뉴스기사', datetime)

# 뉴스기사를 텍스트 파일로 저장할 폴더 만들기
if not os.path.exists(dirname):
    os.mkdir(dirname)

#------------------------------------------------------------
# 2) 수집할 뉴스기사의 URL 조사하기
#------------------------------------------------------------
# 가져온 URL에서 링크에 대한 셀렉터를 크롤링 -> 반환결과는 List형태
# -> 여러 형식의 셀렉터를 동시에 처리해야 할 경우 콤마(,)로 구분하여 지정한다.
link_list = crawler.select(URL, encoding="euc-kr",
                    selector=".newsnow_tx_inner > a, .newsnow_imgarea > a, .mtype_img > dt > a, .mlist2 > li > a")

# 가져온 결과 확인하기
for item in link_list:
    print(item)
    print("-" * 30)

# 리스트의 원소들에 대한 반복 처리
for item in link_list:
    print(type(item.attrs))
    # 각 원소(링크)에 속성들(attrs) 중에
    # href 속성이 있다면 그 속성값을 별도로 준비한 리스트에 추가
    if "href" in item.attrs:
        # href속성은 링크를 클릭했을 때의 URL을 의미한다.
        # URL에 뉴스 상세 페이지의 파일명인 "read.nhn"이 포함되어 있다면
        # 해당 주소를 url_list에 추가한다.
        if "read.nhn" in item['href']:
            url_list.append(item['href'])

# 집계된 리스트의 주소들 확인하기
for v in url_list:
    print(v)

#------------------------------------------------------------
# 3) 뉴스기사에 접속하여 본문 크롤링 하기
#------------------------------------------------------------
# 기사의 본문을 누적해서 저장할 문자열 변수
news_content = ''

# URL 목록만큼 반복
for i, url in enumerate(url_list):
    print("%d번째 뉴스기사 수집중... >> %s" % (i+1, url))

    # URL에 접근하여 뉴스 컨텐츠를 가져온다.
    news_html = crawler.select(url, selector='#main_content', encoding='euc-kr')

    # 가져온 내용이 없다면?
    if not news_html:
        print("%d번째 뉴스기사 크롤링 실패" % (i+1))
        # 반복 수행에 대한 현재 회차를 종료하고 증감식으로 다시 이동
        continue

    # id속성은 고유항목이므로 리스트의 원소는 단 한개이다. -> 0번째 항목을 바로 추출한다.
    news_html_item = news_html[0]

    # 가져온 내용이 있다면 기사의 제목과 내용 추출 시작
    title_str = ""      # 기사 제목이 저장될 문자열
    content_str = ""    # 기사 내용이 저장될 문자열

    # 가져온 내용에서 제목에 대한 리스트를 추출한다.
    title = news_html_item.select("#articleTitle")

    # 가져온 제목이 존재한다면?
    if title:
        # id속성은 고유항목이므로 리스트의 원소는 단 한개이므로
        # -> 0번째 항목의 텍스트를 추출한다.
        title_str = title[0].text.strip()

        # 기사 제목에서 파일이름으로 사용할 수 없는 특수문자 제거
        title_str = title_str.replace("'", "").replace("\"", "").replace("?", "").replace("“", "").replace("”", "").replace("/", "").replace(">", "").replace("<", "")
        print(title_str)


    # 가져온 내용에서 본문에 대한 리스트를 추출한다.
    content = news_html_item.select("#articleBodyContents")

    # 가져온 본문이 존재한다면?
    if content:
        # id속성은 고유항목이므로 리스트의 원소는 단 한개이다.
        # -> 0번째 항목의 텍스트를 추출한다.
        news_text = content[0]

        # 기사 본문에 포함되어 있는 불필요한 태그들을 걸러낸다.
        crawler.remove(news_text, 'script')
        crawler.remove(news_text, 'a')
        crawler.remove(news_text, 'br')
        crawler.remove(news_text, 'span', {'class': 'end_photo_org'})

        # 공백을 제거한 텍스트만 추출
        content_str = news_text.text.strip()

        # 워드클라우드 생성을 위해 전체 기사 내용을 하나의 변수에 누적한다.
        news_content += content_str


    # 제목과 내용이 모두 존재한다면?
    if title_str and content_str:
        # 기사 제목을 파일명으로 지정하여 내용을 텍스트로 저장한다.
        fname = dirname + "/" + title_str + ".txt"
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content_str)

#------------------------------------------------------------
# 4) 수집결과를 기반으로 형태소 분석
#------------------------------------------------------------
# 형태소 분석 객체를 통해 수집된 뉴스 본문에서 명사만 추출
nlp = Okt()
nouns = nlp.nouns(news_content)
count = Counter(nouns)              # 명사들에 대한 빈도수 검사
most = count.most_common(100)       # 가장 많이 사용된 단어 100개 추출

# 추출 결과를 워드 클라우드에서 요구하는 형식으로 재구성
# --> {"단어": 빈도수, "단어": 빈도수 ...}
tags = {}
for n, c in most:
    if len(n) > 1:
        tags[n] = c

#------------------------------------------------------------
# 5) 수집결과를 활용하여 워드클라우드 생성
#------------------------------------------------------------
# 워드 클라우드 객체 만들기
wc = WordCloud(font_path="NanumGothic", max_font_size=200,
               width=1200, height=800, background_color='#ffffff')

wc.generate_from_frequencies(tags)      # 미리 준비한 딕셔너리를 통해 생성
wc.to_file("news_%s.png" % datetime)  # 워드 클라우드 이미지 저장
