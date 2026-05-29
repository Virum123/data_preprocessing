import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import platform

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

youdf = pd.read_excel("youtube_rank_1000_First_Name.xlsx", index_col=0)
print(youdf.head(30))

# 데이터중에 Category 가 가장 많은 것이 무엇입니까?
ds = youdf['Category'].value_counts()
# Series ==> Dataframe 객체로 변환
df = pd.DataFrame(ds)
df.index.name=''
print(df)

#count 컬럼명을 카테고리 개수로 수정
df.rename(columns={'count':'카테고리개수'}, inplace=True)
dtop5 = df.head(5).copy()
print(dtop5)
dtop5.info()
numc = dtop5['카테고리개수']
plt.pie(dtop5['카테고리개수'], labels=dtop5.index, autopct='%.1f%%', startangle=90, explode = [0.05] * 5, colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown', 'cyan'])
plt.show()
