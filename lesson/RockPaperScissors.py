import random
import pickle
  


    
def play():
  try:    
    data = read_game()
    total_games = data['total_games']
    total_wins = data['total_wins']
  except FileNotFoundError:
    total_games = 0
    total_wins = 0 
  
  print(total_games,total_wins)  
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
  with open('data.txt','wb')as f:
    pickle.dump({'total_games':args[0],'total_wins':args[1]},f)
    
      
def read_game():             
  with open('data.txt','rb')as f:
    data = pickle.load(f)
  return data  
while True:
  play()