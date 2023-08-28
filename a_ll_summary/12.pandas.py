# Pandas
# 데이터 분석 및 조작을 위한 라이브러리 (Numpy 기반)
import numpy as np
import pandas as pd

# Series : 1차원 배열 구조
# DataFrame : 2차원 배열 구조

# CSV, Excel, SQL 쿼리

# Series
s = pd.Series([1,3,4, np.nan, 6, 8])
print(s)
print(s[3])

s = pd.Series([1,3,4, np.nan, 6,8], index=['A','B','C','D','E', 'F'])
print(s)
print(s['C'])

# DataFrame
data = {
    'Name':['짱구', '철수', '훈이'],
    'Age':[5,5,5]
}

df = pd.DataFrame(data)

print(df)
print('----------------------')
print(df['Name'])
print('----------------------')
print(df.loc[0]) # 이름
print('----------------------')
print(df.iloc[0]) # 위치

import pandas as pd
import numpy as np

data = {
    'Name':['John', 'Anna', 'Peter', 'Linda'],
    'Age':[28,24,35,32],
    'City':['New York', "Paris", "Berlin", "London"]
}

# 1. 도시 기준으로 정렬
# 2. 평균 나이 구하기
# 3. 이름이 Peter인 사람의 나이 출력
# 4. 가장 나이가 많은 사람이 살고 있는 이름, 도시 출력해보기
df = pd.DataFrame(data)
df = df.sort_values('City')
print(df)
print(df['Age'].mean())
print(df[df['Name']=='Peter']['Age'].values)
oldest = df.loc[df['Age'].idxmax()]
print(oldest[['Name','City']])

# 모든 사람의 이름을 대문자로 변경하기
df['Name'] = df['Name'].str.upper()
print(df)
# 나이가 30 이상인 사람들만 선택하기
older_than_30 = df[df['Age']>=30]
print(older_than_30)

# 각 도시별로 몇명이 살고 있는지 계산하기
city_counts = df['City'].value_counts()
print(city_counts)

# Gender라는 새로운 열을 추가해서 임의 성별 할당하기
np.random.seed(0)
df['Gender'] = np.random.choice(['Male', 'Female'], size=df.shape[0])
print(df)

import pandas as pd
import numpy as np

# 1000명의 사람 데이터 만들기
# 이름 : Person_1, Person_2, ... Person_1000
# 나이 : 20 ~ 60 랜덤
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo
np.random.seed(0)
data = pd.DataFrame({
    'Name': ['Person_' + str(i) for i in range(1, 1001)],
    'Age': np.random.randint(20, 60, 1000),
    'City': np.random.choice(["New York", "Paris", "Berlin", "London", "Seoul", 'Tokyo'], 1000)
})

print(data)
# 도시별 평균 나이 구하기
# 가장 많은 사람이 살고 있는 도시
# 연봉 추가해서 랜덤으로 할당 ex) $50,000 ~ $150,000
# 연봉 순서대로 정렬한 후 연봉 1등과 꼴등 출력해보기

import pandas as pd
import numpy as np

data = {
    'Name':['John', 'Anna', 'Peter', 'Linda'],
    'Age':[28,24,35,32],
    'City':['New York', "Paris", "Berlin", "London"]
}

df = pd.DataFrame(data)
df = df.sort_values('City', ascending=False)

# groupby : 데이터 특정 조건에 다라 그룹으로 분류하는 함수

data = pd.DataFrame({
    'City': ['Seoul', 'Seoul', 'Busan', 'Busan'],
    'Fruit': ['Apple', 'Banana', 'Apple', 'Banana'],
    'Quantity': [10, 15, 7, 12],
    'Price': [1000, 2000, 1500, 2500]
})

group = data.groupby(['City','Fruit'])['Quantity'].sum()

print(group)


# 데이터 통합
# 여러개의 데이터셋을 결합해서 단일 데이터 셋으로 만든다.
import pandas as pd

# concat
# 동일한 열 이름을 가진 여러 데이터프레임을 행 방향(axis = 0)나 열 방향(axis = 1)로 결합할 때 사용한다.

df1 = pd.DataFrame({'A':['A0','A1'], 'B':['B0', 'B1']})
df2 = pd.DataFrame({'A':['A2','A3'], 'B':['B2', 'B3']})

row = pd.concat([df1,df2], ignore_index=True)

print(row)

column = pd.concat([df1, df2], axis=1)

print(column)

# merge
# 공통된 열 혹은 인덱스 기준으로 통합된다.

df1 = pd.DataFrame({'Name':['John', 'Anna', 'Peter'], 'Age':[28,24,36]})
df2 = pd.DataFrame({'Name':['John', 'Anna', 'Peter'], 'City':['New York','Paris','Seoul']})

res = pd.merge(df1, df2, on='Name')
print(res)

# join
# 인덱스 기반 결합 작업, 왼쪽으로 조인, how(내부inner, 외부outer, 왼쪽left, 오른쪽right)
df1 = pd.DataFrame({'A':['A0', 'A1', 'A2']}, index=['I', 'J', 'K'])
df2 = pd.DataFrame({'B':['B0', 'B1', 'B2']}, index=['I', 'J', 'K'])

res = df1.join(df2)
print(res)


import pandas as pd
import numpy as np

# 1000명의 사람 데이터 만들기
# 1번 데이터셋
# ID : ID_1, ID_2, ... ID_1000
# 나이 : 20 ~ 60 랜덤
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo

# 2번 데이터셋
# ID : ID_1, ID_2, ... ID_1000
# 연봉 : 랜덤

# 3번 데이터셋
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo
# 나라 : 특정 도시의 나라 ex) USA, France, Germany, UK, Korea, Japan

# 1. 1번 데이터셋과 2번 데이터셋 병합 (ID 기준)
# 2. 병합된 데이터에 City를 기준으로 병합
# 3. 각 나라별 평균 연봉
# 4. 제일 연봉이 높은 사람 어느 나라 사람인지?