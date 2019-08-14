#-*- coding:utf-8 -*-
a= 123
b= -456
print(a)
print(b)

#한번 할당된 변수는 다른 값으로 변경이 가능하다
a = 10000
print(a)

c=1.2
d=-3.45
print(c)
print(d)

e=4.24e10 # 4.24 * (10의 10제곱)
f=4.24e-10

print(e)
print(f)

g=0o177 #8진수 표현법입니다.
print(g)

h=0xABC
print(h)

#복소수(알파벡 j사용)
i=1+2j
print(i)

#복소수의 실수 부분 조회
print(i.real)

#복소수의 허수수분 조희
print(i.imag)

#복소수의 켤레복소수
print(i.conjugate())

#복소수의 절대값.
print( abs(a))