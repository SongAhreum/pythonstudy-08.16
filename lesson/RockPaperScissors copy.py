import random
import pickle
  
######file로만들어보기

    
def play():

  try:    
    
    total_games, total_wins = read_game()
    # data = data.replace(','," ").replace(':'," ") ????????
    # data = data.replace(","," ")
    # data = data.replace(":"," ")
    # print(data)
    # datas = data.split(" ")   
    # total_games = int(datas[1])
    # total_wins = int(datas[3])
  except FileNotFoundError:
    total_games = 0
    total_wins = 0 
  
  # print(total_games,total_wins)  
  user= input("가위(1), 바위(2), 보(3) 중 선택하세요: ")
  if user in ['1', '2', '3']:
      user = int(user)
      computer = random.randint(1, 3)

      if user == computer:
          print("비겼습니다!")
      elif (user == 1 and computer == 3) or \
            (user == 2 and computer == 1) or \
            (user == 3 and computer == 2):
          print("이겼습니다!")
          total_wins += 1
      else:
          print("졌습니다!")

      total_games += 1
      save_data(total_games,total_wins)
  else:
      print("1, 2, 3 중에서 선택해주세요.")
            
def save_data(*args):
  with open('data2.txt','w')as f:
    f.write(f'total_games:{args[0]},total_wins:{args[1]}')
    
      
def read_game():             
  with open('data2.txt','r')as f:
    data = f.read()
    args = data.split(',')
    total_games = int(args[0].split(":")[1])
    total_wins = int(args[1].split(":")[1])
  return total_games ,total_wins  
while True:
  play()