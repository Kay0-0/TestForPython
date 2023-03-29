#0329
'''
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

'''
planet = input("원하는 행성은? ")
strRadius = input(planet + " 반지름은? ")
radius = int(strRadius)

length = 2*3.14*radius
print(planet,'반지름:',radius)
print(planet,'둘레길이:',length)
'''

'''
a = "Python"
print(a[0], "  ", a[1], "...", a[5])
print("python"[0], "... ", "python"[1], "... ", "python"[5])
print("동양미래대학교"[0])
print(len(a))

sch="동양미래대학교 컴퓨터소프트웨어공학과"
print(sch[:])
print(sch[:3])
print(sch[3:])
print(sch[2:4])
print(sch[-4:-1])
print(sch[0:3:2])
print(sch[0:len(sch):2])

print(sch[8::2])
print(sch[8:])
print(sch[:-3:4])
print(sch[5:0:-1])

print("Hello\nWorld...!")
print("Hello\bWorld...!")
print("Hello\tWorld...!")
print("Hello\vWorld...!")
'''

'''
function 내장함수
method
'''

'''
str_a = "하하하"
print(type(str_a))
str_a.replace("하", "호")
print(str_a.replace("하", "호"))
print(str_a.replace("하", "호", 1))

str_c = "안녕하세요. 파이썬 수업입니다. 파이썬. 파이썬. 파이썬. 파이썬. 파이썬. 파이썬. 파이썬. 파이썬. 파이썬."
print(str_c.replace("파이썬", "자바", 5))
'''

# 6자리 실수를 입력받는다(ex. 222.788)
# 출력: 실수의 각 자리의 합을 출력한다. 2+2+2+7+8+8 => ??
# input(), int(), str.replace()

num = input("6자리 실수를 입력하시오")
num = num.replace(".","")
sum = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]) + int(num[5])
print(sum)