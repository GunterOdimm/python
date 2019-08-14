from print_df import print_df
from pandas import ExcelFile
from pandas import DataFrame
from matplotlib import pyplot
import datetime as dt

#데이터 수집
xls_file = ExcelFile("data/children_house.xlsx")

sheet_names = xls_file.sheet_names
print_df(sheet_names)

df = xls_file.parse(sheet_names[0])
print_df(df)

#데이터 전처리
city_list = list(df['지역'])
print_df(city_list)

index_dict = {}
for i, v in enumerate(city_list):
    index_dict[i] =v

print_df(index_dict)

df.drop('지역', axis=1, inplace=True)
df.rename(index=index_dict, inplace=True)

#전국에 대한 데이터는 필요 없으므로 삭제한다.
df.drop( '전국(계)', inplace=True)

print_df(df)