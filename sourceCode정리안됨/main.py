word = "Apple Banana"
print(len(word))

print(word.replace("Banana","Orange"))
print(word)

print(word.upper())
print(word.lower())
print(word.replace(" ",""))
word = word.replace("Banana","Orange")
print(word)

f1 , f2 = 3,4
print(f1)
print(f2)

# print 1.서식지정자 2. format 3. f-string 정리할것 ########################

score = int(input())
if score >= 90 :
  print("축하합니다 당신은 합격입니다")
else :
  print("불합겨어억")  
  
for i in range(0,10):
  print(i)
  
for i in range(10): #내부원리는 똑같다
  print(i)

a = int(input("몇단을 출력하시겠습니까? : "))
for i in range(1,10):
  print("%d x %d = %d" %(a,i,a*i))  
  
print("구구단출력하기") 
for i in range(2,10):
  # print("---%d단출력---"%i)
  print("---",i,"단---")  
  for j in range(1,10):
    print("%d x %d = %d" %(i,j,i*j)) 

x = int(input("몇단?:"))  
for i in range(x):
    print(x,"x",i," = ",x*i) #+연산자가 안되는이유가 print안에 요소들이 str이아니라서
    
for i in range(2,10):
  for j in range(1,10):
    # print(str(i),x,str(j),"=",str(i*j))
    print(str(i)+x+str(j)+"="+str(i*j))    


# #가위바위보 좀더생각해보기이이이ㄴㅋ    
import random   
random.randint(1,3)
win = 0
same = 0;
i = 0;
a =[3,1,2,3]
while(i<4):
  i += 1
  user = int(input("가위1바위2보3를 입력해주세요"))
  if user not in range(1,4):
    break;
  computer = random.randint(1,3)
  if(user == computer):
    same += 1
    continue
  if(user == 1 and computer == 3):
    win += 1
  elif(user == 2 and computer == 1):
    win += 1
  elif(user == 3 and computer == 2):
    win += 1


print("(전체:",i,"승리:",win,"무승부",same,")")  



check = int(input("짝수단을출력하려면 0을입력하고 홀수단을 출력하려면 1을 입력하세요:"))

for i in range(2,10):
  if i%2 != check :
    continue
  print("---",i,"단---")  
  for j in range(1,10):
    # print(str(i),x,str(j),"=",str(i*j))
    print(str(i)+"x"+str(j)+"="+str(i*j)) 

check = int(input("짝수단을출력하려면 0을입력하고 홀수단을 출력하려면 1을 입력하세요:"))
for i in range(2+check,10,2):
  print("---",i,"단---")  
  for j in range(1,10):
    print(str(i),"x",str(j),"=",str(i*j))
