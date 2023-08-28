#구구단출력하기
for i in range(2,10):
    print("------------", i, "단------------")
    for j in range(1,10):
        #print(str(i) + " X " + str(j) + " = " + str(i*j))
        print("%d X %d = %d" %(i,j,i*j))
    print()
    
#입력값에따라 홀수단,짝수단 출력 선택하기  
    
    
    
#반복문에서 continue break활용하기
x = 1
sum = 0
while(True):
    x = int(input("값을 입력해주세요 : "))
    sum += x
    if x == 0:
        break

print("합계는?", sum)