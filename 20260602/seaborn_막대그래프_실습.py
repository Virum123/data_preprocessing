import matplotlib.pyplot as plt
import pandas as pd
import seaborn
import seaborn as sns
import numpy as np

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.float_format', '{:.3f}'.format) # float 형식 소숫점 3자리


# tipsdf = sns.load_dataset('tips')
# print(tipsdf.info())

# flightsdf = sns.load_dataset('flights')
# print(flightsdf.info())
# print(flightsdf)
# pf = flightsdf.pivot_table(index='year', values='passengers', aggfunc='sum')
# print(pf)
#
# sns.barplot(data=pf, x='year', y='passengers', palette='husl', hue='year')
# plt.show()


titanicdf = sns.load_dataset('titanic')
# print(titanicdf.info())
# age 성별 기준으로 막대 그래프 시각화
# sex 컬럼명을 gender 컬럼명으로 변경

# 뭐야 결측치 제거 어떻게 해요 drop_na
#
# print(titanicdf.isnull().sum())
titanicdf.dropna(subset=["age"],inplace=True) # axis=0, how='any',
titanicdf.rename(columns={"sex":"gender"}, inplace=True)
# print(titanicdf.info())
# print(titanicdf.head())
# 젠더끼리 묶어서 fare을 값으로 넣어야하나?
ptp = titanicdf.pivot_table(index='pclass', columns='gender', values='fare', aggfunc='mean')

ptp.rename(columns={"female":"fare_female", "male":"fare_male"}, inplace=True)
ptp.columns.name = None
print(ptp)
# 이거 차라리 gender column의 내용을 fare_male/female로 바꾸고 그걸 피벗하고 그룹바이 하는게 나을 것 같은데
sns.barplot(data = titanicdf, x='pclass', y='fare', hue='gender', palette='Set3', errorbar=None)
plt.show()