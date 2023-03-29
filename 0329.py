#0329
print("안녕하세요.")
print(3)
print(10.6)

var = "안녕"
print(var)
print(type(var))
print(type(3))

var1 = 3
_var = 10

height = 100
weight = 50
radius = 3.14

import keyword
print(keyword.kwlist)
# 변수명에 사용할 수 없는 키워드.
'''
a = 3
b = 10
a += b
print(a)
a <- a*b
print(a)
a *= b
print(a)

a, b = 100, 10
'''

'''
name = input("이름이 뭔가요? ")
print(name,"이군요.")
age = input("나이는요? ")
print("나이의 타입은", type(age))
age = int(age)
print("아버지 나이는", age+30, "이군요.")
'''

'''
형변환
int("30")
float("20.6")
str(30)
등
'''

planet = input("원하는 행성은? ")
strRadius = input(planet + " 반지름은? ")
radius = int(strRadius)

length = 2*3.14*radius
print(planet,'반지름:',radius)
print(planet,'둘레길이:',length)
