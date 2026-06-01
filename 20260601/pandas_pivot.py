import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pvdf = pd.read_excel('teacher_list_pivot_exam_1.xlsx')
print(pvdf)
# DF 재형성 메서드 ==> pivot
# pvdf = pvdf.pivot_table(index = '과정명', columns='강사명',values='강의시수',aggfunc='sum')
# print(pvdf)
# 9    Emb  Linux system Programming    50  홍길동
# 10   Emb  Linux system Programming    70  홍길동
# pivot() 같은경우
# 이런게 겹쳐서 오류가 남, 재형성 시점에서 중복 발생 시 수정/변환이 불가능함
# ==> pivot_table() ==> 재형성과 동시에 중복데이터를 집계(통계)룰 적용해서 형성한다

pvdf = pvdf.pivot_table(index = '과정명', columns='강사명',values='강의시수')
print(pvdf)

# 과정명 인덱스를 C, EmbC, EmbP, Linux로 변경하고
# 해당 데이터프레임을 막대차트 시각화

# 규칙이랄게 딱히 없으니까 카테고리 이름 하드코딩으로 바꾸고 막대차트 띠로링 하는것 같은데
# C랑 리눅스는 첫 음절을 그대로 사용하고 임베드는 카테고리 + 두번쌔 음절 첫글자 or 첫 음절 3글자 + 두 번쨰 음절 첫글자?
# 진짜 맥락이 하나도없네 문제가 지랄같냐
print(pvdf.index)
pvdf.index = ['C', 'EmbC', 'EmbP', 'Linux']
print(pvdf)
sns.barplot(pvdf, x='과정명', y='강의시수')
plt.show()