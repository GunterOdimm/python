import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
from print_df import print_df
from sample import user_agent

session = requests.Session()
session.headers.update({'referer':None, 'User-agent':user_agent})

r = session.get("https://www.naver.com")

if r.status_code != 200:
    print("%d 에러가 발생했습니다." % r.status_code)
    quit()

r.encoding = "utf-8"
soup = BeautifulSoup(r.text, 'html.parser')

selector = soup.select(".ah_roll_area > .ah_l > .ah_item > .ah_a > .ah_k")

rank_list = []
keyword_list = []

for i, item in enumerate(selector):
    rank_list.append("%02d위" % (i+1))
    keyword_list.append(item.text.strip())

df = DataFrame(keyword_list, index=rank_list, columns=['검색어'])
print_df(df)