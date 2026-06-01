import pandas as pd
import numpy as np

df = pd.DataFrame({"subject":['kor','eng','kor','eng','math','kor','math'],
                   'score': [  70, 80, 90, 85, 75, 65, 60] } )
print(df)

# df.groupby(기준키)[집계(통계)함수를 적용할 컬럼선택].함수적용할집계통계함수
grp = df.groupby('subject')['score'].mean()
print(grp)
grp = df.groupby('subject')[['score']].mean()
print(grp) # 그룹핑된 Series 객체가 반환

# 집계(통계)를 적용할 컬럼을 리스트처럼 여러개로 선택 표현하면
# DataFrame으로 결과물이 나온다