######별찍기

#1.
# for i in range(5):
#   for j in range(5):
#     print("*" ,end="")
#   print()  

lst1 = [["*" for i in range(5)] for j in range(5)]
print(lst1)
for i in lst1:
  for j in i:
    print(j,end="")
  print()  
print()    
#2.
# for i in range(5):
#   for j in range(5):
#     if j <= i:
#       print("*",end="")
#     else:
#       print(end=" ")  
#   print()

lst2 = [["*" if j<=i else " "  for j in range(5) ]for i in range(5) ]
print(lst2)
for i in lst2:
  for j in i:
    print(j,end="")
  print() 
print()  
  
#3.  
# for i in range(5):
#   for j in range(5):      
#     if i == j:
#       print("*",end="")
#     else:
#       print(" ",end="")  
#   print()    

lst3 =[["*" if i==j else " " for j in range(5)]for i in range(5)]
print(lst3)
for i in lst3:
  for j in i:
    print(j,end="")
  print() 
  
print()
#4.
# for i in range(5):
#   for j in range(5):  
#     if 5-j-i > 0:      
#       print("*",end="")
#     else:
#       print(" ",end="")  
#   print("")  

lst4 = [["*" if 5-j-i>0 else " " for j in range(5)]for i in range(5)]
print(lst4)
for i in lst4:
  for j in i:
    print(j,end="")
  print()
print() 

#5.  
#i=0 j 01234 i=1 j 1234 i=2 j 234  
# for i in range(5):
#   for j in range(5):        
#     if j >= i:
#       print("*",end="")
#     else:      
#       print(" ",end="")  
#   print()

lst5 = [["*" if j >= i else " " for j in range(5)]for i in range(5)]
print(lst5)
for i in lst5:
  for j in i:
    print(j,end="")
  print()
  
#list에서 i랑 j뽑자  
for i in range(len(lst5)):
  for j in range(len(lst5[i])):
    print(lst5[i][j],end="")
  print()  


iGenerator = (i for i in range(5) )

#########학원풀이
print()
print("-------------------------------------")
print()

#2.
for i in range(5):
  for j in range(i+1):  #########
    print("*",end="")
  print()

list2 = [["*" for j in range(i+1)] for i in range(5)]
list2 = ["*"*(i+1)+"\n" for i in range(5)] ##########

#3.
list3 = [" "*i+"*" for i in range(5)]
print(list3)
#4.
list4 = ["*"*(5-i) for i in range(5)]
print(list4)

#5
list = [" "*i+"*"*(5-i) for i in range(5)]


for i in range(5):
  for j in range(5):
    if j >= i:
      print("*",end="")
    else:
      print(" ",end="")
  print()
        
for i in range(5):
  for j in range(5):
    if i >=j:
      print("*",end="")
    else:
      print(" ",end="")
  print()  
  
  list = ["asd",'sdf']
  print(list)
  list = ["asd" 'sdf']
  print(list)  