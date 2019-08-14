# -*- coding: utf-8 -*-
myheight = 177.9
myweigth = 83.7
standard_weight = 0
obesity =0


if myheight <= 150:
	standard_weight = myheight - 110
else:
	if myheight > 150:
		standard_weight = (myheight - 110) * 0.9

obesity = ((myweigth - standard_weight) / standard_weight) * 100

print(obesity)

if obesity <20:
	print(" - 정상입니다(안심)")
else:
	if obesity >20 :
		print(" - 경도비만입니다(안심)")
	elif obesity <30:
		print(" - 경도비만입니다(안심)")
	else:
		if obesity >30:
			print(" - 중등도 비만입니다(위험)")
		elif obesity <50:
			print(" - 중등도 비만입니다(위험)")
		else:
			print(" - 고도비만 입니다(매우위험)")
# if obesity <20:
# 	print("당신의 비만도는 "+ obesity + " - 정상입니다(안심)")
# else:
# 	if obesity >20 :
# 		print("당신의 비만도는 " + obesity + " - 경도비만입니다(안심)")
# 	elif obesity <30:
# 		print("당신의 비만도는 "+ obesity + " - 경도비만입니다(안심)")
# 	else:
# 		if obesity >30:
# 			print("당신의 비만도는 "+ obesity + " - 중등도 비만입니다(위험)")
# 		elif obesity <50:
# 			print("당신의 비만도는 "+ obesity + " - 중등도 비만입니다(위험)")
# 		else:
# 			if obesity > 50:
# 				print("당신의 비만도는 "+ obesity + " - 고도비만 입니다(매우위험)")
