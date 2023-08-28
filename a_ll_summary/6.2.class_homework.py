#숙제
# Account - (AtmAccount, BankAccount, CreditAccount)
# Atm = 현금 입출금 -> 5만원권, 1만원권, 5천원, 1천원
# Bank = 예금 이자 (최저 금액 이상 이자)
# Credit = 결제 (한도 초과)

class Account:
    def __init__(self, name, account, balance = 0):
        self._name = name
        self._account = account
        self._balance = balance

    def getBalance(self):
        return self._balance

    def setBalance(self, balance):
        self._balance = balance

class AtmAccount(Account):
    def __init__(self, name, account, balance=0, cash=0):
        super().__init__(name, account, balance)
        self._cash = cash

    def deposit(self, cash):
        self._cash += cash
        self.setBalance(self.getBalance() + cash)

    def withdraw(self, cash):
        if self.getBalance() < cash:
            print("잔액이 부족합니다. 출금할 수 없습니다.")
        else :
            check = input("1. 5만원권을 최대로, 2. 선택, 3. 1만원을 최대로")

            if check == 1:
                c5 = cash // 50000
                cash -= c5*50000
                print(f"출금을 완료되었습니다. 5만원권 {c5}장 과 만원권 {cash//10000}장을 받아가세요.")

            elif check == 2:
                c1 = input("5만원권의 장수와 1만원권의 장수를 순서대로 입력해주세요.") # 5 10
                c = c1.split(' ')
                print(f"출금을 완료되었습니다. 5만원권 {c[0]}장 과 만원권 {c[1]}장을 받아가세요.")

            elif check == 3:
                m = cash // 10000
                print(f"출금을 완료되었습니다. 만원권 {m}장을 받아가세요.")

    class BankAccount(Account):
        def __init__(self, name, account, balance=0):
            super().__init__(name, account, balance)

        def interest(self):
            return super()._balance * 0.05 / 12

    class creditAccount(Account):
        def __init__(self, name, account, balance=0, pay=0, limit=10000000):
            super().__init__(name, account, balance)
            self._pay = pay
            self._limit = limit

        def payment(self, pay):
            if self._limit < self._pay + pay:
                print("결제할 수 없습니다. 한도초과입니다.")

            else :
                self._pay += pay
                print("결제가 완료되었습니다. {}원이 결제되었습니다.".format(pay))
#############################################
from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def cook(self):
        pass

class Pizza(Food):
    def __init__(self, name, price, crust, *topping): #"올리브,페페로니"
        super().__init__(name, price)
        self._topping = []
        for i in topping:
            if isinstance(i, str): #if type(i) == str:
                addtopping = i.split(',')
                for j in addtopping:
                    self._topping.append(j)
            elif isinstance(i, list): #elif type(i) == list:
                for j in i:
                    self._topping.append(j)

        self._crust = crust

    def cook(self):
        str = ""
        for i in self._topping:
            str += i
        print(
            "{}에서 피자가 나왔습니다. 토핑은 {}이고, 크러스트는 {}입니다. 가격은 {}입니다.".format(self.name, ','.join(self._topping), self._crust, self.price))

    def addTopping(self, *topping):
        for i in topping:
            if type(i) == str:
                addtopping = i.split(',')
                for j in addtopping:
                    self._topping.append(j)
            elif type(i) == list:
                for j in i:
                    self._topping.append(j)


p = Pizza("도미노", 100, "치즈", ["페페로니", "올리브"]) #리스트 전달
p.addTopping("포테이토") # 한개 추가

p.cook()

# 숙제 - topping, addTopping() -> 리스트, 값 여러개, 값 하나
p = Pizza("도미노", 100, "치즈", ["페페로니", "올리브"])
p.cook()
p = Pizza("도미노", 100, "치즈", "페페로니", "올리브", )
p.cook()
p = Pizza("도미노", 100, "치즈", "페페로니")
p.cook()                