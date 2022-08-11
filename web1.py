# web1.py
#웹크롤링(데이터 수집)
from bs4 import BeautifulSoup

page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
print( soup.prettify() )

