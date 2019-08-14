#-*-coding: utf-8 -*-
sum = 0

for i in range(1,101):
	if i % 3 == 0 and i % 5 == 0:
			sum += i
tql = "공배수의 총 합 : {0}"
print(tql.format(sum))