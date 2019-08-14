import datetime as dt
import requests
import json
import pandas
from pandas import DataFrame
from matplotlib import pyplot
from print_df import print_df

kobis_key = "8c56c13266968c52f489661f44b76b5b"

kobis_api = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=%s&targetDt=%s"

today = dt.datetime.now()
delta = dt.timedelta(days=-1)
yesterday = today + delta
yesterday_str = yesterday.strftime("%Y%m%d")

api_url = kobis_api % (kobis_key, yesterday_str)
print_df(api_url)

r = requests.get(api_url)

if r.status_code != 200:
    print("[$d Error] %s" % (r.status_code, r.reason))
    quit()

r.encoding = "utf-8"
result = json.loads(r.text)
print_df(result)

df = DataFrame(result['boxOfficeResult']['dailyBoxOfficeList'])
print_df(df.head())

df = df.filter(items=['movieNm','audiCnt'])
print_df(df.head())

movie_list = list(df['movieNm'])
index_dict={}

for i, v in enumerate(movie_list):
    index_dict[i] = v
df.rename(index=index_dict, columns={'audiCnt': '관람객수'}, inplace=True)

df.drop('movieNm', axis=1, inplace=True)
print_df(df.head())

print_df(df['관람객수'])

df['관람객수'] = df['관람객수'].apply(pandas.to_numeric)
print_df(df['관람객수'])

df.sort_values('관람객수', inplace=True, ascending=True)
print_df(df)

df = df.dropna()
empty_sum = df.isnull().sum()
print_df(empty_sum)