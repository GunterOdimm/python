#-*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup

class Crawler:
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

    session = None

    def __init__(self, header={}, referer=None):
        ses_info = {'referer': referer, 'User-agent': self.user_agent}

        if header:
            keys = list(header.keys())
            for k in keys:
                ses_info[k] = header[k]

        self.session = requests.Session()

        self.session.headers.update(ses_info)

    def get(self, url, encoding='utf-8'):
        try:
            r = self.session.get(url)
        except:
            print("[Network Error] Connection Fail")
            return None

        if r.status_code != 200:
            print("[%d Error] %s" % (r.status_code, r.reason))
            return None

        r.encoding = encoding

        return r.text.strip()

    def select(self, url, selector='html', encoding='utf-8'):
        source = self.get(url, encoding)

        if not source:
            return None

        soup = BeautifulSoup(source, 'html.parser')

        return soup.select(selector)

    def url_select(self, url, selector='html', encoding='utf-8'):
        # 웹 페이지 접속 함수를 호출하여 소스코드 리턴받기
        source = self.get(url, encoding)

        # 리턴값이 없다면 처리 중단
        if not source:
            return None

        # 웹 페이지의 소스코드 HTML 분석 객체로 생성
        soup = BeautifulSoup(source, 'html.parser')

        # CSS 선택자를 활용하여 가져오기를 원하는 부분 지정
        # -> list로 리턴
        return soup.select(selector)


    def remove(self, item, tag, selector=None):
        for target in item.find_all(tag, selector):
            target.extract()

    def download(self, url, filename=""):
        try:
            r = self.session.get(url, stream=True)
        except:
            print("[Network Error] Connection Fail")
            return None

        if r.status_code != 200:
            print("[%d Error] %s" % (r.status_code, r.reason))
            return None

        img = r.raw.read()

        with open(filename, 'wb') as f:
            f.write(img)

        return filename
    def __init__(self, header={}, referer=None):
        # 접속에 필요한 정보 구성
        ses_info = {'referer': referer, 'User-agent': self.user_agent}

        # 추가적인 header 정보가 전달되면 ses_info에 병합한다.
        if header:
            keys = list(header.keys())
            for k in keys:
                ses_info[k] = header[k]

        # 세션객체 생성
        self.session = requests.Session()

        # 세션에 접속 정보 설정
        self.session.headers.update(ses_info)

