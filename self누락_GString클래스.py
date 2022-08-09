#전역변수(이름 충돌)
str = "Not Class Member"
#클래스정의 
class GString:
    def __init__(self):
        #인스턴스 멤버 변수 초기화 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)

#인스턴스생성 
g = GString()
g.set("First Message")
g.print()
