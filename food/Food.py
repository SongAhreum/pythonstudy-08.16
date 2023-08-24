#추상클래스
from abc import *
class Food(metaclass=ABCMeta):
  # name = "음식이름"
  # price = 0
  def __init__(self,name,price):
    self.name = name
    self.price = price
  @abstractmethod
  def recipy(self):
    pass
  @abstractmethod
  def ingredients(self):
    pass
  @abstractmethod
  def pay(self):
    pass