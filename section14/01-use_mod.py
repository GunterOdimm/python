# -*- coding: utf-8 -*-

from crawler import Crawler
from sample import naver_news_url
from sample import image_url

#모듈객체 생성하기.
crawler = Crawler()

#이미지 파일 내려받기
savename = crawler.download(image_url, filename="download.jpg")
print(savename +"(이)가 저장되었습니다.")
print("-"* 30)

element = crawler.select(naver_news_url,encoding="euc-kr", selector='#articleBodyContents')

for item in element:
    crawler.remove(item,'script')
    crawler.remove(item, 'a')
    crawler.remove(item, 'br')
    crawler.remove(item, 'sapn',{'class': 'end_photo_org'})

print(item.text.strip())