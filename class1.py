# class1.py
#1)클래스 형식을 정의
class Person:
    #약속된 이름으로 초기화 메서드 정의
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스(복사본)을 생성
p1 = Person()
#3)메서드 호출
p1.print()

