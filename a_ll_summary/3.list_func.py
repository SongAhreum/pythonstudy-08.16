x = int(input("찾고자 하는 값을 입력해주세요 : "))

a = [1,1,2,2,3,3]
print(a.count(x))

count = 0
# count 함수 원리 구현해보기
# for(int i=0; i<a.length; i++) {
#     if(x == a[i]) {
#         count++;
#     }
# }

for i in range(len(a)): #range(0, len(a), 1)
    if x == a[i]:
        count += 1

print(count)


a = [1,2,3]
a.reverse()
print(a) #[3,2,1]

b = []
# reverse 함수 원리 구현해보기
for i in range(len(a)-1, -1, -1): #for(int i=a.length-1; i>-1; i--)
    b.append(a[i])

print(b)

start, end = 0, len(a)-1
temp = 0
while end > start:
    temp = a[start]
    a[start] = a[end]
    a[end] = temp #a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1

print(a)

for i in range(len(a)//2):
    temp = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a) - i - 1] = temp

print(a)

# 3번
# list 함수 원리 구현해보기 (숫자로)
# s = 123456
# lst = list(s)
# print(lst)

#오답 1 :
s = "123456"
#오답 2 :
s = [1,2,3,4,5,6]
#오답 3 :
s = 123456
s2 = str(s)



# (1)[3,6,9,20,-7,5] 리스트를 sort와 같은 함수를 사용하지말고 for문을 활용하여 오름차순으로 정렬해주세요.

# 5x2 이차원 리스트 만들어서 1~10까지 채우기
lst = [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10]
      ]

# int[][] arr = new int[5][2];
#
# for(int i=0; i<arr.length(); i++) {
#     for(int j=0; j<arr[0].length(); j++) {
#         arr[i][j] = 5*i+j+1
#     }
# }

##########################################################
# day02
# # 5x2 이차원 리스트 만들어서 1~10까지 채우기
lst = [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10]
      ]

# int[][] arr = new int[5][2];
#
# for(int i=0; i<arr.length(); i++) {
#     for(int j=0; j<arr[0].length(); j++) {
#         arr[i][j] = 5*i+j+1
#     }
# }

print(len(lst))
print(len(lst[0]))

for i in range(len(lst)) :
        for j in range(len(lst[0])):
                lst[i][j] = 2*i+j+1

for i in range(len(lst)) :
        for j in range(len(lst[0])):
                print(lst[i][j], end=" ")
        print()

lst = []
num = 1

for i in range(5):
        temp = []
        for j in range(2):
                temp.append(num)
                num+=1
        lst.append(temp)

print(lst)

# 3번
# list 함수 원리 구현해보기 (숫자로)
# s = 123456
# lst = list(s)
# print(lst)

s = 123456
lst = []

while s > 0:
        #lst.insert(0,s%10)
        lst.append(s%10)
        s = s // 10

lst.reverse()

print(lst)
lst = []
s = 123456
num = 10
count = 0

while s > num:
        num *= 10
        count += 1

print(count)
print(s//10**count)

while s > 0:
        lst.append(s//10**count)
        s = s % 10**count
        count -= 1

print(lst)


##########
#min, max, sum
lst = [1,2,3,4,5,6,7,8,9]

print(max(lst))
print(min(lst))
print(sum(lst))

maxNum = lst[0]
minNum = lst[0]
sumNum = 0

for i in lst:
    if maxNum < i:
        maxNum = i

    if minNum > i:
        minNum = i

    sumNum += i

print("max : ", maxNum, ", min : ", minNum, ", sum : ", sumNum)

#split, join
fruit = "apple,pear,corn,carrot"
fruit_list = fruit.split(",")
print(fruit_list)

fruit = "-".join(fruit_list)
print(fruit)

fruit = "apple,pear,corn,carrot"
for i in fruit:
    if i == ',':
        print(end=" ")
    else :
        print(i, end = "")
print()
fruit_list = []
s = ''
for i in fruit:
    if i == ',':
        fruit_list.append(s)
        s = ''
    else :
        s += i
fruit_list.append(s)

print(fruit_list)

fruit = "apple,pear,corn,carrot"
fruit_list = []
s = 0

for i in range(len(fruit)):
    if fruit[i] == ',' or fruit[i] == '-' or fruit[i] == '+':
        fruit_list.append(fruit[s:i])
        s = i + 1

fruit_list.append(fruit[s:len(fruit)])

print(fruit_list)

# 아스키코드
print(ord('z')) #ordinal position
print(chr(97)) #character

# 기계어- - -(컴퓨터) - 어셈블리어 - 고급언어 - - -(사람)

fruit = "apple,./+pear-25-corn,carrot"
fruit_list = []
s = 0
for i in range(len(fruit)):
    if not((ord(fruit[i]) >= 65 and ord(fruit[i]) <= 90) or (ord(fruit[i]) >= 97 and ord(fruit[i]) <= 122)):
        if fruit[s:i] != "": # s != i-1
            fruit_list.append(fruit[s:i])
        s = i + 1

fruit_list.append(fruit[s:len(fruit)])

print(fruit_list)

fruit = "carrotapplecornpear" #만약 구분자가 없다면, 단어 데이터베이스
fruit_list = ['apple', 'pear', 'corn', 'carrot'] # 임시 데이터베이스
lst = []

s = ''
for i in fruit:
    s += i

    for j in fruit_list :
        if s == j :         #if s in fruit_list:
            lst.append(s)
            s = ''

if s in fruit_list:
    lst.append(s)

print(lst)