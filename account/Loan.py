from abc import ABC, abstractmethod
class Loan(ABC):
  
  def __init__(self,loan_rate,balance,):
    self._loan_rate = loan_rate
  
  @abstractmethod
  def loan(self,money):
    pass
  
  #일년후 상환금액
  @abstractmethod
  def loan_rate(self,money,loan_rate):
    pass
  
  
  def get_loan_rate(self):
    return self._loan_rate
  def set_loan_rate(self,loan_rate):
    self._loan_rate = loan_rate