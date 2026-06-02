import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.float_format', '{:.3f}'.format) # float 형식 소숫점 3자리

tipdf = pd.read_csv("tips.csv")
print(tipdf.head())
print(tipdf['time'].unique())

sns.barplot(x='size', y='total_bill', data=tipdf, hue='time')
plt.show() 