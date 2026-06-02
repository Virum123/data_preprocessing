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
tipdf.info()

# ‘day’ 컬럼을 기준으로 그룹화 후‘tip‘컬럼의 데이터 합 계산
pvdf = tipdf.pivot_table(index='day', values='tip', aggfunc='sum')
print(pvdf)
pvdf.reset_index(inplace=True)
print(pvdf)
print(pvdf['day'])
print(pvdf['tip'])
plt.bar(pvdf['day'], pvdf['tip'])
#
fig, axes = plt.subplots(2,1, figsize=(10,10))


# 쌓는 기능 = Stacked
# 글자 기울이기 = rot
# 범례 표시하기 legend

# plt.barh(pvdf['day'], pvdf['tip'])
plt.show()
