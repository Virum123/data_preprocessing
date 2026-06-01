import numpy as np
import pandas as pd

tipdf= pd.read_csv("tips.csv")
print(tipdf)
# 'day' 컬럼 데이중 'Sat', 'Fri' 데이터만 추출
subset1 = tipdf.loc[ tipdf['day'] == 'Sat', :]
subset2 = tipdf.loc[ tipdf['day'] == 'Fri', :]
print(subset1)
print(subset2) # 요약된 부분이 없으면 [106 rows x 7 columns] 이런 정리본을 보여주지 않는데
# concat을 이용한 series의 병합은 잘 사용하지 않는다

print('='*80)
condf = pd.concat([subset1, subset2], axis=0) # 1: 아래로, 2: 옆으로 붙인다
print(condf)