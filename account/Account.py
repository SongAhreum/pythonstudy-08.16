
import random

class Account:
  # 입출금 정기예금 자유적금 세이프박스 모임통장

  num = 0
  def __init__(self, name="예금주", balance=0, accountType="") :
    self._name = name
    self._balance = balance    
    self._accountType = accountType   
    # self._accountNumber = random.randint(0, 9999)+"-"+random.randint(0, 99)+"-"+random.randint(0, 9999999) ->중복확인안됨
    
    #accountNumber초기화
    
    if accountType == "모임통장":      
      self._accountNumber = '7'+ '979' +"-"+ str(Account.num)
    elif accountType == "입출금": 
      self._accountNumber = '3'+ '333' +"-"+ str(Account.num)
    elif accountType == "정기적금":
      self._accountNumber = '3'+ '388' +"-"+ str(Account.num)
    elif accountType == "자유적금":
      self._accountNumber = '3'+ '355' +"-"+ str(Account.num)
    elif accountType == "세이프박스": 
      self._accountNumber = '3'+ '310' +"-"+ str(Account.num)
    elif accountType == "마이너스통장": 
      self._accountNumber = '3'+ '300' +"-"+ str(Account.num)

  def deposit(self,money): # 입금
    self.set_balance(self.get_balance() + money) 
    print("잔고: ",self.get_balance())

  def withdrawal(self,money): # 출금
    if self.get_balance() - money >= 0:
      self.set_balance(self.get_balance() - money)
      print("잔고: ",self.get_balance()) 
    else :
      print("금액이 부족합니다")
      print("잔고: ",self.get_balance())
      
  def get_name(self):
    return self._name  
  def set_name(self,name):
    self._name = name
  def get_balance(self):
    return self._balance
  def set_balance(self,balance):
    self._balance = balance    
  def get_accountType(self):
    return self._accountType
  def set_accountType(self,):
    self._accountType
  def get_accountNumber(self): #수정불가
    return self._accountNumber    
      
  def account_service(self):
    n = int(input('1.입금 2.출금'))
    money = int(input('얼마?:'))
    if n == 1:
      self.deposit(money)      
    elif n == 2:
      self.withdrawal(money)
    else:
      print('다시입력')  
      self.account_service()   