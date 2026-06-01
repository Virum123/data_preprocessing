import numpy as np
import pandas as pd

tipdf= pd.read_csv("tips.csv")
tipdf.info()

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

tipdf = pd.read_csv("tips.csv")
print(tipdf)


# 그룹핑할 기준키는 'smoker'
# 집계(통계) 적용할 컬럼은 'total_bill, tip
# 집계 통계 함수는 mean
#==> 흡연자, 비흡연자의 'total_bill'과 'tip' 평균 계산
# df.groupby(기준키)[집계(통계)함수를 적용할 컬럼선택].함수적용할집계통계함수

grb = tipdf.groupby('smoker')[['total_bill', 'tip']].mean()
print(grb)

# 요일별 흡연자/비흡연자 tip의 평균을 계산해서 출력
# 결과는 데이터프레임으로
grb = tipdf.groupby(['day', 'smoker'])[['tip']].mean()
print(grb)

print(grb.index) # 멀티 인덱스가됨
print(grb.loc[('Sat', 'Yes')])
unctacked = grb.unstack()
print(unctacked)
print(unctacked.index)
print(unctacked.loc['Sun', ('tip', 'Yes')])