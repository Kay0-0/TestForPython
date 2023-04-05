# 0405

# 문자열
'''
str = "파이썬수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업"
str2 = "파이썬수업,씨수업,자바수업,이썬수업,파이썬수업"
'''

#format
#3+4=7
'''
print(3, "+", 4, "=", 7)
f= "{} + {} = {}".format(3, 4, 3+4)
print(f)
# 중괄호에 변수를 넣고 싶다는 의미
f2= "{0} + {1} = {2}, {0}, {2}".format(3, 4, 3+4)
print(f2)
# 중괄호에 숫자가 들어가면 인덱스 값을 의미...
f3= "{0} + {1} = {2}, {2:d}, {0:f}".format(3, 4.0, 3+4)
# float는 int로 변경 안됨
# 인덱스 값은 전부 주거나 아예 안주거나...
print(f3)
f4= "{0:10d}, {1:10.3f}, {2:2f}".format(3, 4, 3+4)
print(f4)
'''

#join
'''
#print("**".join(str))
'''

#replace
'''
print(str.replace("파이썬", "자바", 3))
'''

#count
'''
print(str.count("파이썬"))
'''

#split
'''
#print(str.split())
print(str2.split(","))
print(str2.split("업"))
'''

#find, index
'''
str.find("파이썬")
print("find: ", str.find("씨"), "index: ", str.index("씨"))
'''

#bool
'''
print(type(True), type(False))
a="hello"
print(bool("hello"), bool("hi"), bool(3), bool(1), bool(-1))
print(bool(""), bool(0))
str = "100"
print(int(True), int(False), int(str))
'''


#조건문
#if문
'''
if 조건 1:
    실행문 1
elif 조건 2:
    실행문 2
else :
    실행문 3
    '''

#오전/오후
'''
h=9
if h<12 or h>=24 :
    # h가 12보다 작을 때
    print("오전")
elif h<13:
    print("점심")
elif h<18:
    print("오후")
elif h<21:
    print("저녁")
else :
    print("밤")
'''

# 다중if문
'''
tea = input("차 마실래?")
if tea == "헬로비너스" :
    print("그 노래 아시는구나")
    idol = input("무슨 노래가 제일 좋아?")
    if idol == "비너스" :
        print("역시 데뷔곡이 최고지")
    else :
        print("그 노래도 좋지")
        song = input("또 좋아하는 노래 있어?")
        if song=="비너스":
            print("역시 데뷔곡이 최고지")
        else :
            print("비너스는 어때?")
else :
    print("아... 넵")
'''

#for, while
#반복문
#in range
'''
for i in 1, 2, 3, 4, 5, 6:
    print("i: ", i)

for i in range(0, 20, 1):
    print("i: ", i)

for i in range(20):
    print("i: ", i)
'''
'''
while 조건:
    수행문
'''

# 1부터 10까지 합 구하기
'''
sum = 0
for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
    sum+=i
print(sum)
sum=0
for i in range(11):
    sum+=i
else:
    print("else 안의 문구: for문이 잘 종료됨")
print("esle 밖의 문구: for문 종료됨.")
print(sum)
'''
'''
n = 1
sum = 0
while n<=10:
    sum+=n
    n+=1
print(sum)
while True:
    print("무한루프")
while False:
    print("실행되지 않음")
while 0:
    print("실행되지 않음")
'''

#break continue
'''
#단어 입력을 무한 루프로 받는다.
# 그 글자를 3번 써줌
# "exit" -> 루프를 끝내고 종료
# "apple" -> 3번 안쓰고 그냥 다시 단어 입력을 받음.
while 1:
    word = input("단어를 입력하세요: ")
    if word == "exit":
        break
        print("break 뒤의 문장")
    elif word == "apple":
        continue
        print("continue 뒤의 문장")
    else:
        for i in range (3):
            print(word)
    print("apple을 넣으면 이 문장을 절대 볼 수 없음")
print("while문 종료")
'''

# 놀이동산 놀이기구 탑승 문제
# 총 정원 4명
# 정원이 차면, 놀이기구 시작
# 조건 키 150 이상만 탈 수 있음
# 사람들에게 키를 물어보고, 탑승시키시오.
# 150 이상 4명이 되면 놀이기구를 시작
# 수도코드 작성해볼 것

while 1:
    member = 0
    member2 = 0
    service = input("운행을 하겠습니까?(o, x) ")
    if service == "o":
        while member2<4:
            print((str)(member+1)+"번째 손님")
            height = input("키가 150 이상인가요?")
            if height == "o":
                print("탑승하시오.")
                member2+=1
            else :
                print("탑승 불가합니다.")
            member+=1
        print("운행 시작합니다.")
    else:
        "운행 정지합니다."
        break
print("운행 종료")