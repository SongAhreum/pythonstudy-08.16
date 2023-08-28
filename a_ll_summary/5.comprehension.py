# 100이하의 소수(약수가 1과 자기자신)으로 이루어진 1차원 리스트 컴프리헨션으로 만들기
prime_number = []

for i in range(2, 101):
    for j in range(2, i):
        if i%j == 0:
            break
        elif i-1 == j :
            prime_number.append(i)

print(prime_number)

prime_number = []

for i in range(2, 101):
    isPrime = True
    for j in range(2, i):
        if i%j == 0:
            isPrime = False
            break
    if isPrime :
        prime_number.append(i)

print(prime_number)

#두 개의 리스트 곱하기
a = [[10,20],[30,40],[50,60]]
b = [[2,3],[4,5],[6,7]]

# [[1,2],[3,4],[5,6]] 리스트 컴프리헨션으로 만들기

# 2차원 10x10 리스트 0으로 채우기 컴프리헨션으로 만들기

# 100이하의 소수(약수가 1과 자기자신)으로 이루어진 1차원 리스트 컴프리헨션으로 만들기