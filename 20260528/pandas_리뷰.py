import numpy as np
import pandas as pd

# 사전을 활용해서 Dataframe 객체 생성
dictdata = {'Hong':[90,80,70,60,75], 'Kim':[85,95,65,55,75], 'Park':[88, 93, 75, 72,75], 'Lee':[55,66,77,92,75] }
# 위 사전을 활용서 Dataframe  객체 생성
scoredf = pd.DataFrame( dictdata , index=['kor','eng','math','music','sci'])
print(scoredf)
scoredf.rename( index={'music':'음악'},  inplace=True )
print(scoredf)
scoredf.rename( columns={'Park':'김'}, inplace=True )
print(scoredf)

print (scoredf['Lee']) #이렇게 출력되는 형태는 series 이다
print (scoredf [ ['Kim'] ]) # 이렇게 출력되면 DataFrame, 여러 개를 선택한다는 []로 한 번 더 묶어줬기 때문임
sortdf =  scoredf[ ['Kim','Lee', 'Hong', '김'] ] # 정렬하고 싶으면 다시 적어주면됨
print(sortdf)
print ("=" *80)
print( scoredf.iloc[[1], : ])
print( scoredf.iloc[1:2, : ])
# fancy index ==> 추출하고자 하는
print( scoredf.iloc[[1,3], : ])
# date_index=pd.date_range('2026.12.28',periods=30,freq='D')
# print(date_index)
#
dic = {}
dic['dd'] = 'd'
print(dic)
# # date_index=pd.date_range('2026.05.28',periods=50)
# # # freq 설정 안하면 자동으로 day고 날짜를 월, 년만 적으면 거기서 가장 가까운 2026.01.01 / 2026.05.01 같은걸로 시작함
# # print(date_index)
#
# timedf = pd.DataFrame( np.arange(1,51) , index = pd.date_range('2026.12.28',periods=50),
#                        columns=['data'])
# print(timedf)
# timedf.info()
# print(timedf.loc['2026-12-28':'2026-12-31', : ])
# print( timedf.loc['2026/12'])

# 문자열 타입을 ===> datetime 타입으로 변환해서 사용 ( pd.to_datetime() )