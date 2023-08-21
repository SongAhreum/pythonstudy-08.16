class Calculator:
  '''
  # def ord(__c: str | bytes | bytearray) -> int: ...
  print(ord("+")) #43
  print(ord("-")) #45
  print(ord("x")) #120
  print(ord("%")) #37
  print(ord("(")) #40
  print(ord(")")) #41
  print(ord("=")) #61
  
  # def chr(__i: int) -> str: ...
  print(chr(43))
  '''
  
  #연산식계산 우선순위 : ()-> x%(x생략가능) -> +-
  #메모리기능?
  
  def __init__(self):
    self.result = 0
    self.__memory = list()
  
  
  #이전계산결과
  def getMemory(self):
    return self.__memory 
  def setMemory(self, x):
    self.__memory.append(x)
  #이전계산결과확인
  def checkMemo(self):
    memo = self.getMemory(self)
    print(memo)
  #저장한 계산결과  all삭제
  def removeAllMemo(self):
    self.setMemory(list())  
  #저장한 계산결과  선택 삭제
  def removeMemo(self):
    memo = self.getMemory()
    for i in range(len(memo)):
      print(i + 1, ".", memo[i])
    idx = input("삭제할 번호: ")-1
    memo.remove(memo(idx)
                )  
    
    
  def singleCal(self,a,b,c,d): # d = "=" 디폴트로 둘수있나?
    if (type(a) == int or type(a) == float) and type(b) == str and (type(c) == int or type(c) == float) and d =="=": #type체크해서 b =="+", =="-", =="x", =="%" 로해서 하는거랑 차이?
      
      if ord(b) == 43:
        # print(a + c)
        return a  + c
      elif ord(b) == 45:
        # print(a - c)
        return a - c
      elif ord(b) == 120:
        # print(a * c)
        return a * c
      elif ord(b) == 37:
        # print(a / c)
        return a / c
      else:
        print("잘못입력하셨습니다.1")          
    
    else:
      print("잘못입력하셨습니다.2")   
  
  #일반계산기 - 순차적계산
  def generalCal(self,*args):
    if args[len(args)-1] != "=":      
      print("잘못입력하셨습니다3")
      return
    # 1+ 2- 3+ 4- 5
    exp = self.singleCal(args[0],args[1],args[2],"=") #유효성체크도됨   
    
    for i in range(3,len(args)-1,2):                        
      if type(args[i]) == str or type(args[i+1]) == int:
        exp = self.singleCal(exp,args[i],args[i+1],"=")          
      else:        
        print("잘못입력하셨습니다4")
        return
    return exp  
  
  #괄호 연산제외 -> x % 우선 (x생략안됨)
  def expressionCal(self,*args):
    args = list(args)
    if args[len(args)-1] != "=": 
          
      print("잘못입력하셨습니다5")
      return
    
    for i in range(len(args)-1):
      # if (i%2 == 0 and (type(args[i]) == int or type(args[i]) == float)) or (i%2 == 1 and type(args[i]) == str):  
      # #체크(return self.generalCal(*args)에서 될거임)
      
      # if ord(args[i]) == 120: #ex) ~~~~~3-4x5-4 or ~~~~~3+4x5-4 or 3+4x5x4  args가 튜플이라 수정이안되나...list로?
      # # 1. - 연산자를 -1*로 바꿀지
      # # 2. 순차적으로 연산하다가 x,%가 나오면 앞숫자와 앞숫자의 바로 전 연산자를 체크해서(-인지) 처리할지  
      # # 3. 연속으로 x,% 
        
      # 1. 
      if args[i] == "-":
        args[i+1] = -1 * args[i+1]
        args[i] = "+"
      if args[i] == "x":  # + -5(i-1) x(i) 3(i+1)
        args[i+1] = args[i-1]*args[i+1]
        args[i-1] = 0
        args[i]="+"
      elif args[i] == "%":
        args[i+1] = args[i-1]/args[i+1]
        args[i-1] = 0
        args[i] = "+"
            
      # else:
      #   print("잘못 입력하셨습니다") 
    
    return self.generalCal(*args)      
  
#()연산 (,)가나오는 index기준으로 잘라서 list에 포함후 계산하려고했음 -> ( (   ) + (  ) )( )이런형태안됨 
  #( )포함연산
  def expressionCalPlus(self,*args):
    startIdx = list()
    endIdx = list()
    for i in range(len(args)):
      if args[i] == "(":
        startIdx.append(i)
      elif args[i] == ")":   
        endIdx.append(i)
    
    
    pass
  
  
  # # 3+5(5-6-3-1-4) 는 가능하나 3+5(5-6-(3-1)-4) 괄호안에 괄호는 어려움 다시하기    
  # def expressionCal(self,*args):
    
  #   if args[len(args)-1] != "=":      
  #     print("잘못입력하셨습니다")
  #     return
    
  #   expressions = list()
  #   startIdx = 0
  #   endIdx = 0
  #   for i in range(len(args)-1):   #i = arsg의 index   
  #     if ord(args[i]) == 40:
  #       if startIdx == 0:
  #         expressions.append(args[0:i])
  #         startIdx = i
  #       else:
  #         expressions.append(args[endIdx+1:i])
  #         startIdx = i           
  #       continue      
  #     elif ord(i) == 41:
  #       expressions.append(args[startIdx+1:args[i]])
  #       endIdx = i
  #   expressions.append(args[endIdx+1:len(args)-2])    

    # for i in range(len(args)-1):      
    #   if ord(i) == 40:
    #     startIdx.append(i)
    #     continue
    #   elif ord(i) == 41:
    #     endIdx.append(i)  
    #     continue
    # for i in range(len(startIdx)):
    #   if i == 0:
    #     expressions.append(args[0:startIdx[i]])
    #     expressions.append(args[startIdx[i]+1:endIdx[i]])
    #   else:
    #     expressions.append(args[endIdx[i]+1:startIdx[i]])
    #     expressions.append(args[startIdx[i]+1:endIdx[i]])
    # expressions.append(args[endIdx[i]+1:args[len(args)-1]) 
  
  
  # def singleCal(self,a,b,c,d):
  #   if (type(a) == int and type(b) == str and type(c) == int and  d == "=") and (b =="+" or b =="-" or b =="x"or b =="%"):     
  #     if b == 'x':
  #       b ="*"
  #     if b == '%':
  #       b =="/"  
  #     exp = str(a)+b+str(c)
  #     self.result  = eval(exp)
  #     print(self.result) 
  #   else :
  #     print("제대로입력하여 주세요")

  # def multiCal(self,*args):
  #   lst = list()
  #   exp = ""
  #   #입력값체크
  #   if args[len(args)-1] != "=":
  #     print("잘못입력했습니다")
  #     return
    
  #   for i in range(len(args)-1): #마지막 =연산자 제외    
    
  #     if (i%2 == 0 and type(args[i]) == int) or (i%2 == 1 and type(args[i]) == str):
        
  #       if args[i] =="%":
  #         exp = str(eval(exp))
  #         args[i] == "/"       
          
  #       elif args[i] =="x":
  #         exp = str(eval(exp))  
  #         args[i] == "*"          
  #       exp += str(args[i])
          
  #     else:
  #       print("잘못입력하였습니다")
  #       return                          
    
  #   self.result = eval(exp)
  #   print(self.result)
  
  #지수로그?삼각함수?적분?진수변환?
  #방정식계산?   
    
      
    

car = Calculator() 
print(car.singleCal(1,"-",2,"=") )
print(car.generalCal(1,"-",2,"+",4,"="))
print(car.expressionCal(1,"-",2,"x",8,"+",4,"%",7,"="))


