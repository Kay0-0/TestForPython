#0412

#자료형 - 리스트, 튜플, 딕셔너리, 집합

# 리스트 ["김밥", "떡볶이", "돈까스"]
# 추가와 삭제가 가능하다.
# 변화하는 자료를 다룰 때 사용

# 튜플 ("김밥", "떡볶이", "돈까스")
# 수정할 수 없음.
# 변하면 안되는 값을 다룰 때 사용

# 딕셔너리 - 사전
# 키 - 값
# {k:v, "사과":"apple"}
# adress = {"홍길동":"구로구", "김길동":"부천", "박길동":"인천"}


# 리스트
# 1. 빈 리스트를 만들어서, 하나씩 원소를 추가하는 방식
lst = []
print(type(lst))
# 리스트 추가 메소드
lst.append("김밥")
lst.append("햄버거")
lst.append("초밥")
lst.append("오코노미야끼")
print(lst)
lst.append("브런치")
print(lst)
# 위치(인덱스)를 선택하여 값 부여
lst.insert(0, "밥버거")
print(lst)
lst.insert(0, "써브웨이")
print(lst)
print("list에서 5번째에 있는 값입니다. → ", lst[4])
# 점심메뉴 출력하기 1
for i in range(len(lst)):
    print(lst[i])
# 점심메뉴 출력하기 2
for item in lst:
    print(item)
print("-----------------------")
# 인자값이 몇 번 들어갔는지 확인하기
print(lst.count("김밥"))
# 몇 번째 값인지(인덱스) 확인하기
print(lst.index("김밥"))
# slicing
# list[start : end : step]
# start부터 end-1까지 step씩 뛰어넘어라
lst[::]
print(lst[:len(lst):1])
print(lst[0:8:2])
# 삭제 → 앞부터 삭제
lst.insert(0, "삭제실습")
lst.append("삭제실습")
print(lst)
lst.remove("삭제실습")
print(lst)
lst.remove("삭제실습")
print(lst)
# lst.remove("삭제실습")
# 오류 → 미존재 값
# 해결은 if문 사용
lst.append("삭제실습")
lst.append("삭제실습")
print(lst)
while 1 :
    if "삭제실습" in lst:
        lst.remove("삭제실습")
    else:
        print("삭제 완료")
        break
print(lst)
# pop → 마지막 인덱스 삭제(기본)
# 파이썬에서는 변형해서 숫자(인덱스)를 지정하여 삭제 가능
print("lst.pop(): ", lst.pop())
print(lst)
print(lst.pop(0))
print(lst)
# pop과 remove의 결과는 같지만, pop은 삭제하는 데이터도 표현이 가능하다.
# 리스트 합치기
# print 안에서는 동작하지 않음 → print(lst.extend(dessert)) (×)
dessert=["케이크", "마카롱", "쿠키", "까눌레", "다쿠아즈", "누네띠네", "마들렌"]
lst.extend(dessert)
print(lst)
# sort vs sorted
fruit = ["orange", "apple", "mango", "kiwi", "banana"]
print(fruit)
print(sorted(fruit))    # 원본이 바뀌지 않음
print(fruit)
fruit.sort()    #원본이 바뀜(print문 내에서 실행 ×)
print(fruit)
# reverse 순서 뒤집기
fruit.reverse()
print(fruit)
# clear 비우기
fruit.clear()
print(fruit)
# del 리스트 삭제하기(변수 삭제)
del fruit
# print(fruit) → 오류(존재하지 않는 변수 not defined)
# 리스트 컴프리핸션
# 리스트를 선언할 때 짧고 빠르고 간결하게 하기 위한 목적으로 만들어짐.
# 0부터 10까지 숫자가 있는 리스트 선언하기
# 1. 그냥 선언하기
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l1)
# 2. for문으로 append
l2 = []
for i in range(11) :    # range의 의미는 0에서 시작해서 10까지
    l2.append(i)
print(l2)
# 3. 리스트 컴프리핸션
l3 = [i for i in range(11)]
print(l3)
# 문제1. 0~10 숫자의 제곱을 리스트에 넣어라
l4 = [i*i for i in range(11)]
print(l4)
# 문제2. 0~10 숫자의 3배수를 리스트에 넣어라
l5 = [i*3 for i in range(11)]
print(l5)
# 문제3. hello를 리스트에 10번 넣어라
l6 = ["hello" for i in range(10)]
print(l6)
# 문제4. 0~10까지 짝수들의 제곱을 리스트에 넣으시오
l7 = [i**2 for i in range(11) if i % 2 == 0]
print(l7)
# list 복사
# 복사 후 원본 리스트의 변화가 복사리스트에도 적용됨
# → shallw copy라고 함. 메모리 주소를 공유.
l8 = l1
l1.pop()
print(l1)
print(l8)
print(l8 is l1)
l8.append(5455)
print(l1)
print(l8)
# 메모리 주소를 공유하지 않는.... deep copy 3가지 방법
l9 = l1[:]  # [:]는 l1의 처음부터 끝까지 라는 의미
# l9 = l1.copy()
# l9 = list(l1)
l1.pop()
print(l1)
print(l9)
print(l1 is l9)
l9.append(45)
print(l1)
print(l8)
print(l9)