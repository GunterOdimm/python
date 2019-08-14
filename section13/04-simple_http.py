import requests

simple_text_url = "http://itpaper.co.kr/demo/python/simple_text.txt"

r = requests.get(simple_text_url)

if r.status_code != 200:
    print("[$d Error] %s" % (r.status_code, r.reason))
    quit()

r.encoding = "utf-8"

print(r.text)