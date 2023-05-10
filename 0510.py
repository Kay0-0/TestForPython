# 0510

# 랜덤함수
import random
print(random.randint(1, 100)) #1부터 100까지 숫자 중 하나 리턴.

import math
# import math as m
# m.fsum 으로 사용 가능
print(int(math.fsum([1,1,1,1,1])))
math.pow(10, 3) # 10**3
# from math import pow
# math. 의 선언 없이 pow함수 사용 가능
# -> pow(10, 3)
# from math import pow as p
# 처럼 응용 가능
# from math import pow, fsum
# 처럼 여러개 동시에 가져오기 가능 (뒤에 as p, f를 붙여 줄이는 것은 불가넝...)

# 내가 모듈 만들기
# 같은 디렉토리에 파이썬 파일 생성(myModul0510.py)
# 같은 레벨(디렉토리)에 만들어야 임포트가 쉽다(다른 디렉토리에 생성해도 임포트는 가능).
import myModul0510 as my    # 임포트와 동시에 모든 어쩌고 실행
my.imNear()
print("__name in myModul0510.py : ", __name__)

# 임포트는 python 파일만 가능.
# 디렉토리는 from으로 호출
from moduleYA.ai import ya as selected
selected.helloYA()

# 터미널에서 입력: pip istall numpy
# ctrl+shift+P
# select python interpreter