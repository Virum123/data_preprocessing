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
tipdf['tip_pct'] = tipdf['tip'] / (tipdf['total_bill']-tipdf['tip'])
tipdf.info()

fig, axes = plt.subplots(3,1, figsize=(10,10))
sns.histplot(data=tipdf, x='tip_pct', ax=axes[0], kde=True)
sns.histplot(data=tipdf, x='day', ax=axes[1], kde=True)
sns.histplot(data=tipdf, x='total_bill', ax=axes[2], kde=True)



# 쌓는 기능 = Stacked
# 글자 기울이기 = rot
# 범례 표시하기 legend

# plt.barh(pvdf['day'], pvdf['tip'])
plt.show()
