import Account,Loan
class Credit(Account,Loan):
  CREDIT_TYPE = ['체크카드','현금카드','신용카드']
  # def __init__(self,name,balance,accountType,loan_rate):
  #   Account.__init__(name,balance,accountType)
  #   Loan.__init__(loan_rate)
  def __init__(self,acount,loan_rate):
    Account.__init__(acount.get_name(),acount.get_balance(),acount.get_accountType())
    Loan.__init__(loan_rate)
  
  #체크카드
  
  #현금카드
  
  #신용카드
  
  #한도제한
  
  #대출