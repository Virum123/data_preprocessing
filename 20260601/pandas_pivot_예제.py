import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)


tipdf= pd.read_csv("tips.csv")
print(tipdf)
# 요일별 'total_bill, tip 의 총합을 계산 출력

grp = tipdf.groupby('day')[['total_bill', 'tip']].sum()
print(grp)

# 재형성에서 pivot_table()
# pd.pivot_table(data = tipdf) 애는 데이터를 직접 줘야함
ptt = tipdf.pivot_table(index='day', values=['total_bill', 'tip'], aggfunc='sum') # 애는 직접 줘서 따로 데이터를 주지 않아도 됨  columns=, 는 여기서 안씀
# 명시되어있어 가독성도 훨씬 좋음

print(ptt)

pvdf = tipdf.pivot_table(index='day', columns='smoker', values='tip', aggfunc='sum')
print(pvdf)
pvdf.plot.bar(stacked=True, rot = 45)
plt.show()