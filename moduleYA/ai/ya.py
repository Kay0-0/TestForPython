# myModul0510.py

def helloYA() :
    print("Hello-? Hello? I'm NEAR: Who are you?")

# __name__ : 현재 파일에선 __main__, 다른 파일에선 파일명(myModul0510)으로 작동하는 변수
if __name__ == "__main__" :
    print("오늘은 5월 10일 입니다.")
    helloYA()
    print("축제가 곧이네요~")
    print("__name in myModul0510.py : ", __name__)