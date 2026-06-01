import pandas as pd
import numpy as np

# 제일 위에 있는 데이터를 기본적으로 컬럼 데이터로 인식하여 DataFrame 형성
# header=None: 제일 위의 데이터를 컬럼으로 인식하지 않고 데이터로 사용
# None 말고 [] 리스트로 직접 명시도 가능하다
scoredf = pd.read_csv("scoredata.csv", names=['main', 's', 'su', 'sub'])
print(scoredf)
