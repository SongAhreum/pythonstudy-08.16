from Account import Account
from BankService import BankService
'''
1.
import Account,BankService  
  수정
  ->from Account import Account
    from BankService import BankService

2.
Loan(ABC) < BankService(ABC,LOAN) < Bank(BankService)  :::: TypeError: metaclass conflict: the metaclass of a derived class 
수정 :  Loan(ABC) < BankService(LOAN) < Bank(BankService) 

3.
Credit(Account,Loan) 다중상속시 생성자??
def __init__(self,name,balance,accountType,loan_rate):
  Account.__init__(name,balance,accountType)
  Loan.__init__(loan_rate)


'''
class Bank(BankService):
  PRODUCT__LIST = {"상품명":'금리',"모임통장":0.02,"입출금":0.01,"정기적금":0.06,"자유적금":0.05,"세이프박스":0.05,"마이너스통장":0.09,'대출':0.1}
  
  def __init__(self,bank_name) :
    super().__init__(Bank.PRODUCT__LIST['대출'])
    self._account_list = {}
    self._account_num = 0
    self._bank_name = bank_name
    
  ### get set을 인스턴스변수에서사용하나? 
  def get_account_cnt(self):
    return self._account_num
  def increase_account_num(self):
    self._account_num += 1
  def get_bank_name(self):
    return self._bank_name
  def get_account_list(self):
    return self._account_list



  #개좌개설
  def oppen_account(self):
    #계좌유형
    acount_type_list = [key for key in Bank.PRODUCT__LIST.keys() if key not in ["상품명", "대출"]]
    print("/".join(acount_type_list))
    accountType = input('원하는 계좌유형을 입력하세요')
    try:
      Bank.PRODUCT__LIST[accountType]
    except KeyError:
      print('다시입력하세요')
      self.oppen_account()
    except Exception as e:
      print(e.__traceback__) #print('에러! 서비스종료') import logging쓰려면 다읽어야하나... 
      return      
    name = input("이름: ")
    balance = int(input('초기금액: '))
    
    #확인용
    a = Account(name, balance, accountType)
    print(a.get_accountNumber())
    self._account_list[self._account_num] = a
    # self._account_list[self._account_num] = Account(name, balance, accountType)
    self.increase_account_num()
    

  #대출관련 LOAN /binance의 200%대출가능
  def loan(self,money,loan_rate):
    amount = money *2 
    repayment = self.loan_rate(amount,loan_rate)  
    print(f'일년 후 상환금액은{repayment} 입니다.')
    return amount
    
  #대출금리적용/일년 후 예상상환금액
  def loan_rate(self,amount,loan_rate):
    return amount*(loan_rate+1)
  
  #상품금리적용
  def interest_rate(self,account):
    pass
  
  #상품안내
  def productInfo(self):
    for key, value in Bank.PRODUCT__LIST.items():
      if key == '상품명':
        print(f'<{key}({value})>')
        continue
      print(f'{key}({value}),', end=" ")
    print()
    print('-------------------------')
  
  def service(self):
    
    print(f'---------{self._bank_name}입니다---------')
    self.productInfo()
    
    n = int(input('1.계좌개설 2.입출금 3.통장해지 4.대출'))
    while True:
      if n<1 or n>4 or type(n) != int :
        n = int(input('다시입력해주세요 1.계좌개설 2.입출금 3.통장해지 4.대출'))
      else:
        break
    
    if n == 1:     
      self.oppen_account()
      self.service()
    elif n == 2:
      accountNumber = input('계좌번호입력 :')
      my_acount = [[key,value] for key,value in self._account_list.items() if value.get_accountNumber() == accountNumber]
      my_acount = self.get_account_list()[my_acount[0][0]]
      while True:
        # my_acount[0][1] = my_acount[0][1].account_service()
        my_acount.account_service()
        n = input("1.해당계좌로 거래를 계속? 2.처음메뉴 3.종료")
        if n == '2':
          self.service()
        elif n == '3':
          return
        else:
          continue
    elif n == 3:
      accountNumber = input('계좌번호입력 :')
      #value -> Acount ()에서 돈,
      #key로 딕셔너리 list 에서 삭제
      ####gerator라 한번쓰면없어짐 ! 
      my_acount = [[key,value] for key,value in self._account_list.items() if value.get_accountNumber() == accountNumber]
      my_acount = self.get_account_list()[my_acount[0][0]]
      #다른계좌로 banance송금 
    elif n == 4:
      # 빌릴금액입력
      self.loan()       
k = Bank('신한')
k.service()