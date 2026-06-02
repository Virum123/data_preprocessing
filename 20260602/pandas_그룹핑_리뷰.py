import pandas as pd
import numpy as np
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


# 엑셀 파일을 전처리해 시각화
youdf = pd.read_excel("youtube_data.xlsx", index_col=0) # DF 생성
print(youdf)
youdf.info() # 결측치 체크, 각 컬럼별 Datatype 체크
print(youdf.head())

# type = object sum하면 문자열끼리 그냥 합침, mean은 str이 아니라서 TypeError 발생
# 내 답
# def changeMan(arg1):
#     if arg1[-1] == '만':
#         return int(arg1[:-1] + '0000')
# youdf['Subscriber'] = youdf['Subscriber'].apply(changeMan)

print(youdf['Subscriber'])
# 슨상 답
import re
youdf['Subscriber'] = youdf['Subscriber'].apply(lambda x: int(re.sub(r'만','0000',x)) )
#
# youdf['Subscriber'] = youdf['Subscriber'].apply(lambda x: int(x.replace(r'만','0000',x) ) )
# youdf['Subscriber'] = youdf['Subscriber'].str(r'만','0000').astype(int64)
# youdf.info()

pvdf= youdf.pivot_table(index='Category', values='Subscriber', aggfunc='mean')
print('='*80)
# 피벗을 그룹바이로 바꾸기
grb = youdf.groupby('Category')[['Subscriber']].mean()
print(grb)
# print(pvdf.values, type(pvdf.values))
grb.sort_values(by=['Subscriber'], ascending=False, inplace=True)
grb_top7 = grb.head(7).copy()

plt.figure(figsize=(9, 7))
sns.barplot(x='Category', y='Subscriber', data=grb_top7, palette='viridis')
plt.show()