import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
import seaborn as sns # 씨본 라이브러리 이용한 시각화
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

df = pd.read_excel('국소마취제_groupby.xlsx')
print(df.info())
print(df.head(10))

# 상병명 기준으로 금액이 가장 큰 상위 top 5개만 추출

pdf = df.pivot_table(index='상병명', values='금액', aggfunc='sum')
pdf = pdf.sort_values('금액', ascending=False)
five = pdf.head(5)
print(five)

# seaborn 라이브러리 이용해서 막대 차트 시각화

sns.barplot(five, x='상병명', y='금액', palette=sns.color_palette('muted'))
plt.show()