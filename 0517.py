# 0517

# 뷰티풀숲?이란걸 사용할것임
# 새로운 라이브러리이기 때문에 인스톨을 해야함
# pip install beautifulsoup4
# 오류 날 경우 -> python.exe -m pip install --upgrade pip
# 시도 후 다시 해보기
from bs4 import BeautifulSoup
# 오른쪽 아래 있는 3. 11. 3 누르고
# (현재 편집중인 폴더 선택)
# 파이썬 버전 중 'base' 선택 bs4에 밑줄이 사라지는지 확인
import requests

headers = {
    "User-Agent" : "DongYang Mirae Univ"  # 유저 에이전트는 이 곳에서 보내는 겁니다. 라는 표시
}
# 데이터 크롤링 환경 구축
# 1. Chrome 설치(이미 있음)
# 2. pip install selenium 파이썬 셀레니움 설치
#    pip install selenium webdriver_manager 웹드라이브매니저 설치
# 3. 임포트하기
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# 파이썬 코드로 크롬 동작 준비 완료,,

# 뉴스 가져오기
'''
# 주소를 .get 메소드를 이용하여. . . 우 . . . .
# 젤다 기사(드랍ㅠㅠ) http://www.consumernews.co.kr/news/articleView.html?idxno=678588
# 스키즈 기사 https://sports.donga.com/article/all/20230428/119064911/1
webpage = requests.get("https://news.mt.co.kr/mtview.php?no=2023051711193596588", headers=headers)
print(webpage)
print(webpage.content)  # 웹페이지의 컨텐츠를 표시
soup = BeautifulSoup(webpage.content, "html.parser")
# print(soup)

news = soup.select_one("#articletxt").get_text.strip()  #나는 왜 이게 안대까
print(news)
'''

# 네이버 열어 기사 제목 가져오기
'''
driver.get("https://www.naver.com/")    # 인터넷 주소
# 크롬이 url에 접속
time.sleep(3)	# 5초 동안 멈추라는 명령어 -> time(기본 설치 모듈) 임포트
# 위 time에 준 시간 이후 종료됨
# 시간 종료 전에 버튼을 누르는 명령을 한다.
# 클릭 할 컨텐츠 우클릭 -> 검사 -> 개발자 도구(html)에서 표시된 항목 우클릭 -> Copy -> Full XPath
# 뉴스 메뉴 클릭
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)
# 뉴스에서 랭킹 메뉴 클릭
driver.find_element(By.XPATH, "/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[8]/a/span").click()
time.sleep(3)
# 랭킹 기사 클릭
driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div/div[1]/ul/li[1]/div/a").click()
time.sleep(3)
# 기사 제목 받아오기
newstitle = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/h2/span").text
print(newstitle)
# .click() 을 .text로 변경하여 출력 가능
time.sleep(10)
'''

# 아파트 가격 알아보기
'''
driver.get("https://m.land.naver.com/search")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(1)
# 전세값 가져오기
rentprice = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text
print("전세: ",rentprice)
time.sleep(5)
# 매매값 가져오기
rentprice = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]/dd").text
print("매매: ",rentprice)
time.sleep(5)
'''

# 주식 가져오기 : for문 이용
driver.get("https://finance.naver.com/")
sub1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a").text
sub2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a").text
sub3 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a").text

print(sub1, sub2, sub3, sep="\n")

# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a
# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a
# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a

lst = []
for i in range(10) :
    sub = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text   # f를 왜 써?
    lst.append(sub)
lst1 = []
for i in range(10) :
    sub = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[1]").text
    lst1.append(sub)
lst2 = []
for i in range(10) :
    sub = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[2]").text
    lst2.append(sub)
lst3 = []
for i in range(10) :
    sub = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[3]").text
    lst3.append(sub)

a = list(zip(sub, sub1, sub2, sub3))
print(a)
