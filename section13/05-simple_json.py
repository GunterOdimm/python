import requests
import json
from print_df import print_df

simple_json_url ="http://itpaper.co.kr/demo/python/phone.json"

r = requests.get(simple_json_url)

if r.status_code != 200:
    print("[$d Error] %s" % (r.status_code, r.reason))
    quit()

r.encoding = "utf-8"
print_df(r.text)

result = json.loads(r.text)
print_df(result)

print("결과코드: %s" % result['rt'])
print("결과메시지: %s" % result['rtmsg'])
print("제품병: %s" % result['item']['name'])
print("제조사: %s" % result['item']['type'])
print("사진: %s" % result['item']['img'])
print("정가: %s" % result['item']['price']['fixed'])
print("판매가: %s" % result['item']['price']['sale'])