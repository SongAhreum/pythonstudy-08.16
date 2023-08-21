def add(x,y):
  return x+y

add_lambda = lambda x,y:x+y 
#lambda 람다 키워드
#arguments 매개변수 x,y
#expression 표현식 x+y

# print(add(3,4))
# print(add_lambda(3,4))

#map함수 - ㅠ파이썬내장함수
#주어진 함수를 반복가능한 객체(iterable한객체)의 각원소에 적용하고 결과를 반환한다

#map(function,iterable)

def square(x):
  return x*x

lst = [1,2,3,4,5]

# square_list = map(square,lst)
# list = list(square_list)
# print(list)


square_list = map(lambda x:x*x,lst)
result = list(square_list)
# print(result)


def f(x):
  if x%2 ==0:
    return 0
  else :
    return x
# print(list(map(f,lst)))

###############
#filter : 파이썬내장함수 import필요없
#주어진 함수를 반복가능한 객체(iterable한객체)의 결과가 참인 원소들만 반환한다

#filter(function,iterable) -> return값이 boolean일때만 사용
def is_even(x):
  return x%2 ==0

lst = [1,2,3,4,5,6,7,8]
even_lst = filter(is_even,lst)
# print(list(even_lst))
# print(list(filter(lambda x : x%2 == 0 ,lst)))

# list(filter(lambda x:x>2,lst))

numbers = [12,32,55,12,32,4,86,50]
result = list(map(lambda x : "합격" if x >60 else "불합격" if x < 50  else "대기",numbers))
print(result)

filse = ["memo.txt","1.jsp","32.png","23.jpg","223.jpg"]

# 리스트에서 확장자가 jpg만 골라내는 리스트를 만드세요 람다 필터
result = list(filter(lambda x : x.endswith('jpg'), filse))
print(result)


def Find(str):
  idx = 0;
  for i in range(len(str)):
    if str[i] == ".":
      idx = i #쨋든 젤 마지막 '.'인덱스가 idx임  
  return str[idx+1:]    

filse = ["memo.txt","1.jsp","32.png","23.jpg","223.jpg"]
result = list(filter(lambda x : Find(x) == "jpg" ,filse))
print(result)


filse = ["memo.txt","1.jsp","32.png","23.jpg","223.jpg"]
result = list(filter(lambda x : '.jpg' in x ,filse))
print(result)


###list세개의곱

lst1=[1,2,3,4,5]
lst2=[1,3,5,7,9]
lst3=[2,4,8]

result = list(map(lambda x,y,z : x*y*z , lst1,lst2,lst3))
result = list(map(lambda x: x[0]*x[1]*x[2] , zip(lst1,lst2,lst3))) 
#zip함수는 iterable한 객체들을 매개변수로 받아 tuple로 반환
print(result)


#1부터 10까지 제곱값중 홀수만 출력
lst = list(range(1,11))
result = list(map(lambda x : x*x ,filter(lambda x : x%2 ==1,range(1,11)))) 
print(result)


