# web2.py 
#웹서버에 요청
import urllib.request
from bs4 import BeautifulSoup

#파일에 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for i in range(1,6):
    #웹서버에 요청해서 실행결과 받기(문자열)
    url = \
    "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    #검색이 용이한 객체
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text.strip()
        print(title)
        f.write(title + "\n")

f.close() 