from tkinter.constants import LEFT

import pandas as pd
import numpy as np

df1 = pd.DataFrame({"customid":[1234,5678,1111,888,3333], 'name':['Han', 'Hong', 'Park', "Lee","Song"]})
print(df1)

df2 = pd.DataFrame({"customid":[1234,5678,1111,777, 3333], 'consume':[3000, 4000,33333 ,2500,9000]})
print(df2)

# 특정 키 기준으로 두 데이터프레임을 변합할때 사용하는 메서드 ==> merge()
# 동일 키가 없다면 오류가 난다.
# 기본값은 inner join이다 ==> 두 데이터프레임의 병합할 기준 키 데이터중 둘 다 있는 키 데이터만 병합
# inner/outer 로 나누는듯
# left, right 도 사용가능
mdf = pd.merge(df1, df2, how='outer')
print(mdf)

# 만약 동일 키가 없다면?
df3 = pd.DataFrame({"customod":[1234,5678,1111,888,3333], 'name':['Han', 'Hong', 'Park', "Lee","Song"]})

mergedf = pd.merge(df3, df2, left_on='customod', right_on='customid')
print(mergedf)
# 서로 다른 부서에서 다른 엑셀작업할때 정도? 잘 쓰지는 않음, 데이터량이 많으면 인덱스 따로 달아서 넣으면 오래걸리긴 하겠다
# 알고 있자 정도로 알아둡시다.

# 특정 데이터프레임을 병합할 때 ===> merge(), concat

arr1 = np.array([ [1,2,3], [4,5,6] ])
print(arr1)

arr2 = np.array([ [5,6,7], [14,15,16] ])
print(arr2)

conarr = np.concatenate([arr1, arr2], axis=0) # 넘파이 배열을 축 기준으로 병합하는 메서드
# 기본값이 axis=0, 1은 열축
print(conarr)