# 0607

# dictionary 복습
# key - value
# dict = {key1: value1, key2: value2, ...}
# 자동차 등록번호: (생산년도, 배기량)
carDict = {'h101':('2020','1600'), 'h102':('2021','1600'),
           'b101':('2020','3600'), 'b102':('2021','5200')}
# print(carDict.keys())
# print(carDict.values())
# print(carDict.items())

# h101 ('2020', '1600') 과 같은 형태로 출력하는 방법
# for i, j in carDict.items():
#     print(i, j)
# for i in carDict.items():
#     print(i[0]. i[1])
# for k in carDict.keys():
#     print(k, carDict[k])
'''
carYear = []
for v in carDict.values():
    carYear.append(int(v[0]))
print(*carYear, sep='\n')

year = int(input("생산연도를 입력하세요: "))
print(year, "년도에 생산된 자동차는 ", carYear.count(year), "대 입니다.", sep='')
'''

# 다음 코드의 올바른 결과값을 쓰시오.
'''
members = {'홍':'111','박':'222','정':'333'}
members['최'] = '555'
members.update({'강':'666'})
members['김']='777'
members.update({'최':'888'})
print(members)
'''

# zip
# list, tuple, 문자열 등 여러개를 순서대로 묶어주는 것.
# l1 = [1, 2, 3, 4, 5]
# l2 = ['a', 'b', 'c', 'd', 'e']
# print(list(zip(l1, l2)))

# zip을 묶고, input 받아서 종목 이름 입력받기.
# 선수 수 출력하기
# for문 사용
# quit를 만나면 종료할 것.
# 다른 종목이 들어오면 "몰라요" 출력, 다시 입력받기.
# continue, break를 활용할 것.
'''
sport = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]

sports = dict(zip(sport, num))

while 1:
    s = input("종목을 입력하세요: ")
    if s == 'quit':
        print("quit 입력, 종료.")
        break
    if s in sports.keys():
        print(s, "의 선수 수는 ", sports[s], "명")
    else :
        print("몰라요")
'''


# map
# map(함수, input 리스트) => 리스트
# map(addone, [1, 2, 3])
# => [addone(1), addone(2), addone(3)]

# filter
# filter(posiNum, [-1, 2, 3])
# => [2, 3]

# lambda
# lambda 입력값 : 리턴결과

# filter와 lambda를 사용하여
# 아래 리스트에서 음수를 모두 제거해보자
'''
l1 = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x: x>0, l1)))
'''

# 리스트 두 개를 받아 각각 같은 순서끼리 더하는 함수를 만들어라.
# map과 lambda 사용
# 결과: [11, 22, 33, 44, 55]
'''
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
# print(list(map(lambda x:x[0]+x[1], list(zip(l1, l2)))))
print(list(map(lambda x, y: x+y, l1, l2)))
'''


# 9단원
# import 파일
# __name__ = __main__ run
import n2

n2.hello2py()
print("==========")
print("현재 파일의 __name__입니다. ", __name__)
print("==========")

# 코딩 하는 문제가 나올 것이니 코딩을 해보세용~
# 문제는 최대한 조금 내려고 노력...인데 장담은 못해용
# 진수는 안낼게요(277쪽)