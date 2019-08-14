import requests
import json
from pandas import DataFrame
from matplotlib import pyplot
from print_df import print_df

json_list_url = "http://itpaper.co.kr/demo/python/student.json"

r = requests.get(json_list_url)

if r.status_code != 200:
    print("[%d Error] %s" % (r.status_code, r.reason))
    quit()

r.encoding ="utf-8"
print_df(r.text)

result = json.loads(r.text)
print_df(result)

df=DataFrame(result['student'])
print_df(df)

name_list = list(df['name'])

name_dict={}
for i,v in enumerate(name_list):
    name_dict[i] = v
df.rename(index=name_dict, inplace=True)
df.drop('name', axis=1, inplace=True)
print_df(df)
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 14
pyplot.rcParams["figure.figsize"] = (14,8)

df.plot.bar()
pyplot.grid()
pyplot.title("학생별 시험 점수")
pyplot.legend()
pyplot.ylabel("점수")
pyplot.show()
pyplot.close()
