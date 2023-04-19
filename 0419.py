# 0419
'''
# 튜플
t1 = (1, 2, 3, 4, 5)
# 리스트는
l1 = [1, 2, 3, 4, 5]
# 튜플은 수정할 수 없다.
print(l1)
print(t1)
# 출력해보면 생긴건 똑같음(괄호가 다르다)

# 튜플은 (리스트에 비하면) 메서드가 별로 없음...!
print(t1.count(1))  # 특정 인자가 몇 번 나오나요
print(t1.index(5))  # 특정 인자가 몇 번째 인덱스에 나오나요(최초 1회?)

# 튜플은 수정하지 않는 데이터, 거의 변하지 않는 데이터에 사용.
# 예시
# 커피숍 프로그램
menu = ("아메", "라떼", "유자차")
print(menu)
# 아이스티 추가(수정하는 방법)
# 리스트로 바꾸기
menu = list(menu)
menu.append("아이스티")
print(menu)
# 수정 완료 후 다시 튜플로 바꾸기
menu = tuple(menu)
print(menu)

# 튜플 선언
# 위 t1 처럼 선언하기 또는 선언된 리스트를 튜플로 바꾸기.
# 다른 방법 : 빈 튜플을 선언하기(할 수는 있지만 수정이 불가하기 때문에 이상하다!ㅋㅋ)
# tuple = (1, 2, 3, 4, 5)
# tuple = ()
# tuple = 10, 20, 30, 40, 50
# tuple = 10,
# ,를 붙이면 튜플이 된다.

# sort 하는 법
# 리스트는 list.sort()
# 튜플은 sorted(tuple)
print(sorted(menu)) # 튜플 자체가 수정 X

# for in 반복문에서
for i in 1, 2, 3, 4, 5:
    print(i)
# in 다음 1, 2, 3, 4, 5 는 튜플 선언 방식과 같다(튜플을 사용함)


# 딕셔너리
# 말 그대로 프로그램 안에서 '사전' 형태로 저장된 데이터
# 키와 값(Value)이 여러개가 있다.
d1 = { "k1":"v1", "k2":"v2" }
# 키는 중복 값을 허용하지 않는다.
# 값(Value)는 중복 가능.

# 딕셔너리에 값 추가하기
# 1. 선언하기
stu = {}
print(stu)
stu[101] = '최'     # 101이 키, '최'가 값
stu[102] = '함'
stu[103] = '이'
stu[104] = '민'
print(stu)
print(stu[104])
# 키와 값의 페어로 이루어져 있기 때문에 인덱스값이 중요하지 않음
# 인덱스처럼 stu[0]으로 검색하면 keyerror가 된다. (존재하지 않는 키)
# -> 키 값으로 자료 식별
stu['수석'] = '우'
stu['귀요미'] = '박'
stu['귀욤이'] = ['홍', '주', '이']
stu['여신'] = '김'
print(stu)
stu['학점'] = 'A+'
print(stu['학점'])
stu['학점'] = 'A'
print(stu['학점'])
stu.update({'학점' : 'A+'})     # 업데이트는 딕셔너리 형태로
print(stu['학점'])

# 
month = {1 : '1월', 2 : '2월', 3 : '3월', 4 : '4월', 5 : '5월', 6 : '6월', 7 : '7월', 8 : '8월', 9 : '9월', 10 : '10월', 11 : '11월', 12 : '12월'}

# for i in range(1, 13):
#     print(month[i])
# for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 :
#     print(month[i])
for i in month:
    print(i)    # i에는 키값이 들어감.
print(month.keys())
print(month.values())
print(month.items())

# .keys() 메서드 사용 반복문
month = {'a' : '1월', 'b' : '2월', 'c' : '3월', 'd' : '4월', 'e' : '5월', 'f' : '6월', 'g' : '7월', 'h' : '8월', 'i' : '9월', 'j' : '10월', 'k' : '11월', 'l' : '12월'}
for k in month.keys() : # month[key] = value
    print(month[k])
for v in month.values() : # month[key] = value
    print(v)
for i in month.items() : # month[key] = value
    print(i[0])
    print(i[1])

# print(month.get('k1'))
# print(month.get('key100'))
# print(month('k1'))
# print(month('key100'))
# get에서 해당 값이 존재하지 않을 경우 none 결과를 출력하지만, month 형태에서는 오류 메시지를 출력한다.

# dictionary 삭제
print(month.pop('a'))   # key값을 줘야함
print(month)    # 삭제된 데이터는 제외되고 출력
print(month.popitem())  # 마지막 데이터를 삭제
print(month)


# zip(), enumerate()
# 여러개의 리스트를 묶는 것
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']
l3 = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ']

z = zip(l1, l2, l3)
print(type(z))
print(list(z))  # zip을 보기 위해 타입 변경 필요함(리스트 or 튜플)

# 리스트 1개가 딕셔너리가 될 수는 없지만
# 리스트 두개를 zip으로 묶은 뒤 딕셔너리로 바꾸는 것은 가능하다.
d1 = dict(zip(l1, l2))
print(d1)

# 세 개 이상의 리스트를 한번에 딕셔너리로 바꿀 수는 없다.
d2 = dict(zip(l1, zip(l2, l3)))
print(d2)
'''

# 과목을 주면 강의실을 알려주는 시스템
# dictionary로 변환해서 활용
# 무한루프로 강의실을 알려줘라
# quit 라는 단어가 들어오면, 강의실을 알려주는 시스템을 종료해라
# 다른 과목을 물어보면, "몰라요". 다시 과목명 물어보는 것으로 돌아간다.
# 해당 과목에 대한 강의실을 알려준다.
# continue와 break 활용할것.
sub = ['파이썬', '자바', 'C', 'IOT', '웹프론트엔드', 'DB']
room = [101, 102, 103, 104, 105, 106]
study = dict(zip(sub, room))
while 1 :
    c = 0
    sch = input("과목명을 입력하세요 >> ")
    if sch == 'quit' :
        break
    for i in study :
        if i == sch :
            print("강의실은 "+str(study[i])+"호실") # int와 str을 더할 수 없으므로 str형으로 변환하여 사용.
            c+=1
            break
    if c == 0 :
        print("몰라요")
    
# 교수님이 한 것
while 1:
    sch = input("과목명을 입력하세요 >> ")
    if sch == 'quit' :
        print("종료")
        break
    if c in study.keys() :
        print("강의실은 "+str(study[i])+"호실")
    else :
        print("몰라요")