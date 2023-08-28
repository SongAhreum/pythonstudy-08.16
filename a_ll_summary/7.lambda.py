#람다(lambda)는 익명 함수를 생성하는 키워드다. 코드를 짧게 만드는데 사용됨.
#함수를 만들 때, 간단한 함수를 만든다. 매개변수, return, def.. 과정들이 너무 번거롭기 때문에

# lambda arguments: expression

def add(x,y):
    return x+y

add_lambda = lambda x,y: x+y
# lambda 람다 키워드
# arguments 매개변수 x,y
# expression 표현식 x+y

print(add(3,4))
print(add_lambda(3,4))

# map 함수 - 파이썬 내장 함수
# 주어진 함수를 반복 가능한(iterable) 객체의 각 원소에 적용하고, 결과를 반환한다.

# map(function, iterable) -> 원래 객체의 각 원소에 해당 함수를 적용한 결과

def square(x) :
    return x * x

lst = [1,2,3,4,5]
square_list = map(square, lst)
lst = list(square_list)

lst = [1,2,3,4,5]
square_list = map(lambda x: x*x, lst)
lst = list(square_list)

print(lst)

a = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(a)):
    if a[i] %2 == 0:
        a[i] = 0

print(a)

def f(x):
    if x%2 == 0:
        return 0
    else:
        return x

for i in range(len(a)):
    a[i] = f(a[i])

print(a)

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(f,a)))
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: 0 if x%2==0 else x,a)))

# filter 함수 - 파이썬 내장 함수
# 주어진 함수를 반복 가능한(iterable) 객체의 결과가 참인 원소들만 반환한다.

# filter(fuction, iterable)

def is_even(x): #return값이 boolean
    return x%2 == 0

lst = [1,2,3,4,5]

even_lst = filter(is_even, lst)
even_lst = filter(lambda x: x%2 == 1, lst)

print(list(even_lst))

numbers= [12,32,55,12,32,4,86,50]
print(list(map(lambda x: "합격" if x>60 else "대기" if 50<x else "불합격", numbers)))

files=["memo.txt","1.jpg","32.png","23.jpg","223.jpg"]

print(list(filter(lambda x: x.find(".jpg") != -1, files)))
print(list(filter(lambda x: '.jpg' in x, files)))

for i in files:
    if ".jpg" in i:
        print(i)

# 숙제 - in, .jpg 사용하지 않고

# 리스트 세 개의 곱
lst1 = [1,2,3,4,5]
lst2 = [1,3,5,7,9]
lst3 = [2,4,8]
print(list(map(lambda x,y,z: x*y*z, lst1,lst2,lst3))) #[2, 24, 120]
print(list(map(lambda x: x[0]*x[1]*x[2], zip(lst1,lst2,lst3)))) #(1,1,2), (2,3,4), (3,5,8)

#1부터 10까지의 제곱 값 중 홀수만 출력해보기
a = list(map(lambda x: x*x, range(1,11)))
print(a)

print(list(filter(lambda x : x%2 == 1, a)))

print(list(filter(lambda x : x%2 == 1, map(lambda x: x*x, range(1,11)))))

files=["memo.txt","1.jpg.jpg","32.png","23.jpg","223.jpg"]

print(list(filter(lambda x: x.find(".jpg") != -1, files)))
print(list(filter(lambda x: '.jpg' in x, files)))

for i in files:
    if ".jpg" in i:
        print(i)

# 숙제 - in, .find 사용하지 않고
print(list(filter(lambda x: ".jpg" == x[len(x)-4:], files)))

lst = []
for i in files:
    for j in range(len(i)):
        if(i[j] == '.') :
            if i[j+1:] == 'jpg':
                lst.append(i)
            break
print(lst)
str = "jpgpgjgpjpgjgpjgpjgpjpgjpjgp" # 몇 개의 jpg가 들어가있는지
count = 0

for i in range(len(str)-2):
    if str[i] == 'j' and str[i+1] == 'p' and str[i+2] == 'g':
        count += 1

print(count)

lst = []

for i in range(len(str)-2):
    if str[i] + str[i+1] + str[i+2] == 'jpg':
        lst.append(str[i:i+3])
print(len(lst))
# 숙제2 - 람다식으로 써보기

# 숙제1 - 몇 개의 gpjgpj가 있는지 gpjgpjgpj - 1개 (겹치는 것 불가)

str = "jpgpgjgpjpgjgpjgpjgpjpgjpjgp"

# 숙제1 - 몇 개의 gpjgpj가 있는지 gpjgpjgpj - 1개 (겹치는 것 불가)
for i in range(10):
    if i==3:
        i = 8
    print(i)

# for(int i=0; i<str.length(); i++)

i = 0
count = 0
while i<len(str)-5:
    temp = ""
    for j in range(6):
        temp += str[i+j]
    #if str[i] + str[i+1] + str[i+2] ...
    if temp == "gpjgpj":
        count += 1
        i += 5
    i += 1

print(count)
count = 0
while len(str) >= 6:
    temp = ""
    for j in range(6):
        temp += str[j]

    if temp == "gpjgpj":
        count += 1
        str = str[6:]

    str = str[1:]

print(count)

# 숙제2 - 람다식으로 써보기
str = "jpgpgjgpjpgjgpjgpjgpjpgjpjgp"
res = list(filter(lambda x : x[0] == "j", [str[i:i+3] for i in range(len(str) - 2)]))
print(res)
result = list(filter(lambda y : y == "jpg", res))
print(result)
print(list(filter(lambda y : y == "jpg", list(filter(lambda x : x[0] == "j", [str[i:i+3] for i in range(len(str) - 2)])))))