import pandas as pd
import numpy as np

gas_df = pd.read_csv("seoul_keumchun_gas_info.csv", encoding='CP949')
print(gas_df)

# 생성된 Dataframe의 '데이터 기준일자' 컬럼 데이터가
# datetime 이 아니고 object(문자열) 이면 datetime type으로 변환
# 변환 이후 해당 컬럼을 인덱스로 설정해줌
# ==> 완벽한 시계열 데이터 형성

print(gas_df.info())
gas_df['데이터기준일자'] = gas_df['데이터기준일자'].astype('datetime64[ns]')
print(gas_df.info())

# 이러면 날짜 추출해서 object > datetime으로 바꾸고 그걸 다시 인덱스에 넣어주라는말이네 어떻게 해줄 수 있을까?
#
