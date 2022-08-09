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
#실행시간에 변수 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
p1.age = 30
print(p1.age)
#print(p2.age)


