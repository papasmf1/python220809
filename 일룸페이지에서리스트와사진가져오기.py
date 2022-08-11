# python 3.5 설치(설치본 있음) 
# pip install bs4  뷰티플스프 설치 
# pyQt 5.6 설치(설치본 있음)
import sys
from PyQt5.QtWidgets import *
import urllib.request
from bs4 import BeautifulSoup
import webbrowser   #브라우저로 넘기는 경우 
import re 

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #창의 시작위치와 폭, 높이(x,y,width,height) 
        self.setGeometry(200, 200, 800, 800)
        
        #입력 텍스트 
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(20, 20)
        self.lineEdit.setText("13")  #기본 값 셋팅 

        #버튼
        self.btn = QPushButton("검색", self)
        self.btn.move(120, 20)
        self.btn.clicked.connect(self.setTableWidgetData)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(20, 70)
        self.tableWidget.resize(600, 400)
        self.tableWidget.setRowCount(50)  #행의 갯수 
        self.tableWidget.setColumnCount(1)  #컬럼의 갯수 
        #컬럼의 폭을 지정한다. 0번 1번 
        self.tableWidget.setColumnWidth(0, 400)


    def setTableWidgetData(self):
        #User-Agent를 조작하는 경우 
        hdr = {'User-agent':'Mozila/5.0 (compatible; MSIE 5.5; Windows NT)'}
        #기본 주소
        base_url = "https://www.iloom.com/"
        row = 0
        #전체카테코리가 13번, 쇼파가 8 
        for n in range(1,4):
             data ='https://www.iloom.com/product/item.do?&cn=0&sortGb=hits&' \
                 'categoryNo=' + str(self.lineEdit.text()) + '&topParent=13&depth=1&pageNo=' + str(n)
        req = urllib.request.Request(data, \
                                          headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('p', attrs={'class':'text'})
        #파일로 저장 
        f = open("ilroom.txt", "a+", encoding="utf-8")
        #반복하면서 태그의 문자열 가져오기 
        for item in list:
               item1 = item.contents[1]
               title1 = item1.text 
               item2 = item.contents[3]
               title2 = item2.text 
               mergeTitle = title1 + title2 
               print(mergeTitle)
               #행데이터로 출력 
               self.tableWidget.setItem(row, 0, QTableWidgetItem(mergeTitle))
               f.write(mergeTitle + "\n")
               row += 1
        #image가져오기 
        listImage = soup.find_all('p', attrs={'class':'image'})
        for item in listImage:
                #<img>태그 찾기 
                img = item.find('img')
                #소스 속성 가져오기 
                img_src = img.get('src')
                img_url = base_url + img_src
                #이미지에서 /를 없애고 
                img_name = img_src.replace('/', '')
                #이미지 저장하기 
                urllib.request.urlretrieve(img_url, 
                        './img/' + img_name)

 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Form()
    mywindow.show()
    app.exec_()






