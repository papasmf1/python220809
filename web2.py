# web2.py 
#웹서버에 요청
import urllib.request
from bs4 import BeautifulSoup
#웹서버에 요청해서 실행결과 받기(문자열)
data = urllib.request.urlopen(
    "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")
cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format( len(cartoons) ))
title = cartoons[0].find("a").text 
print(title)
link = cartoons[0].find("a")["href"]
print(link)
#ctrl + /:다중라인 주석
# <td class="title">
# 		<a href="/webtoon/detail?titleId=20853">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>