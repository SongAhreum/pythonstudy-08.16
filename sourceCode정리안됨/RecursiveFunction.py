'''
lst = [1,2,3,1,4,2,1]

def allIndx(lst ,n):
  res =[]
  for i in range(len(lst)):
    if n == lst[i]:
      res.append(i)
  return res    

print(allIndx(lst,1))
print(allIndx(lst,2))
print(allIndx(lst,3))

person1 ={"치킨","피자","족발","삼겹살"}
person2 ={"김밥","김치찌개","삼겹살","쌈밥"}
person3 ={"치킨","김치찌개","떡볶이","초밥","삼겹살","족발","햄버거","보쌈","한우","아이스크림"}

#all any써서 공통음식 찾기 두명부터
#########################################
res = any(food in person2 for food in person1)
common_food = [food for food in person1 if any(food == food2 for food2 in person2)]
# list = [food for food in common_food if food in person3]
lists = [food for food in common_food if any(food == food3 for food3 in person3)]




def allIndx2(l ,n):
  res = list()
  for i in range(len(l)):
    if n == l[i]:
      res.append(i)
  return res 
print(allIndx2(lst,3))



def calc(calc,*args):
  if calc == "+":
    res = 0
    for i in args:
      res += i
    return res
  if calc == "*":
    res = 1
    for i in args:
      res *= i
    return res
  return "해당연산을 시행 할 수없습니다 +,* 만 가능"  
  
print(calc("+",1,2,3,4,5,6,7,8,9)  )
  
print(calc("*",1,2,3,4,5)  )
print(calc("-",1,2,3,4,5)  )

def personal_info(**kwargs):
  for kw, arg in kwargs.items():
    print(kw, ': ', arg, sep='--')
    
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')    
'''
# def test(end):
  
#   if end ==0:
#     return
#   test(end -1)
#   print(end)
  
# test(5)  


# def f_sum(n):
#   if n > 0:   
#     return n + f_sum(n-1)
#   else: return  
  
# def f_number(n):
#   if n == 0:
#     return  
#   f_number(n//10)
#   print(str(n)[len(str(n))-1])
  
  
# f_number(1234)  



#######################################
#재귀함수
#1.두수사이 홀수출력
def betweenOdd(n1,n2):
  if n1> n2 :
    return 
  if n1%2 == 0:
    betweenOdd(n1+1,n2) 
  else:
    print(n1)
    betweenOdd(n1+2,n2)
    return
# betweenOdd(1,31)


#2.피보나치 수열 
#1,1,2,3,5,8,13,21,34...




def fibo(n):
  if n == 2 :
    return 1
  if n == 1:
    return 1
  return fibo(n-1)+fibo(n-2)


  
print(fibo(9))



#10진수 2진수로 변환하기  

def decimalToBinary(m):
  if m < 2:
    return m
  return decimalToBinary(m//2)*10 + (m%2) 

print(decimalToBinary(3))
decimalToBinary(10)

example = [[1,2,3],[4,[5,6]],7,[8,9]]

#1차원으로 변환하는 배열

'''
def flatten(data):
  lst = list()
  for i in data:
    if len(str(i)) == 1:
      lst.append(i)
      return lst
    lst.append(flatten(i))        
        
print(flatten(example)) 
'''        

#list일때만 뽑아오기  
# def flatten(data):
#   lst = list()
#   for i in data:
#     if type(i) == list:        
#       for j in i:
#         if type(j) == list:
#           continue
#         else:
#           lst.append(j)  
#     else :
#       lst.append(i)
#   return lst
      
      
# print(flatten(example))  

def flatten(data):
  lst = list()
  for i in data:
    if type(i) == list:        
      lst += flatten(i)
      # lst.append(flatten(i))  
      # ---> flatten(data)리턴값이 list인데 append하면 list에 list를 요소로 넣는것
      # ---> lst += flatten(i)로 수정
    else :
      lst.append(i)    
  return lst

print(flatten(example))

