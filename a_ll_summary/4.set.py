#SET
# 1. 사람 3명이 각각 먹고 싶은 여러 개 음식이 있다라고 할 때, 어떤 메뉴를 시키는게 가장 좋을지 (교집합)
person1 = ["치킨", "피자", "족발", "삼겹살"]
person2 = ["김밥", "김치찌개", "삼겹살", "쌈밥"]
person3 = ["치킨", "김치찌개", "떡볶이", "초밥", "삼겹살", "족발", "햄버거", "보쌈", "한우", "아이스크림"]

menu1 = set(person1)
menu2 = set(person2)
menu3 = set(person3)

print(menu1 & menu2 & menu3) #set()
print((menu1 & menu2) | (menu1 & menu3) | (menu2 & menu3))

#리스트 상태에서 3명의 공통 음식 찾기 - 숙제

# 2. 사람 3명이 각각 음식을 여러 개 가지고 있다고 할 때, 두 명이 서로 음식을 교환해보자 (이미 갖고 있는 음식에 대한 교환 X)

while True:
    print(menu1)
    print(menu2)
    print(menu3)
    inputSet = int(input("1. 교환하기, 2. 종료하기"))

    if inputSet == 1:
        inputSet = int(input("누구와 교환하시겠습니까? 2.person2 3.person3"))
        if inputSet == 2 :
            myFood = (input("어떤 음식을 교환하시겠습니까? "))
            yourFood = (input("어떤 음식과 교환하시겠습니까? "))
            if myFood in menu2 or yourFood in menu1:
                print('이미 가지고 있는 음식입니다. 교환할 수 없습니다.')
            elif myFood in menu1 and yourFood in menu2:
                menu1.add(yourFood)
                menu2.remove(yourFood)
                menu1.remove(myFood)
                menu2.add(myFood)
            else :
                print('가지고 있는 음식이 아닙니다. 교환할 수 없습니다.')
        elif inputSet == 3 :
            myFood = (input("어떤 음식을 교환하시겠습니까? "))
            yourFood = (input("어떤 음식과 교환하시겠습니까? "))
            if myFood in menu3 or yourFood in menu1:
                print('이미 가지고 있는 음식입니다. 교환할 수 없습니다.')
            elif myFood in menu1 and yourFood in menu3:
                menu1.add(yourFood)
                menu3.remove(yourFood)
                menu1.remove(myFood)
                menu3.add(myFood)
            else:
                print('가지고 있는 음식이 아닙니다. 교환할 수 없습니다.')
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")

    elif inputSet == 2 :
        break
    else :
        print("잘못된 입력입니다. 다시 입력하세요.")