# Numpy (Numerical Python)
# 과학, 공학 연산을 쉽게 하도록 지원하는 다차원 배열(multi-dimensional array) 라이브러리
# Numpy를 사용해서 대규모 배열 처리를 쉽게 하도록 하고, 파이썬 List 와는 차이가 있다.

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6]])

print(a)
print(b)

# 내부에 연속된 메모리 구조를 가지고 (Array Interface)를 가지고 있고, C를 통해 연산된다.

# 생성 함수 : np.array(), np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()
# 변환 함수 : ndarray.reshape(), ndarray.ravel(), ndarray.transpose(), ndarray.swapaxes()
# 연산 함수 : np.add(), np.substract(), np.multiply(), np.divide(), np.sqrt(), np.dot(), np.sum()
#               np.mean(), np.std(), np.max(), np.min(), np.argmax(), np.argmin()
# 집계 함수 : ndarray.sum(), ndarray.mean(), ndarray.std(), ndarray.max(), ndarray.min(),
#               ndarray.argmax(), ndarray.argmin()
# 논리 함수 : np.logical_and(), np.logical_or(), np.logical_not()


# 2차원 배열에서 각 행과 각 열의 합을 구해보기
import numpy as np
# 1 2 3
# 4 5 6
# 7 8 9
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
# 6 15 24
# 12 15 18

for i in range(len(arr)):
    print(arr[i].sum(), end=" ")
print()

for i in arr:
    print(i.sum(), end=" ")
print()

print(arr.transpose())

for i in arr.transpose():
    print(i.sum(), end=" ")
print()

print(arr)
print(arr.sum(axis=None))
print(arr.sum(axis=0))
print(arr.sum(axis=1))


import numpy as np

arr = np.random.rand(3,3)
print(arr)
print(np.sort(arr))

#숙제3. 10X10 배열에서 서로 다른 두 원소를 선택해서 두 원소의 차이의 절대값이 가장 작은 두 원소를 찾아보기

arr = np.random.rand(10,10)
arr = arr.flatten()
print(arr.max() - arr.min())
sorted_arr = np.sort(arr)

print(sorted_arr)
print(sorted_arr[sorted_arr.argmax()] - sorted_arr[sorted_arr.argmin()])

min = sorted_arr[sorted_arr.argmax()] - sorted_arr[sorted_arr.argmin()]
min_index = 0
for i in range(len(sorted_arr)-1):
    diff = abs(sorted_arr[i] - sorted_arr[i+1])

    if diff < 0:
        diff *= -1

    if diff < min:
        min = diff
        min_index = i

print(f"첫번째 원소 : {sorted_arr[min_index]}, 두번째 원소 : {sorted_arr[min_index+1]}, 최소값 : {min}")