import requests
from bs4 import BeautifulSoup
from print_df import print_df
from sample import naver_news_url
from sample import user_agent

session = requests.Session()
session.headers.update({'referer':None, 'User-agent': user_agent})

r = session.get(naver_news_url)

if r.status_code != 200:
 	print("%d 에러가 발생했습니다." % r,status_code)
 	quit()

r.encoding ="euc-kr"

soup = BeautifulSoup(r.text, 'html.parser')

selector = soup.select('#articleBodyContents')

item = selector[0]

for target in item.find_all('script'):
	target.extract()

for target in item.find_all('a'):
	target.extract()

for target in item.find_all('br'):
	target.extract()

for target in item.find_all('span',{'class':'end+photo_org'}):
	target.extract()

result_str = item.text.strip()
print_df(result_str)