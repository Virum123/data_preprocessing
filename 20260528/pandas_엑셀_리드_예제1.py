import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

youdf = pd.read_excel("youtube_rank_1000_First_Name.xlsx", index_col=0)
print(youdf)
print(youdf.head(30))
youdf.info()
print(youdf['Video'].map(type).value_counts())
# Video 컬럼 데이터 기준으로 Top 10 항목을 추출해서 출력
# 1차 Video 컬럼 데이터를 수치 데이터로 모두 변환
# 문자열로 바꿔서 정규표현식으로 숫자만 뽑자
# 2차 내림차순으로 정렬
# 3차 리밋 10 때리면 되지 않을까
num = []
for i in youdf['Video']:
    result = re.findall(r'[0-9]',i)
    num.append(int(''.join(result)))

youdf['Video'] = num
youdf.sort_values(by=['Video'], inplace=True, ascending=False)
youdf_top10 = youdf.head(10).copy()
youdf_top10 = youdf_top10[['ChannelName','Video']]
print(youdf_top10)

sns.barplot(x='ChannelName', y='Video', data=youdf_top10, palette='Set3')
plt.show()

youdf_top10.set_index('ChannelName', inplace=True)
youdf_top10.plot.bar()
# plt.show()
# 정리하면
# 일단 핵심은 정규표현식을 이용해 숫자만 빼기야
# 1. 반복문으로 숫자만 저장하기
# 2. sort_value(by=[기준 컬럼], ascending=T/F) 로 정렬하기
# 3. 헤드 10개 .head(10)


# def VideoDataControl(arg):
#   re.sub(r'[,개]'.'', arg)
# youdf['Video'] = youdf['Video'].apply(VideoDataControl) >> 함수 자동으로 돌리기 훨씩 간단함
# youdf.info()
# youdf['Video'] = youdf['Video'].astype('int64') # 특정 컬럼데이터를 일괄 타입변환 해주는 메서드
# youdf.info()


