import pandas as pd
import numpy as np

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

# tips.csv 파일을 읽어서 male 을 0으로, female을 1로 일괄 변경하기
tipsdf = pd.read_csv('tips.csv', encoding='cp949')
print(tipsdf)


def dataselect(arg):
    #print(arg)
    if arg == 'Male':
        return 0
    elif arg == 'Female':
        return 1

tipsdf['gender']=tipsdf['gender'].apply(dataselect) # 함수명만 적어야 호출임

print(tipsdf)

# day 컬럼 데이터중 몇 개의 요일이 있는지 체크하기
# 이거 그냥 유니크로 던지고 countd 해버리면 되지 않나?
print(len(tipsdf['day'].unique()))

# 요일이 Sat or Thur 인 항목만 출력

def dayselect(arg):
    #print(arg)
    if arg == 'Sat' or arg == 'Thur':
        return True
    else:
        return False
dd = tipsdf['day'].apply(dayselect)  # 함수명만 적어야 호출임

set = tipsdf.loc[dd, :].copy
print(set)
print( subset['size'].mean() ) # 평균 집계함수를 제공함