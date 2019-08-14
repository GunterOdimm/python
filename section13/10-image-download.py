import os
import requests
from print_df import print_df
from sample import image_url
from sample import user_agent

session = requests.Session()
session.headers.update({'referer':None,'User-agent':user_agent})

r=session.get(image_url,stream=True)

if r.status_code != 200:
    print("%d 에러가 발생했습니다. " % r.status_code)
    quit()
fname = os.path.basename(image_url)
print_df(fname)

p=fname.rfind(".")

if p < 0:
    fname += ".jpg"
print_df(fname)

img = r.raw.read()

with open(fname, 'wb') as f:
    f.write(img)