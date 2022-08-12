# Form1.py
# Form1.ui(화면단) + Form1.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

form_class = uic.loadUiType("Form1.ui")[0]

#화면 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.label.setText("첫번째 Qt화면")

#직접 모듈을 수행한 경우만 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_() 
