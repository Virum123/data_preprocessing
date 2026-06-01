import numpy as np
import pandas as pd

tipdf= pd.read_csv("tips.csv") # csv파일을 읽어서 Dataframe 객체로 생성
print(tipdf)
tipdf.info()
print(tipdf.head())
# 특정 컬럼 데이터의 속성이 뭐가 있고 몇 개가 있는지 체크할때 ==> unique()
print(tipdf['gender'].unique())
tipdf['gender'] = tipdf['gender'].map({'Female':1, 'Male':0}) # 새로 생성된데이터를 기존 데이터에 업데이트
print(tipdf['gender'])

# total_bill 컬럼 기준 상위 5개만 추출
# 특정 컬럼데이터 기준 정렬 ==> sort_values
# by= : 정리할 기준 컬럼
# ascending = : 오름차순, 내림차순 정렬
tipdf.sort_values(by=['total_bill', 'tip'], ascending = False, inplace=True)

tipdf_top5 = tipdf.head(5).copy
print(tipdf_top5)

# 특정 컬럼데이터의 데이터항목의 개수를 파악
day_cnt = tipdf['day'] .value_counts() # 시리즈랑 데이터 프레임을 구분하자. 일단 잘 하긴 하는듯
print(day_cnt)
day_cnt_df = pd.DataFrame(day_cnt)
print(day_cnt_df)

# time 컬럼의 데이터가lunch 인 행만 추출 ==> is in(): 불린 배열

tipdf['time'] == 'Lunch' # 하나만 이렇게도 ㄱㅊ 근데 여러개면 귀찮아짐
time_bool = tipdf['time'].isin(['Lunch']) # 항목이 하나더라도 리스트로 줘야함 그렇지 않으면 오류
#불린배열 사용
# tipdf.loc[ 불린배열, ㅣ]
subset = tipdf.loc[ time_bool, 'tip':'time'] # 컬럼 슬라이싱
print(subset)