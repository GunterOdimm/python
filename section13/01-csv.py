from print_df import print_df
from pandas import read_csv
from pandas import DataFrame
from sklearn.impute import SimpleImputer
import numpy
import datetime as dt
from matplotlib import pyplot

# 데이터 수집
df = read_csv("data/grade.csv",encoding="euc-kr")

print(df.shape)

print_df(df.head(5))

#데이터 전처리

student_list = list(df['이름'])

index_dict={}
for i, v in enumerate(student_list):
    index_dict[i] = v


df.drop('이름', axis=1, inplace=True)
df.rename(index=index_dict, inplace=True)
print_df(df.head(5))

#데이터 정제
#열별로 결측치(빈칸)의 수를 파악
print_df(df.isnull().sum())

#결측치를 정제할 규칙 정의 nan값을 평균으로 대체
imr = SimpleImputer(missing_values=numpy.nan, strategy="mean")

df_imr = imr.fit_transform(df.values)

df = DataFrame(df_imr,index=list(df.index), columns=list(df.columns))

print_df(df.isnull().sum())

#평균 점수에 대한 열 추가하기
df['평균'] = df.mean(axis=1)

conditions= [ (df['평균']>= 90),
             (df['평균']>= 80),
             (df['평균']>= 70),
             (df['평균']< 70),]

grade=['A','B','C','F']

df['학점'] = numpy.select(conditions, grade)
print_df(df.head(5))

#생성결과를 csv로 저장하기
NT = dt.datetime.now().strftime("%y%m%d_%H%M%S")
filename="grade"+NT+".csv"

df.to_csv(filename, encoding='euc-kr', na_rep='NaN', index_label='이름', header=['국','영','수','과','평균','학점'])

#데이터 시각화
cnt = df['학점'].value_counts()
result_df = DataFrame(cnt)
print_df(result_df)

#생성된 데이터 프레임의 컬럼이름 수정
result_df.rename(columns={'학점': '학생수'},inplace=True)
print_df(result_df)

pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 14
pyplot.rcParams["figure.figsize"] = (12,8)

result_df.plot.bar()
pyplot.grid()
pyplot.legend()
pyplot.title("학점 분포도")
pyplot.xlabel('학점')

pyplot.show()
pyplot.close()