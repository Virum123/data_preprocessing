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

# tipdf = pd.read_csv('tips.csv')
#
# tipdf['tip_pct'] = tipdf['tip'] / (tipdf['total_bill']-tipdf['tip'])
# print(tipdf.head())
#
# sns.set_style('darkgrid')
# fig, axes= plt.subplots(1,2, figsize=(10,6))
#
# sns.regplot(x=tipdf['total_bill'], y=tipdf['tip'], ax=axes[0], fit_reg=True, color='orange')
# sns.regplot(x=tipdf['total_bill'], y=tipdf['tip'], ax=axes[1], fit_reg=False, color='pink')
# plt.show()

irisdf = sns.load_dataset("iris")
print(irisdf.head())
spc = irisdf['species'].unique()
# iris 데이터를 sns.lmplot으로 산점도 시각화
# 세 종류를 하나의 plot 창에 동시 시각화, fig_reg = False(회귀선 False)
# x축 ==> petal_length
# y축 ==> petal_width

sns.lmplot(data=irisdf, x='petal_length', y='petal_width', hue= 'species',fit_reg=False)
# 머신러닝? 다중분류? 뭐라노
plt.show()