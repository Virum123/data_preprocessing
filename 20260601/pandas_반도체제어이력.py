import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)


df= pd.read_excel("반도체_제어_이력.xlsx")
print(df.info())
print(df.columns)
# '공정 단계', '장비명', 파라미터 목표값 실제값 5개 컬럼만 선택 추출
print(df.index)
semidf= df[ ['공정 단계', '장비명', '파라미터', '목표값', '실제값'] ].copy()
print(semidf)

# 1 문제) 장비명에 숫자 문자가 있는 장비명 행만 추출(선택)
# subset = semidf.loc[ semidf['장비명'].apply(lambda x: True if len( re.findall(r'[0-9]+', x) ) > 0 else False) ]
# print(subset)
# 보통 함수로 쓰는게 훨씬 안정적이고 읽기도 쉬움
# 가끔 람다로 넣는 사람 있어서 예시로 든 것
def dataselect(arg):
    #print(arg)
    if len(re.findall(r'[0-9]+',arg)) >0:
        return True
    else:
        return False
sub=semidf['장비명'].apply(dataselect) # 함수명만 적어야 호출임

set = semidf.loc[sub,:]
print(set)


# 2 문제) 공정단계중 가장 많은 공정단계는 무엇인가요?
print(semidf.value_counts('공정 단계')) # CMP

# 3. 공정 단계별 목표값 실제값의 평균을 계산해서 출력
# semidf['목표값'] = semidf['목표값'].astype('float')
# semidf['실제값'] = semidf['실제값'].astype('float')
grb = semidf.groupby('공정 단계')[[ '목표값', '실제값']].mean()
print(grb)
