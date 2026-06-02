import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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

fishdf = pd.read_csv('Fish.csv')
print(fishdf)
print(fishdf.info())
print(fishdf['Species'].unique())
print(fishdf.head())
# fishdf = fishdf[['Species', 'Weight', 'Length1']].copy()
#
# fishdf.rename(columns={'Length1':'Length'}, inplace=True)
# print(fishdf.head())
#
# # plt.scatter() # 산점도
# # x 축을 Length
# # y 축을 Weight 로 설정해서 산점도 출력
# # plt.scatter(x=fishdf['Length'], y=fishdf['Weight'], c= 'black',alpha=0.1)
# # plt.show()
#
# sns.set_theme()
#
# # Load the penguins dataset
#
#
# # Plot sepal width as a function of sepal_length across days
# g = sns.lmplot(
#     data=fishdf, x="Length", y="Weight", hue="Species", fit_reg=False,
# )
# plt.show()

del fishdf['Length2']
del fishdf['Length3']
fishdf.rename(columns={'Length1':'Length'}, inplace=True)
print(fishdf.head())

# 각 종별 Height, Width의 평균을 계산해서 출력

fps = fishdf.pivot_table(index='Species',  values=['Height','Width'], aggfunc='mean')
print(fps)

# Height, Width 각 컬럼별 평균 에 5씩 더하기
# ==> 함수 적용 방법을 활용하되 lambda 표현식 활용
# 내 정답
# fps['Height']=fps['Height'] + 5
# fps['Width']=fps['Width'] + 5
# fps['Height'] = fps['Height'].apply(lambda x: x + 5)
# fps['Width'] = fps['Width'].apply(lambda x: x + 5)
# 굳이 둘이 한 번에 하고 싶으면
# fps[['Height', 'Width']] = fps[['Height', 'Width']] + 5 이게 제일 낫단다

fps = fps.map(lambda x: x+5)

print(fps)