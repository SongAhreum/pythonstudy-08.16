from abc import ABC, abstractmethod
from Loan import Loan

class BankService(Loan):
  
  def __init__(self,loan_rate):
    super().__init__(loan_rate)


  #대출관련 LOAN
  @abstractmethod
  def loan(self,money):
    pass
  
  #대출금리적용/일년 후 예상상환금액
  @abstractmethod
  def loan_rate(self,money,loan_rate):
    pass

  #상품금리적용/일년후
  @abstractmethod
  def interest_rate(self,accountType):
    pass
  
  #상품안내
  @abstractmethod
  def productInfo(self,accountType):
    pass