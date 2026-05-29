import pandas as pd
import numpy as np
import re
pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

passdf = pd.read_csv('서지승승.csv', encoding='cp949')


# 문제)
# ==>호선_명칭 컬럼 데이터 중 숫자문자가 있는 호선_명칭 데이터만 추출해서
# 출력해주세요.

# 호선_명칭 컬럼에서 숫자가 없는 컬럼 지우고 나머지 출력하면 되지 않을까
# 컬럼 필터링은 뭘 써야할까?
# print(passdf)
# 몰라 아는거 없어
# 대충 r'[0-9]' 해서 하면 될 것 같은데 모르겠음
# 순서만 정리하면 1. [호선_명칭] 컬럼 선택 2. 행에 숫자가 있는지 판단 3. 해당 행만 필터링

# 답
print(passdf['호선_명칭'] ) ## 메인 포인트는 불린색인이네 True면 출력하고 False면 출력안하는
bool_list = []

for name in passdf['호선_명칭']:
    result = re.findall(r'[0-9]+', name)

    if len(result) > 0:
        bool_list.append(True)
    else:
        bool_list.append(False)

subset = passdf.loc[bool_list, :]

print(subset)


import re
def dataselect(arg):
    #print(arg)
    if len(re.findall(r'[0-9]+',arg)) >0:
        return True
    else:
        return False
sub=passdf['호선_명칭'].apply(dataselect) # 함수명만 적어야 호출임

set = passdf.loc[sub,:]
print(set)