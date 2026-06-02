import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# fig = plt.figure( figsize=(10,6))
#
# ax1 = fig.add_subplot(1,2,1)
# ax2 = fig.add_subplot(1,2,2)
#
# ax1.bar([10,20,30,40,50],[20,60,80,90,120],width=5, color='pink')
# ax2.plot([10,20,30,40,50],[20,60,80,90,120], linewidth=5, color='pink', alpha=0.5)
# plt.show() # 화면에 출력
# # plt.savefig('test.png') # 현재 차트를 이미지 파일로 저장

fig, axes = plt.subplots(1,2, figsize=(10,6))
axes[0].bar([10,20,30,40,50],[20,60,80,90,120],width=5, color='skyblue', linestyle='dashed')
axes[1].plot([10,20,30,40,50],[20,60,80,90,120], linewidth=8, color='#FFD6E0', alpha=0.5,
             marker='*', markersize=20, markeredgewidth=3,
             markeredgecolor='#6B4226', markerfacecolor='#FFE66D')
plt.show()
# 정리시 마커랑 색깔 예시 7개씩 제시할것