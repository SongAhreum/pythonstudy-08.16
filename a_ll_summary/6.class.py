# 함수 매개변수

# 1. 기본 인자값(Default Argument Values)
# 함수에 전달되는 기본 매개변수 기본값을 지정해주는 것

def func1(pa1 = 1, pa2 = 2, pa3 = 3):
    return 0

# 2. 키워드 인자(Keyword Argument)
# 함수에 전달되는 인자를 키-값 의 형태로 전달하는 것
# 순서 상관없이 키값에 일치하는 곳에 값이 전달된다.

def greeting(name, message = "Hello"):
    print(f"{message}, {name}")

greeting(message="안녕", name="홍길동")
greeting(name="김철수")

# 3. 가변 인수 리스트(Arbitrary Argument Lists)
# 함수에 전달되는 매개변수 앞에 (*)을 붙여서 가변 인수로 지정해주는 것.
# 인자가 일렬로 나열되서 전달되는데, tuple 형태로 전달이 된다.

def sum(*args):
    res = 0
    for arg in args:
        res += arg
    return res

print(sum(1,2,3))
print(sum(1,2,3,4,5,6,7,15616,87489))

# 4. 위치 인자 리스트(Positional Argument Lists)
# 함수에 전달되는 매개변수 앞에 (**)을 붙여서 인자 리스트로 지정해주는 것.
# 만약, 함수를 호출했을 경우 키-값 쌍의 형태로 값이 전달되면, 딕셔너리 형태로 전달된다.

def greeting2(**kwargs):
    for name, message in kwargs.items(): #key-value = name-message
        print(f"{message}, {name}")

greeting2(Chris="hello", Bob="안녕")

def calc(a, *args):
    if a == "*":
        sum = 1
        for arg in args:
            sum *= arg
        return sum
    elif a == "+":
        sum = 0
        for arg in args:
            sum += arg
        return sum

print(calc("+",11,32,53,34,55))
print(calc("*",1,2,3,4,5,848,0))

#재귀함수(recursion function)
#1. 함수 내부에서 자기 자신 함수를 호출해야 한다.
#2. 재귀를 종료시켜주는 조건문이 존재해야 한다.

def test(end):
    if end == 0:
        return
    test(end-1)
    print(end)

test(5)

# 두 수 사이의 홀수 전부 출력
# print_odd(1,10) - 1 3 5 7 9

# 피보나치 수열 1 1 2 3 5 8 13 21 34 ...
# fibo(6) - 8

# 10진수 -> 2진수로 변환하기
# 10 - 1010
# 2 - 10
# binary(10) - 1010

# 두 수 사이의 홀수 전부 출력
# print_odd(1,10) - 1 3 5 7 9

# 피보나치 수열 1 1 2 3 5 8 13 21 34 ...
# fibo(6) - 8

# 10진수 -> 2진수로 변환하기
# 10 - 1010
# 2 - 10
# binary(10) - 1010

def print_odd(start, end):
    if start == end:
        return
    elif start%2 == 1:
        print(start)
    print_odd(start+1, end)

print_odd(100,200)

def fibo(n): # 피보나치 수열 1 1 2 3 5 8 13 21 34 ... 처음 두 개의 숫자가 1이고, 그 이후에는 앞의 두 숫자의 합
    if n == 1 or n == 2:
        return 1
    return fibo(n-2) + fibo(n-1)

#fibo(3) = fibo(1) + fibo(2)
#fibo(4) = fibo(2) + fibo(3)
#fibo(5) = fibo(3) + fibo(4)
#fibo(6) = fibo(4) + fibo(5)
#fibo(n) = fibo(n-2) + fibo(n-1)

print(fibo(6))

def binary(n):
    if n<1:
        return
    binary(n//2)
    print(n%2, end="")

# 2로 몇번 나누어지는지?
# 10 - 1010 = 1010
# 2 - 10
binary(10) #binary(5) -> binary(2) -> binary(1) -> binary(0)
print()
binary(50)
#########!!!!!!!!!!!!!!
example = [[1,2,3], [4, [5,6]], 7, [8,9]] # [1,2,3,4,[5,6],7,8,9]
# if type(data) == list:

print()
lst = [[1,2,3],[4,5,6]] #[1][3]
empty_lst = []
for i in range(len(example)): #1 -> 2 #[1,2,3], [4, [5,6]], 7, [8,9]
    if type(example[i]) == list:
        for j in range(len(example[i])): #3
            if type(example[i][j]) == list:
                for k in range(len(example[i][j])):
                    empty_lst.append(example[i][j][k])
            else:
                empty_lst.append(example[i][j])
    else:
        empty_lst.append(example[i])
print(empty_lst)

# 숙제
def flatten(data):
    flat_lst = []
    for i in data:
        if type(i) == list:

        else:

    return flat_lst

print(flatten(example)) #[1,2,3,4,5,6,7,8,9]

example = [[1,2,3], [4, [5,6,44,[6,5,67,[8,8]]]], 7, [8,9]] # [1,2,3,4,[5,6],7,8,9]
# 숙제
def flatten(data):
    flat_lst = []
    for i in data:
        if type(i) == list:
            flat_lst += flatten(i) #[1,2,3] - [4, [5,6]] - [8,9]
        else:
            flat_lst.append(i)
    return flat_lst

print(flatten(example)) #[1,2,3,4,5,6,7,8,9]