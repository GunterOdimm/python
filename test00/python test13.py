#-*-coding: utf-8 -*-

times = [7,5,5,5,5,10,7]
total = 0

size = len(times)
half=(size//2) + 1

for i in range(0, half):
	p = size -i
	print(p)
	total += p * 5200

print(total)

for i in range(half,7):
	p = half + i
	total += p * 5200


tpl = "일주일간의 총 급여는 {0}원입니다."
print(tpl.format(total))