# -*- coding: utf-8 -*-

# 모듈 가져오기
from crawler import Crawler
from print_df import print_df   # 출력기능 모듈
from pandas import DataFrame    # 데이터 프레임
import pandas as pd             # 데이터 프레임 병합 함수를 위해 pandas 참조
import urllib

#-----------------------------------------------
# 검색에 필요한 정보 준비
#-----------------------------------------------
df = DataFrame()                                # 결과를 저장할 빈 데이터 프레임
keyword = '노트북'                              # 검색어
params = {"query": keyword, "frm": "NVSHATC"}   # `?` 이후의 변수들을 딕셔너리 구조로 생성
# 딕셔너리를 URL에 추가할 수 있는 형태로 인코딩 (한글이 포함된 경우 필수)
query = urllib.parse.urlencode(params)

# 크롤링 할 사이트 주소 -> 네이버 쇼핑에서 "노트북"으로 검색한 결과
site_url = "https://search.shopping.naver.com/search/all.nhn?" + query
print_df(site_url)


#-----------------------------------------------
# # 상품 목록 영역 가져오기
#-----------------------------------------------
crawler = Crawler()
html = crawler.select(site_url, selector=".info")

# 검색된 상품목록 영역 수 만큼 반복
for item in html:
    # 하나의 상품 정보를 담기 위한 빈 딕셔너리
    info = {}

    # 상품명 추출
    # -> class 이름으로 상품명 영역 추출
    title_list = item.select('.tit')
    # -> 상품명은 하나만 존재하므로 0번째에 직접 접근하여 텍스트 추출
    title = title_list[0].text.strip()
    # -> 추출된 결과를 빈 딕셔너리에 추가
    info['제품명'] = title

    # 가격 추출
    # -> class 이름으로 가격 영역 추출
    price_list = item.select('.num')
    # -> 가격은 하나만 존재하므로 0번째에 직접 접근하여 텍스트 추출
    price = price_list[0].text.strip()
    # -> 상품 가격에 포함된 콤마를 빈 문자열로 변경
    price = price.replace(",", "")
    # -> 정수형으로 변환
    price = int(price)
    # -> 추출된 결과를 빈 딕셔너리에 추가
    info['가격'] = price

    # 노트북 스팩 영역 추출
    # -> class 이름으로 접근하여 그 하위의 링크 추출
    spec_list = item.select('.detail a')

    # -> 제품별로 스팩 항목이 여러개 이므로 추출된 결과만큼 반복
    for v in spec_list:
        v = v.text.strip() # -> 텍스트 추출
        tmp = v.split(":") # -> 콜론으로 분리 (ex: 디스플레이 : 1920x1080 )

        if len(tmp) == 2:  # -> 길이가 2라면 key와 value로 분리하여 딕셔너리에 추가
            key = tmp[0].strip()
            value = tmp[1].strip()
            info[key] = value

    # 개별 상품 정보를 담고 있는 빈 딕셔너리를 데이터 프레임으로 변환
    item_df = DataFrame([info], columns=info.keys())

    # 맨 처음 준비한 빈 딕셔너리에 개별 상품에 대한 데이터 프레임을 병합
    # --> concat 함수는 데이터 프레임들의 모든 행을 하나의 데이터프레임으로 모아서 병합한다.
    # --> 이 과정에서 서로 열이 다르더라도 sort=False 파라미터가 있다면,
    #     열을 추가하는 형태로 병합한다.
    df = pd.concat([df, item_df], sort=False)



#-----------------------------------------------
# 결과확인
#-----------------------------------------------
# 생성된 데이터 프레임 확인
print_df(df.head())

# 데이터 프레임을 엑셀로 저장
df.to_excel("노트북.xlsx", index=False)
