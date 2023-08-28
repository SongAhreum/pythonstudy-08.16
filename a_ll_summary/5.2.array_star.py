lst = []

for i in range(5):
    temp = ""
    for j in range(5):
        temp += "*"
    lst.append(temp)

for i in lst:
    print(i)
print(lst)

lst = ["*****" for _ in range(5)]
lst = [["*" for i in range(5)] for _ in range(5)]
lst = ["*"*5 for _ in range(5)]

for i in lst:
    print(i)
print(lst)

for i in range(5):
    for j in range(5):
        if i >= j:
            print("*", end="")
        else:
            print()
            break
print()
lst = []
for i in range(5):
    temp = ""
    for j in range(i+1):
        temp += "*"
    lst.append(temp)

for i in lst:
    print(i)
print(lst)

lst = [["*" for i in range(j+1)] for j in range(5)]
print(lst)
lst = ["*"*(i+1) for i in range(5)]

for i in lst:
    print(i)
print(lst)

lst = []
for i in range(5):
    temp = ""
    for j in range(5):
        if i==j:
            temp += "*"
            break
        else:
            temp += " " #print(" ", end="")
    lst.append(temp)

for i in lst:
    print(i)
print(lst)


lst = [" "*i + "*" for i in range(5)]

for i in lst:
    print(i)
print(lst)

#1,2,3,4,5 -> 5,4,3,2,1
for i in range(5):
    for j in range(5):
        if i <= j: #(0:0) (1:0,1) (2:0,1,2) (0:01234) (1:1234)
            print("*", end="")
        else:
            print(end = " ")
    print()

for i in range(5):
    for j in range(5):
        if i <= j: #(0:0) (1:0,1) (2:0,1,2) (0:01234) (1:1234)
            print("*", end="")
        else:
            print(end = " ")
    print()

print("---------------")
for i in range(5):
    for j in range(4, -1, -1):
        if i <= j: #(0:0) (1:0,1) (2:0,1,2) (0:01234) (1:4321)
            print("*", end="")
    print()

for i in range(5):
    for j in range(5):
        if i <= j: #(0:0) (1:0,1) (2:0,1,2) (0:01234) (1:4321)
            print("*", end="")
    print()

lst = []
for i in range(5):
    temp = ""
    for j in range(5):
        if i <= j: #(0:01234) (1:1234) (2:234)
            temp += "*"
    lst.append(temp)

for i in lst:
    print(i)
print(lst)

lst = []
for i in range(5):
    temp = ""
    for j in range(5):
        if i <= j: #(0:0) (1:0,1) (2:0,1,2) (0:01234) (1:1234)
            temp += "*"
        else:
            temp += " "
    lst.append(temp)

for i in lst:
    print(i)
print(lst)

lst = [["*" for i in range(5-j)] for j in range(5)]
lst = ["*"*(5-i) for i in range(5)]
for i in lst:
    print(i)
print(lst)


lst = [" "*i + "*"*(5-i) for i in range(5)] #(0,5) (1,4) (2,3)
for i in lst:
    print(i)
print(lst)

lst = ["*"*(i+1) for i in range(5)]

for i in reversed(lst):
    print(i)
print(lst)

lst = ["*"*(5-i)+" "*i for i in range(5)]
for i in lst:
    print(i)
print(lst)

lst = []
for i in range(5):
    temp = []
    for j in range(4, -1, -1):
        if i <= j: #(0:0) (1:0,1) (2:0,1,2) (0:01234) (1:1234)
            temp.append("*")
        else:
            temp.append(" ")
    lst.append(temp)

for i in lst:
    i.reverse()

for i in lst:
    print(i)
print(lst)