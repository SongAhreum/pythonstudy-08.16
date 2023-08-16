# # #Hello world -> Hell world 

# word = "Hello world"
# # idx1 = word.index("o")
# # idx2 = word.index("o",idx1+1,len(word)+1)
# # print(idx1)
# # print(idx2)
# # # def index(self, __sub: str, __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ...) -> int: ...

# # #1.
# # print(word[0:idx1]+word[idx1+1:])
# # #2.
# # print(word.replace("o",""))
# #3.
# lst = list(word)
# # for i in lst:
# #   if(i == "o"):
# #     continue
# #   print(i,end="") #end =\n기본
# newList = ""
# for i in lst:
#   if i == "o":
#     i = ""
#   newList += i;    
  
# print(newList)  
# # n = 0;
# # for i in range(len(lst)-n):
# #   if lst[i] == "o":
# #     del lst[i]
# #     i -= 1 #이걸로안되네 range도안변하고
# #     n += 1
    
    
# for i in range(len(lst)):
#   if i ==len(lst):
#     break
#   if lst[i] == "o":
#     del lst[i]
#     i -= 1 #이걸로안되네 range도안변하고
# print(lst)   

# lst2 = list("Helloooo wooorld") #하나지우고 전으로돌아가는데 그자리를 다시 확인을 못해준다
# # for i in range(len(lst2)):
# #   if i == len(lst2):
# #     break
# #   if lst2[i] == "o":
# #     del lst2[i]
# #     i = 0
# #   print(i)   
# # print(lst2) 
# # iterable한객체가 in 뒤에들어가는데 it.next로 동작해서그런가? 
# # --> while문으로 해결
# i = 0
# while True:
#   if i == len(lst2):
#     break
#   if lst2[i] == 'o':
#     del lst2[i]
#   else: i+=1 
  
# # 삭제하고 다시검사   
# for j in range(len(lst)):  
#   for i in range(len(lst)):
#     if lst[i] == "o":
#       del lst[i]
#       break  

#!!!!!!정렬함수 구현하기이이이
a =[1,2,3]
a.reverse()  
print(a)

#reverse함수 원리구현
#1
tmp = 0;
for i in range(len(a)//2):
  tmp = a[i]
  a[i] = a[len(a)-i-1]
  a[len(a)-i-1] = tmp 

print(a)  
#2
a2 = list()
for i in range(len(a)-1,-1,-1):
  print(a[i],"i:",i)
  a2.append(a[i])
print(a2)

b = 123456
#3. 학원
start, end = 0, len(a)-1

while end > start:
  temp = a[start]
  a[start] = a[end]
  a[end] = temp
  #a[start], a[end] = a[end], a[start]
  start += 1
  end -= 1




#숫자를 list로 
#s =12345
#list(s)안됨


k = list()
while True : 
  if b == 0:
    break
  k.insert(0,b%10)
  b = b//10
  
print(k)  

#sort정렬
sort = [3,9,6,20,-7,5]
print(sort)
# 3,6,9,20,-7,5 -> 3,6,9,-7,20,5 -> 3,6,9,-7,5,20
# 3,6,-7,9,5,20 -> 3,6,-7,5,9,20 -> 
# 3,-7,6,5,9,20 -> 3,-7,5,6,9,20
# -7,3,5,6,9,20
# for i in range(len(sort)):
  
#   if(sort[i]> sort[i+1]):
#     tmp = sort[i]
#     sort[i] = sort[i+1]
#     sort[i+1] = tmp

#
cnt = 0;    
while True:  
  if len(sort)-cnt == 0:
    break
  for i in  range(len(sort)-cnt-1):
    if(sort[i]> sort[i+1]):
      temp = sort[i]
      sort[i] = sort[i+1]
      sort[i+1] = temp
  cnt += 1    
print(sort)

#가운데 값으로 정렬하기
# 3, 5, 6, -7, 20, 9
3, -7, 6, 5, 20, 9

3 6 20
-7 5 9

while True:
  n = len(sort)//2
