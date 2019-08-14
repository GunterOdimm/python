def print_point(x):
	point = list(x.values())
	point.sort()

	tpl = "국어 : {0}"
	print(tpl.format(point[2]))

	tpl = "영어 : {0}"
	print(tpl.format(point[1]))

	tpl = "수학 : {0}"
	print(tpl.format(point[0]))

	print("-" * 10)
	avg = sum(x.values()) / len(x)
	tpl = "평균 : {0}"
	print(tpl.format(avg))

my_point = {"kor": 98, "eng": 82, "math": 75}
print_point(my_point)