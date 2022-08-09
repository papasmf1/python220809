# class1.py
#1)클래스 형식을 정의
class Person:
    #약속된 이름으로 초기화 메서드 정의
    def __init__(self):
        #초기화 루틴 
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스(복사본)을 생성
p1 = Person() 
p2 = Person() 
p1.name = "전우치"
#3)메서드 호출
p1.print()
p2.print() 

