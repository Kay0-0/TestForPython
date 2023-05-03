# 0503
# 함수
'''
    함수 이름  - addthree
    기능: 3을 더함!
    input : 숫자 1개
    output : 숫자 1개, input 숫자에 3 더한것을 내보냄.

    def function_name(input1, input2, input3) :
        # 수행문 1
        # 수행문 2
'''


def addthree(num):
    return num+3

print(addthree(100))

def printaddthree(num):
    print(num+3)

printaddthree(100)

# function 작성
# function1 - 사람 이름 2개를 입력 받아서 '안녕 사람1, 안녕 사람2' 출력
def hello(n1, n2) :
    print("안녕 ",n1,", 안녕 ",n2)

hello('민채영', '함경민')

# function2 - 숫자 2개 입력받아 두개의 합을 return
def mysum(n1, n2):
    return n1+n2

print(10, 20)

# function3 - 인자는 몇 개가 들어올지 모르지만, 모든 인자의 합을 return
def mysum2(*numbers):   # 몇 개의 인자가 들어와도 파이썬이 처리해주겠다는 의미. 리스트 같은 거라고 생각해주세용^__^
    # for문 사용하기.
    result = 0
    for num in numbers:
        result += num
    return result

print(mysum2(1,2,3,45,6,7,8,9,19))

lis1=[1,2,3,45,6,7,8,9,19]
print(mysum2(*lis1)) #리스트 함수에 활용하기

# key, value pair
# cafe function
# 메뉴 = 가격
# 출력해주는 function을 만들자

def cafe(**keyvalue):
    for key in keyvalue:    #아메, 라떼, 핫초코
        print(key, keyvalue[key])  # 아메, 2000<식으로 끔

menu={'아메리카노':2000, '카페라떼':3000, '핫초코':5000, '마카롱': 2500}

cafe(아메리카노=2000, 카페라떼=3000, 핫초코=5000)
cafe(아메리카노=2000, 카페라떼=3000)

cafe(**menu)    # 딕셔너리 메뉴에 넣기 

# 람다 함수
# Lambda function
# 짧게 간결하게 쓰고 싶어서 개발된 함수
# 익명함수인가봄?
# 수행문이 한줄.

# addthree 함수를 람다로 작성
# lambda '파라미터' : '수행문'
print((lambda num : num + 3)(100))

# 숫자 입력받아서 x10 리턴
print((lambda num : num*10)(10))

# 숫자 두개 입력받아 곱 리턴
print((lambda num1, num2 : num1*num2)(4,5))


# map, filter

# map: 리스트 각각에 함수 수행
print(*map(addthree, [10, 20, 30, 40, 50]))
print(list(map(addthree, [10, 20, 30, 40, 50])))
# 맵의 개념 이해하는 것 중요!

print(list(map(lambda x: x+3, lis1)))


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# *5+10 결과를 function, lambda을 이용하여 각각 리스트로 출력
def x5p10(n) :
    return n * 5 + 10
print(list(map(x5p10, list1)))
print(list(map(lambda n: n * 5 + 10, list1)))

# 두개의 list에서 하나씩 뽑아, 두 개를 더해 하나의 리스트로 만들기
print(list(map(mysum, list1, list2)))
print(list(map(lambda n1, n2: n1+n2, list1, list2)))


# filter
# filter(function, list)
# false면 빠져나오는 반복문으로 실행?

def positive(x) :
    if x > 0:
        return True
    else:
        return False

print(list(filter(positive, [10, -2, 3, -5, 9])))
print(list(filter(lambda x : x>0, [10, -2, 3, -5, 9])))
