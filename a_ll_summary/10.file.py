#파일 입출력

# 1. 파일 열기(open) - 파일을 열어서 객체를 생성한다. 모드 설정(읽기, 쓰기, 추가 등)
# 2. 파일 읽기(read) or 파일 쓰기(write) - 생성된 객체를 통해서 파일을 읽거나 쓸 수 있음.
# 3. 파일 닫기(close) - 파일 사용이 끝나면 반드시 닫아줘야 한다. 파일을 닫지 않으면, 메모리에 남아있어서 데이터 손실의 위험이 있다.

file = open("example.txt", "w")
file.write("안녕하세요.\n 파일 입출력 시간입니다.")
file.close()

file = open("example.txt", "r")
res = file.read()
for i in res:
    print(i, end="")
    if(i == '.'):
        print()
file.close()

with open("example.txt", "r") as file:
    res = file.read()
    print(res)

# read() : 파일의 전체 내용을 문자열로 반환
# readline() : 파일에서 한 줄씩 문자열로 읽어옵니다.
# readlines() : 파일의 전체 내용을 한 줄씩 읽어와서 각각 리스트로 만들어서 반환

with open("alice.txt", "r") as f:
    line = f.readline()

    while line:
        # print(line.strip()) #print(line, end="")
        line = f.readline()

with open("alice.txt", "r") as f:
    line = f.readlines()
    for i in line:
        print(i.strip())
    print(len(line))

# 모드
# "r" : 읽기 모드
# "w" : 쓰기 모드 (이전에 데이터를 모두 삭제하고 새로 적는다.)
# "x" : 생성 모드 (파일을 생성해주는 모드, 이미 파일이 있으면 에러)
# "a" : 추가 모드 (파일에 데이터를 추가하기 위해 사용된다. 해당 파일이 이미 존재한다면, 기존의 데이터 뒤에 새로운 데이터를 추가한다.)
# "b" : 바이너리 모드 (바이너리 데이터를 사용하기 위해)
# "t" : 텍스트 모드 (텍스트 데이터를 다루기 위해 사용됨. (기본값)) 생략가능.
# "r+" : 파일 읽기 쓰기를 모두 사용할 수 있는 모드

# "rb" : 읽기 모드
# "wb" : 쓰기 모드

# "ab" : 추가 모드
# "xtb" : 생성 모드
# "rb+", "wb+", "ab+" : 읽기 쓰기 모드
    
    
    
    
# 다이어리 프로그램 - 날짜를 입력하고, 일기 작성, 날짜를 입력해서 작성한 일기를 출력

def menu():
    print("1. Write a diary")
    print("2. Read a diary")
    choice = int(input("어느 것을 하시겠습니까?"))

    if choice == 1:
        write_diary()
    elif choice == 2:
        read_diary()

def write_diary():
    date = input("날짜를 입력하세요 (dd-mm-yyyy):")
    text = input("오늘 하루는 어땠나요 : ")

    with open(f"{date}.txt", "w") as f:
        f.write(text)

    print("저장이 완료되었습니다.")

def read_diary():
    view = input("보고 싶은 다이어리의 날짜를 입력해주세요 (dd-mm-yyyy):")

    try :
        with open(f"{view}.txt","r") as f:
            res = f.read()

        print(res)

    except FileNotFoundError:
        print("해당 날짜의 다이어리를 찾을 수 없습니다 ㅠ")

# while True:
#     menu()
###################################
# pickle 모듈
import pickle
# 파이썬에 딕셔너리, 리스트, 클래스 - 자료구조, 객체 등을 자료형 변환 없이 그대로 파일에 저장하고 싶을 때 사용한다.
# 인수가 여러 개일떄, 게시판(1.글 번호, 2. 글 제목, 3. 글 내용)

data = {"no": 1, "title": "제목", "content": "내용"}

print(data["no"])

with open('data.p', 'wb') as f:
    pickle.dump(data, f)

d = dict()
with open('data.p', 'rb') as f:
    d = pickle.load(f)

