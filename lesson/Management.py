import pickle

def score_management():
  
  n = input('메뉴를 선택해주세요 1 - 입력, 2 - 조회, 3 - 삭제, 0 - 종료')

  if n == '1':
    score_list = []
    try:      
      with open('score.txt',"rb") as f:
        data = pickle.load(f)
        if type(data) == dict:
          score_list.append(data)
        elif type(data) == list:
          score_list += data        
    except FileNotFoundError:
      score_list = []
    score = {'이름':input('이름 : '),'수학':input('수학 : '),'과학':input('과학 : '),'영어':input('영어 : ')}
    score_list.append(score)
    with open('score.txt',"wb") as f: 
      pickle.dump(score_list,f) 
  elif n == '2':
    with open('score.txt',"rb") as f:
      scores = pickle.load(f)     
      for i in range(len(scores)):
        print(f"[{i}] 이름 : {scores[i].get('이름')}, 수학 : {scores[i].get('수학')}, 과학 : {scores[i].get('과학')}, 영어 : {scores[i].get('영어')}") 
      
    
  elif n == '3':
    with open('score.txt',"rb") as f:
      scores = pickle.load(f)
      for i in range(len(scores)):
        print(f"[{i}] 이름 : {scores[i].get('이름')}, 수학 : {scores[i].get('수학')}, 과학 : {scores[i].get('과학')}, 영어 : {scores[i].get('영어')}") 
      num = int(input('삭제할 번호를 입력해주세요'))
      try :
        if num >= 0 or num < len(scores):
          scores.pop(num)
          with open('score.txt', 'wb') as f:
            pickle.dump(scores, f)
          print('삭제되었습니다.')
      except IndexError: 
        print('잘못입력')
      # else:
      #   print('유효한 번호를 입력godi.')
  elif n == '0':
    print('종료')
    return 0   
  else:
    score_management() 

while True: 
  if 0 == score_management():
    break    