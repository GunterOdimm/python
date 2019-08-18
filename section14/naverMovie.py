# -*- coding: utf-8 -*-

import requests
from crawler import Crawler
from bs4 import BeautifulSoup
from matplotlib import pyplot
from collections import Counter
from konlpy.tag import Okt
from urllib.request import urlretrieve
import datetime as dt
import os
import ssl
import openpyxl

crawler = Crawler()
# datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")
dirname = ('영화순위')
#본격적으로 코드를 들어가기전에..
#이코드는 URL뒤에 pageNum 함수가 붙어야합니다 지금은 테스트 하기위해서 단순하게 1페이지만 조회중입니다.
#마지막에 저장 하는 코드는 삭제해도 무방합니다 다만 영화 줄거리가 워낙에 길어서 따로 저장하는것을 추천합니다.
#이 코드의 최종 목적지는 mysql연동입니다 아직 구현 안된 부분 입니다.

for i in range(1,2):
    pageNum = str(i)

    URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190815&page='+ pageNum
    url_list =[]
    point_str = ""


    if not os.path.exists(dirname):
        os.mkdir(dirname)

    link_list = crawler.select(URL, encoding ="euc-kr", selector = "tr > .title > .tit5 > a")
    for j in range(1,41):
        pointNum = str(j)
        point = crawler.select(URL, encoding ="euc-kr", selector = "tbody  tr:nth-of-type("+ pointNum +")  .point")
        if point:
            point_str = point[0].text.strip()
            point_str = point_str.replace("'","").replace("\"","").replace("?","").replace(""","").replace(""","").replace("/","").replace(">","").replace("<","")
            print(point_str)

    for item in link_list:
        # print(item)
        if "href" in item.attrs:
            url_list.append("https://movie.naver.com"+item['href'])

    # for v in url_list:
    #     print(v)
    movie_content = ''

    for i, url in enumerate(url_list):

        movie_html = crawler.select(url, selector = '.article', encoding='utf-8')
        link_list2 = crawler.select(url, encoding="utf-8", selector = ".mv_info_area > .poster > a > img" )
        #네이버영화는 영화 상세 정보 페이지가 utf-8입니다 왜캐 번거로운지..
        # print(movie_html)
        if not movie_html:
            # print("%d 번째 영화정보 수집 실패" % (i+1))
            continue
        movie_html_item = movie_html[0]

        title_str = ""
        content_str = ""
        director_str = ""
        actor_str = ""
        genre_str = ""

        title = movie_html_item.select("h3 > a")

        if title:
            title_str = title[0].text.strip()

            title_str = title_str.replace("'","").replace("\"","").replace("?","").replace(""","").replace(""","").replace("/","").replace(">","").replace("<","")

        # print("영화 제목 : " + title_str)
        director = movie_html_item.select("dd > p > a")

        if director:
            director_str = director[0].text.strip()
            director_str = director_str.replace("'","").replace("\"","").replace("?","").replace(""","").replace(""","").replace("/","").replace(">","").replace("<","")
        # print("감독 : " + director_str)



        genre = movie_html_item.select("dd > p > span > a")
        # print(genre)
        if genre:
            genre_str = genre[0].text.strip()
            genre_str = genre_str.replace("'","").replace("\"","").replace("?","").replace(","").replace(""","").replace("/","").replace(">","").replace("<","")
        # print(genre)
        # print("장르 : " +genre_str)

        content = movie_html_item.select(".con_tx")

        if content:
            movie_text = content[0]

            crawler.remove(movie_text,'script')
            crawler.remove(movie_text, 'a')
            crawler.remove(movie_text,'br')
            crawler.remove(movie_text,'span',{'class': 'end_photo_org'})

            content_str = movie_text.text.strip()
        # print("영화 줄거리 : " + content_str)
        link_list2 = crawler.select(url, encoding="utf-8", selector = ".mv_info_area > .poster > a > img" )
        img =""
        if link_list2:
            img = link_list2[0]

        urlretrieve(img.attrs["src"], "naver_img/" + title_str + ".png")

        if title_str and content_str:
            fname = dirname + "/" +title_str + ".txt"
            with open(fname, 'w',encoding='utf-8')as f:
                f.write(content_str)
