from crawler import Crawler
from print_df import print_df
from pandas import DataFrame
import pandas as pd
import urllib

df = DataFrame()
keyword ='노트북'
params = {"query": keyword, "frm": "NVSHATC"}
query = urllib.parse.urlencode(params)

site_url = "https://search.shopping.naver.com/search/all.nhn?" + query
print_df(site_url)

crawler = Crawler()
html = crawler.select(site_url, selector=".info")

for item in html:
    info ={}

    title_list = item.select('.tit')
    title = title_list[0].text.strip()
    info['제품명'] = title

    price_list = item.select('.num')
    price = price_list[0].text.strip()
    price = price.replace(",","")
    price = int(price)
    info['가격'] = price

    spec_list = item.select('.detail a')

    for v in spec_list:
        v = v.text.strip()
        tmp = v.split(":")

        if len(tmp) ==2:
            key = tmp[0].strip()
            value = tmp[1].strip()
            info[key] = value

item_df = DataFrame([info], columns=info.keys())

df = pd.concat([df,item_df], sort=False)

print_df(df.head())

df.to_csv("노트북.csv", index=False)