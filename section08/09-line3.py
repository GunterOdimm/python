from matplotlib import pyplot
import numpy

from sample import seoul
from sample import busan
from sample import daegu
from sample import inchun
from sample import label

pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 12

pyplot.figure()

pyplot.grid()

pyplot.title("2017년 주요도시 교통사고")
pyplot.xlabel("월")
pyplot.ylabel("교통사고")

pyplot.plot(seoul, label="서울")
pyplot.plot(busan, label="부산")
pyplot.plot(daegu, label="대구")
pyplot.plot(inchun, label="인천")
pyplot.savefig('traffic1.png',dip=200)

pyplot.xlim(0,11)
pyplot.ylim(0,4000)

pyplot.legend(title='도시',loc="center left", shadow=True)

pyplot.savefig('traffic2.png',dpi=200)

x = list(range(0,len(label)))

pyplot.xticks(x,label)

pyplot.savefig('traffic3.png', dpi=200)

pyplot.close()
