'''
예외처리
'''

class NotNumberException(Exception):
  def __init__(self):
    super().__init__("NotNumber, 잘못된숫자입니다")
    
def gugudan(n):
  if type(n) != int or (n >1 and n <=9):
    try: 
      raise NotNumberException
    except NotNumberException as e:
      print('!',e.__traceback__)
        
gugudan(10)

'''
from import
'''
# 패키지에서 디랙토리내에 __init__.py파일이 있어야한다
# 버전업데이트되면서 현재는 없어도되지만 버전에 맞춰서 개발할 것



'''
데코레이터

코드를 수정하지 않고 함수 메서드 동작을 변경하거나 확장하고 싶을때 사용한다
일반적으로 함수를 다른 함수에 매개변수로 전달하는 것 처럼 구현된다.
'''

#데코레이터 함수 래퍼함수
#데코레이터 함수생성(매개변수로 다른함수를 받는다)
#데코레이터 함수 내부에 래퍼 함수를 만든다
#래퍼 함수가 함수의 동작을 변경, 확장해 줄 수 있다.

def log_decorator(func):
  
  def wrapper(*args,**kewards):
    print(func.__name__,'함수 실행전')
    result= func(*args,**kewards)
    print(func.__name__,'함수 실행후')

    return result
  return wrapper

@log_decorator
def function():
  print('데코레이터 함수실행')
  
function()


'''
일급객체,일급함수

  -일급객체조건
    변수에 저장할 수 있다
    인수로 전달 할 수 있다
    반환값으로 사용할 수 있다.
    자료구조 내부에 넣을 수 있다
  -일급함수
    파이썬에서는 함수가 일급객체다
    함수에 변수를 할당 할 수 있고 인수를 전달하고 반환할 수 있다.  
    
'''  

'''
클로저 closure
  함수내부에서 정의된 함수에서 외부함수의 변수를 참소하거나 변경을 하고,
  외부함수가 종료된 후에도 해당 변수값을 유지할 수 있게  해주는 함수 
'''

def outer(x):
  def inner(y):
    return x+y
  return inner
a = outer(5)
res = a(3)

print(res)