# -*- coding: utf-8 -*-

# 모듈 가져오기
from crawler import Crawler
import urllib
import json
import datetime as dt
import os

#-----------------------------------------------
# 검색에 필요한 정보 준비
#-----------------------------------------------
# 카카오에서 발급받은 인증키
auth = {'Authorization': 'KakaoAK 발급받은인증키적용'}

# 카카오 인증키를 HTTP Header에 포함시켜야 하므로 크롤러 모듈의 생성자로 전달한다.
crawler = Crawler(header=auth)

max_page = 5                # 최대 페이지 수 (1~50)
group_count = 80            # 한 페이지당 가져올 데이터 수 (1~80)
keyword = '고화질 바탕화면' # 검색어

#-----------------------------------------------
# 검색어_현재시각 형식으로 이미지가 저장될 폴더를 생성한다.
#-----------------------------------------------
# 현재시각
datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")

# 검색어에 포함된 공백은 언더바로 변환한 후 폴더이름 구성
dirname = "%s_%s" % (keyword.replace(' ', '_'), datetime)

# 폴더 생성하기
if not os.path.exists(dirname):
    os.mkdir(dirname)

#-----------------------------------------------
# 지정된 최대 페이지 수 만큼 반복처리
#-----------------------------------------------
# 저장되는 이미지의 수를 카운트 하기 위한 변수
counter = 1

# 0~최대 페이지 수 전까지 반복한다.
for num in range(0, max_page):
    # https://dapi.kakao.com/v2/search/image?page=1&size=80&query=검색어
    # 에서 ? 뒤의 값들만 딕셔너리로 변환
    params = {"page": num + 1, "size": group_count, "query": keyword}

    # 웹 페이지에 전달하는 변수는 한글을 포함할 수 없으므로 한글이 포함된 경우
    # 인코딩 처리를 거쳐야 한다.
    query = urllib.parse.urlencode(params)

    # 검색 URL 생성
    site_url = "https://dapi.kakao.com/v2/search/image?" + query
    print(site_url)

    # 생성된 URL에 접속하여 결과를 가져온다.
    result = crawler.get(site_url)

    # 결과가 존재한다면?
    if (result):
        # json 결과를 딕셔너리로 변환
        data = json.loads(result)

        # List가 포함된 부분에 대한 반복 처리
        for item in data["documents"]:
            # 이미지가 저장될 "폴더/파일이름" 구성
            fname = "%s/%04d.jpg" % (dirname, counter)
            # List에서 이미지 주소를 추출하여 준비된 파일 이름으로 저장되도록 다운로드
            ok = crawler.download(item["image_url"], filename=fname)

            if ok:
                print(ok + "(이)가 저장되었습니다.")
            else:
                print(" >>> [Error] " + item["image_url"] + " 저장에 실패했습니다.")

            counter += 1
