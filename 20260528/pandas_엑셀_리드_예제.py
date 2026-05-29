from posixpath import split

import pandas as pd
import numpy as np
pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

youdf = pd.read_excel("youtube_rank_1000.xlsx")
print(youdf)
print(youdf.head(10))
# ChannelName 컬럼 데이터를 정리
# ==> 예) Boram Tube Vlog [보람튜브 브이로그] == Boram
#             JYP ~~~     ==> JYP
#                 BLACKPINK   ==> BLACKPINK
# 어떻게 업데이트 할까? 엑셀 > 컬럼 > 첫 글자까지 추출
# 그럼 공백 기준으로 자르고 그 앞을 출력?
# 아니면 공백까지 출력?
# 공백까지 출력은 어떻게하는데?
# [: ''] 처럼 슬라이싱 할 수 는 없나?
# T/F로 하는건 안될텐데 뭐로 하지
# 아 이거 공백기준으로 split 하고 인덱싱해서 1번만 가져올까?

print(youdf['ChannelName'])
result = []
for i in youdf['ChannelName']:
    word=i.split() # 아시발 공백' ' 넣는거 까먹었다 근데 왜됐지
    result.append(word[0])

youdf['ChannelName'] = result
print(youdf['ChannelName'])

print(youdf)
youdf.to_excel("youtube_rank_1000_First_Name.xlsx")
# 선생님 답
# 함수를 이용해서 ChannelName 컬럼 데이터를 일괄 정리
# 일괄 정리 ==> 하나의 문자열 항목만 있게 하자.(공백을 기준으로 분할시켜서
# 첫 번째 항목만 선택
# print(youdf.columns) 써서 컬럼을 출력(공백이 있나 확인) 후 그거 드래그/복사 해서 쓰는게 낫다

# def ChannelNameControl(arg):
#     print(arg.split(' '))
#
# youdf['ChannelName'].apply(ChannelNameControl)