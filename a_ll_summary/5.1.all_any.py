#all함수 any함수
#여러 개의 조건 or 값이 있는 리스트, 튜플, set... 값의 조건에 따라 True or False 리턴하는 함수

#all함수 : 모든 값이 True일 때, True
#any함수 : 하나라도 True면 True 리턴한다.

number = [i+1 for i in range(10)] # 1...10
lst = [x for x in number if x % 2 == 0]

#all
res = all(x%2 == 0 for x in number)
print(res)

res = all(x%2 == 0 for x in lst)
print(res)

#any
res = any(x == 5 for x in number)
print(res)

res = any(x == 5 for x in lst)
print(res)

prime_number = [i for i in range(2, 101) if all(i%j !=0 for j in range(2, i))]
print(prime_number)

##########
person1 = ["치킨", "피자", "족발", "삼겹살"]
person2 = ["김밥", "김치찌개", "삼겹살", "쌈밥"]
person3 = ["치킨", "김치찌개", "떡볶이", "초밥", "삼겹살", "족발", "햄버거", "보쌈", "한우", "아이스크림"]

# all, any를 사용하여 공통된 음식 찾기 일단 두명부터
res = any(food in person2 for food in person1)
common_foods = [food for food in person1 if any(food == food2 for food2 in person2)]

print(res)
print(common_foods)

lst = [food for food in common_foods if any(food==food3 for food3 in person3)]
print(lst)
