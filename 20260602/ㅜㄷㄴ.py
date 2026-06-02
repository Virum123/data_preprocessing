from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
import seaborn as sns
import numpy as np
import pandas as pd

idxdata = [ str(x) for x in range (20000501,20000531)]
# 문자 인덱스
mydf = pd.DataFrame({'가격':np.random.randint(12000,13000,size=(30,))},
                    index = idxdata)

fig = plt.figure(figsize=(11,7))
ax1 = fig.add_subplot(1,1,1)
ax1.plot(mydf.index, mydf)

ax1.xaxis.set_major_locator(MultipleLocator(3)) # major 눈금 x축 첫번째 부터 시작해서 매 3번째 마다 표시
ax1.xaxis.set_minor_locator(MultipleLocator(1))  # minor 눈금 모든 x축 위치 마다 눈금 표시
# x축 눈금스타일설정:x축major눈금 설정및회전
ax1.tick_params(axis='x',which='major',length=10,width=2,color='r', rotation=15)
# plt.xticks(rotation=15)
ax1.plot()
plt.show()