print(d)

# 가위바위보 게임
import random

def play():
    total_game, win_game = read_game().split(',')
    win = 0
    print(f"TOTAL : {total_game}, WIN : {win_game}")

    user = int(input("1. 가위, 2. 바위, 3. 보를 입력하세요 : "))
    com = random.randrange(1,4)

    print()
    if user == com:
        print("무승부")

    if user == 1:
        if com == 2:
            print("패배")
        elif com == 3:
            print("승리")
            win += 1

    if user == 2:
        if com == 1:
            print("승리")
            win += 1
        elif com == 3:
            print("패배")

    if user == 3:
        if com == 1:
            print("패배")
        elif com == 2:
            print("승리")
            win += 1

    write_game(int(total_game)+1, int(win_game)+win)

def write_game(total, win):
    with open("game.txt", 'w') as f:
        f.write(str(total)+","+str(win)) #111

def read_game():
    try:
        with open("game.txt", 'r') as f:
            contents = f.read()
    except:
        #return "0,0"
        with open("game.txt", 'w') as f:
            f.write("0,0")
            contents = "0,0"
    return contents

# while True:
#     play()
    
    
#######################################################   
#실습 02 - 숙제
import pickle

def menu():
    user = int(input("메뉴를 선택해주세요 (1-입력, 2-조회, 3-삭제, 0-종료):"))

    if user == 1:
        name = input("이름:")
        math = input("수학:")
        science = input("과학:")
        english = input("영어:")
        write_user(name, math, science, english)

    elif user == 2:
        load_user()

    elif user == 3:
        load_user()
        delete = int(input("삭제할 번호를 입력해주세요 : "))
        delete_user(delete)

    elif user == 0:
        print("종료되었습니다.")
        return -1
    return 0

def write_user(name, math, science, english):
    dic = {"이름":name, "수학":math, "과학": science, "영어": english}
def load_user():
    print()

def delete_user(delete):
    print("삭제가 완료되었습니다.")

while True:
    if menu() == -1:
        break  
      
####################################        
Class01.py
#실습 02 - 숙제
import pickle

def menu():
    user = int(input("메뉴를 선택해주세요 (1-입력, 2-조회, 3-삭제, 0-종료):"))

    if user == 1:
        name = input("이름:")
        math = input("수학:")
        science = input("과학:")
        english = input("영어:")
        write_user(name, math, science, english)

    elif user == 2:
        load_user()

    elif user == 3:
        load_user()
        delete = int(input("삭제할 번호를 입력해주세요 : "))
        delete_user(delete)

    elif user == 0:
        print("종료되었습니다.")
        return -1
    return 0

def write_user(name, math, science, english):
    dic = {"이름":name, "수학":math, "과학": science, "영어": english}
    lst = []
    with open('data.p', 'rb') as f:
        item = pickle.load(f)

    if item != "":
        if type(item) == dict:
          lst.append(item)
        elif type(item) == list:
          lst += item

    lst.append(dic)
    with open('data.p', 'wb') as f:
        pickle.dump(lst, f)
def load_user():
    with open('data.p', 'rb') as f:
        data = pickle.load(f)

    for i in range(len(data)):
        # print(data[i])
        print(f'[{i}] 이름 : {data[i]["이름"]}, 수학 : {data[i]["수학"]}, 과학 : {data[i]["과학"]}, 영어 : {data[i]["영어"]}')

def delete_user(delete):
    with open('data.p', 'rb') as f:
        lst = pickle.load(f)

    if delete < 0 or delete >= len(lst):
        print("잘못된 입력입니다. 삭제할 수 없습니다.")
        return

    lst.pop(delete)

    with open('data.p', 'wb') as f:
        pickle.dump(lst, f)

    print("삭제가 완료되었습니다.")

try:
    with open('data.p', 'rb') as f:
        pickle.load(f)
except:
    with open('data.p', 'wb') as f:
        pickle.dump("", f)

while True:
    if menu() == -1:
        break