x = [1,2,3]

try:
    print(10/0)
    x[5]

except ZeroDivisionError as e:
    print("숫자를 0으로 나눌 수 없음", e)

except IndexError as e:
    print("잘못된 인덱스", e)

class MyError(Exception):
    def __init__(self):
        super().__init__("나의 오류")

try:
    raise MyError
except Exception as e:
    print("예외발생", e)



class NotNumberException(Exception):
    def __init__(self):
        super().__init__("NotNumber: 잘못된 숫자입니다.")
def gugudan(n):
    if not(2 <= n <= 9):
        try:
            raise NotNumberException
        except Exception as e:
            print(e)
    else :
        for i in range(1,10):
            print("{} X {} = {}".format(n,i,n*i))

input_number = int(input())
gugudan(input_number)

# 패키지에서 디렉토리 내에 __init__.py 파일이 있어야 한다.
# 버전 업데이트 되면서 반드시 있어야 된다 -> 없어도 된다.
# 이제는 없어도 되지만, 약속

