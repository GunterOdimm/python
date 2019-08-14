# -*- coding: utf-8 -*-

from crawler import Crawler
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from matplotlib import pyplot
from collections import Counter
from konlpy.tag import Okt
import datetime as dt
import os

crawler = Crawler()

URL = "https://news.naver.com/"

url_list =[]

datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")
dirname = "%s_%s" %('뉴스기사', datetime)

if not os.path.exists(dirname):
    os.mkdir(dirname)

link_list = crawler.select(URL, encoding ="euc-kr", selector = ".newsnow_tx_inner > a, .newsnow_imgarea > a, .mtype_img > dt > a, .mlist2 > li > a")

for item in link_list:
    print(item)
    print("-" * 30)

for item in link_list:
    print(type(item.attrs))
    if "href" in item.attrs:
        if "read.nhn" in item['href']:
            url_list.append(item['href'])
for v in url_list:
    print(v)
news_content = ''

for i, url in enumerate(url_list):
    print("%d 번째 뉴스기사 수집중... >> %s" %(i+1, url))

    news_html = crawler.select(url, selector = '#main_content', encoding='euc-kr')

    if not news_html:
        print("%d 번째 뉴스기사 크롤링 실패" % (i+1))
        continue
    news_html_item = news_html[0]

    title_str = ""
    content_str = ""

    title = news_html_item.select("#articleTitle")

    if title:
        title_str = title[0].text.strip()

        title_str = title_str.replace("'","").replace("\"","").replace("?","").replace(""","").replace(""","").replace("/","").replace(">","").replace("<","")
        print(title_str)

    content = news_html_item.select("#articleBodyContents")

    if content:
        news_text = content[0]

        crawler.remove(news_text,'script')
        crawler.remove(news_text, 'a')
        crawler.remove(news_text,'br')
        crawler.remove(news_text,'span',{'class': 'end_photo_org'})

        content_str = news_text.text.strip()
        news_content += content_str

    if title_str and content_str:
        fname = dirname + "/" +title_str + ".txt"
        with open(fname, 'w',encoding='utf-8')as f:
            f.write(content_str)

nlp = Okt()
nouns = nlp.nouns(news_content)
count = Counter(nouns)
most - count.most_common(100)

tags = {}
for n, c in most:
    if len(n) > 1:
        tags[n] =c

wc = WordCloud(font_path = "NanumGothic", max_font_size=200, width=1200, height=800, background_color= #ffffff)

wc.generate_from_frequencies(tags)

wc.to_file("news_%s.png" % datetime)