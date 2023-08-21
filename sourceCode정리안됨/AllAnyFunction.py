lst = [1,2,3,1,4,2,1]

def allIndx(lst ,n):
  res =[]
  for i in range(len(lst)):
    if n == lst[i]:
      res.append(i)
  return res    

print(allIndx(lst,1))
print(allIndx(lst,2))
print(allIndx(lst,3))

person1 ={"치킨","피자","족발","삼겹살"}
person2 ={"김밥","김치찌개","삼겹살","쌈밥"}
person3 ={"치킨","김치찌개","떡볶이","초밥","삼겹살","족발","햄버거","보쌈","한우","아이스크림"}

#all any써서 공통음식 찾기 두명부터
#########################################
res = any(food in person2 for food in person1)
common_food = [food for food in person1 if any(food == food2 for food2 in person2)]
# list = [food for food in common_food if food in person3]
lists = [food for food in common_food if any(food == food3 for food3 in person3)]
