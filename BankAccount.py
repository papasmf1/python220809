# BankAccount.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #이름규칙(이름을 숨겨달라~)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        #입금 
        self.__balance += amount 
    def withdraw(self, amount):
        #출금 
        self.__balance -= amount
    def __str__(self):
        #인스턴스 문자열 출력
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#외부에서 접근: _클래스명__변수명
#혹시 개발자가 접근해야 하면(백도어)
print(account1._BankAccount__balance)
print(account1._BankAccount__name)
print(account1)
