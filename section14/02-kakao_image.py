from crawler import Crawler
import urllib
import json
import datetime as dt
import os

auth = {'Authorization': 'KakaoAK 1f84f241e9d1a0f871dc40e7926ac5f1'}

crawler = Crawler(header=auth)

max_page = 5
group_count = 80
keyword = '아이린'

datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")

dirname = "%s_%s" %(keyword.replace(' ', '_'), datetime)

if not os.path.exists(dirname):
    os.mkdir(dirname)
counter = 1

for num in range(0, max_page):
    params = {"page": num +1, 'size': group_count, "query": keyword}

    query = urllib.parse.urlencode(params)

    site_url ="https://dapi.kakao.com/v2/search/image?" + query
    print(site_url)

    result = crawler.get(site_url)

    if(result):
        data = json.loads(result)

        for item in data["documents"]:
            fname = "%s/%04d.gif" % (dirname, counter)
            ok = crawler.download(item["image_url"], filename=fname)

            if ok:
                print(ok + "(이)가 저장되었습니다.")
            else:
                print(" >>> [ERROR] " + item["image_url"] +" 저장에 실패 하였습니다.")

            counter += 1