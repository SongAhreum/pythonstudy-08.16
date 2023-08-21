

arr = [[i*8+j+1 for j in range(0,8)] for i in range(0,8)]

arr = [[i*5+j+1 for j in range(0,5)] for i in range(0,5)]


# for i in range(0,5):
#   for j in range(0,5):
#     arr[i][j] = i*j+j+1
#     print(arr[i][j]," ",end="")
#   print()  




###딕셔너리
# dic = {"name":input("이름:"),"age":input("나이:"),"phone":input("전화번호:")}

# name = input("이름:")
# age=input("나이:")
# phone=input("전화번호:")

# dic = dict(name = name,age = age,phone = phone)
# print(dic)

##set

p1 = {'마라탕','꿔바로우','마라샹궈','지삼선'}
p2 = {'마라탕','꿔바로우','어향가지','볶음밥'}
p3 = {'꿔바로우','지삼선','어향가지'}


#1.3명이 각각 먹고싶은 여러음식이잇을때 어떤메뉴? 
###########리스트에서 교집합을 구현하는방법을 생각해보자

m1 = set(p1)
m2 = set(p2)
m3 = set(p3)

print(m1&m2&m3)

#두명이 서로음식교환 이미갖고있는음식교환안됨
#1.
# c1 = m1 - m2
# c2 = m2 - m1

# m2 = (m1&m2)|c1
# m1 = (m1&m2)|c2

# minus = input()
# res = m1 - {"마라샹궈"}
# print(res)


#2.
# n = input("누구와 교환할것입니까? 2.p2 3.p3")
# if n == 2:
#   #p1이 p2와 메뉴교환할 거임
#   myfood = {input("어떤을음식교환")} #'마라샹궈','지삼선'
#   yourefood ={input("어떤음식과 교환")}#'어향가지','볶음밥'
#   m1 - myfood
#   m1|yourefood
 
  
#3.
# m1.add()
# m1.remove()

# a = {'a':"b",'c':'d'}
# key =a.keys()
# key = list(key)
# print(key)


# lst = [1,2,3,4,5,6,7,8,9]
# max = 0
# min = 0
# sum = 0
# for i in lst:
#   if max < i:
#     max = i
#   if min > i :
#     min = i  
#   sum += i 
  
  
   
# print(max) 
   
# def switch(key):
#   telecom = {"011" : "SKT", "016": "KT", "019" : "LGU"}.get(key, "알 수 없는")
#   print(f'당신은 {telecom} 사용자입니다.')

# firstNumber = input().split("-")[0] 
# switch(firstNumber),

#split,join구현하기

#1.split구현하기
'''
fruit ="alppe,pear,corn,carrot"

seperator = input("어떤문자로 나눌것입니까?: ")

res = list()
str =""
for i in fruit:
  if(seperator == i):  
    res.append(str)
    str = ""
    continue 
  str  = str + i  
res.append(str)
print(res) 

res3 = list()
s = 0
for i in range(len(fruit)):
  if fruit[i] ==",":
    res3.append(fruit[s:i])
    s = i+1
res3.append(fruit[s:])    
print("res3:",res3)
'''   
#####

# print(ord('a'))
# print(ord('b'))
# print(ord('A'))
# print(ord('B'))
# print(ord('-'))
# print(ord('+'))
# print(ord(','))
# print(chr(64))
result = list()
fruit ="alppe-/, --pear++corn,carrot" 
s = 0
for i in range(len(fruit)):
  if not (ord(fruit[i])>=65 and ord(fruit[i])<=90 )or(ord(fruit[i])>=97 and ord(fruit[i])<=122 ):
    if fruit[s:i] != "":
      result.append(fruit[s:i]) 
    s = i+1
result.append(fruit[s:])
#print(result)

##만약구분자가없다면 ,단어데이터베이스?   
fruit ="applepearcorncarrot"    
sample = ['apple','pear','corn','carrot']

# result = list()
# s =""
# for i in fruit:  
#   s = s+i
#   for j in sample:
#     if j == s:
#       result.append(s)
#       s=""
# print(result)

result = list()
s =""
for i in fruit:
  s += i  
  if s in sample:
    result.append(s)
    s=''
print(result)


random = list()
sampleNum = len(sample)
fruit ="ccadpsappledsfpeardcsfcornsdfscarrot"

for i in range(len(fruit)):
  for j in range(sampleNum):
    if(fruit[i] == sample[j][0]) and i+len(sample[j]) <= len(fruit) :                
      if fruit[i:i+len(sample[j])] == sample[j]:        
        random.append(fruit[i:i+len(sample[j])])
print(random)

zeroList = [ 0 for i in range(10)]
zeroList = [i for i in range(1) for j in range(10)]
print(zeroList)
#1.
word =['school','game','piano','science','hotel','mountian']
comp = [i for i in word if len(i)>= 6]
print(comp)
comp = [len(i) for i in word if len(i)>= 6]
print(comp)
#2.
comp = [len(i) for i in word ]
print(comp)   
'''
#2.join구현하기
res2 =""
delimiter = input("어떤문자로 이을 것입니까?: ")
for i in res:
  if(res2 == ""):
    res2 = i
    continue
  res2 = res2+delimiter+i
  
print(res2)
'''
a=[[10,20],[30,40],[50,60]]
b =[[2,3],[4,5],[6,7]]

result = [[20,60],[120,200],[300,420]]
# {a[0][0]*b[0][0],a[0][1]*b[0][1]},{a[1][0]*b[1][0],a[1][1]*b[1][1]},{a[2][0]*b[2][0],a[2][1]*b[2][1]}

result = [[ a[i][j]*b[i][j] for j in range(len(a[i]))] for i in range(len(a))  ]

result = [ x for i in range(len(a))]
  
x : 
[ a[0][j]*b[0][j] for j in range(len(a[0]))] # -> [a[0][0]*b[0][0] , a[0][1]*b[0][1]] 
[ a[1][j]*b[1][j] for j in range(len(a[1]))] # -> [a[1][0]*b[1][0] , a[1][1]*b[1][1]]
[ a[2][j]*b[2][j] for j in range(len(a[2]))] # -> [a[2][0]*b[2][0] , a[2][1]*b[2][1]]


#result를 컴프리헨션으로만들기
print(result)
result = [[(i+j+1)+i for j in range(2)] for i in range(3)]
# i : 0 1 2 j: 0 1

# i : 0 j : 0   -> 1
# i : 0 j : 1   -> 2

# i : 1 j : 0   -> 3
# i : 1 j : 1   -> 4

# i : 2 j : 0   -> 5
# i : 2 j : 1   -> 6



print(result)

#[[1,2][3,4][5,6]]을 리스트 컴프리헨션으로 만들기