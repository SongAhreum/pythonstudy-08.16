from Food import Food
#
class Pizza(Food):
  ToppingList = {'치즈':1000,'페퍼로니':1500,'감자':1500,'올리브':1000}
  
  def __init__(self,name,price,*toppings):
    super().__init__(name,price)
    self.topping_list ={}
    
    
    self.toppingSetting(toppings)
    
    # if toppings
      
    # self.crust = []
    
  def toppingSetting(self,toppings):
    
    for t in toppings:
      
      if type(t) == list:
        self.toppingSetting(t)
        continue
      # elif type(t) == str:
        
        
      if self.topping_list.get(t) != None :
        self.topping_list[t] += self.topping_list[t] 
      else:
        price = Pizza.ToppingList[t]
        self.topping_list[t] = price
        
    
  def recipy(self): #요리방법 알아내기
    pass
  def ingredients(self): #재료
    
    pass
  
  
  def pay(self):
    price = self.price
    for i in self.topping_list.values():
      price += i
    
    print(f"총가격은 {price}입니다")
    
  
  
  def cook(self):
    print(self.name,'에서 피자가 나왔습니다.')
  
  
  def addTopping(self):
        
    for topping in Pizza.ToppingList.keys():
      print(topping,end=" ")
    print()  
    add = input('추가할 토핑을 입력하세요 : ')
    
    if self.topping_list.get(add) != None :
      self.topping_list[add] += self.topping_list[add]  
      return
    try:
      price = Pizza.ToppingList[add]
      self.topping_list[add] = price
    except KeyError as e:
      print("잘못된 입력입니다")
      self.addTopping()
    except Exception as e:
      print("error!!!!",e.__traceback__)  
    
    #토핑리스트 출력- 딕셔너리?
    #선택  
    #가격계산

p = Pizza("도미노",30000)
# p2 = Pizza("도미노",30000,'치즈','페퍼로니')
p2 = Pizza("도미노",30000,['치즈','페퍼로니'],['감자'])


# p.addTopping()
# p.addTopping()
# p.pay()
p2.pay()
