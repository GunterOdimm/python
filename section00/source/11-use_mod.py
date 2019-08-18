# -*- coding: utf-8 -*-

# 필요한 모듈 참조하기
from crawler import Crawler

# sample.py에서 필요한 데이터 참조
from sample import naver_news_url   # 가져올 뉴스의 URL
from sample import image_url        # 다운로드 할 이미지의 URL

#--------------------------------------------------
# 모듈객체 생성하기
#--------------------------------------------------
crawler = Crawler()

#--------------------------------------------------
# 이미지 파일 내려받기
#--------------------------------------------------
savename = crawler.download(image_url, filename="download.jpg")
print(savename + "(이)가 저장되었습니다.")
print("-" * 30)

#--------------------------------------------------
# 웹 페이지 크롤링
#--------------------------------------------------
# -> 가져올 페이지의 URL과 추출할 영역의 CSS 셀렉터를 지정한다.
# -> encoding이 utf-8인 경우는 파라미터 설정을 생략한다. (기본값 사용)
element = crawler.select(naver_news_url,
                 encoding="euc-kr", selector='#articleBodyContents')

# 크롤링 결과의 원소 수 만큼 반복하면서 불필요한 태그를 제거한다.
for item in element:
    crawler.remove(item, 'script')
    crawler.remove(item, 'a')
    crawler.remove(item, 'br')
    crawler.remove(item, 'span', {'class': 'end_photo_org'})

    # 크롤링 처리된 최종 결과
    print(item.text.strip())
