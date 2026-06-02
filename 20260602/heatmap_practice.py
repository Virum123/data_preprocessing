import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

flights = sns.load_dataset("flights")
print(flights.head(10))

flights_pivot = flights.pivot(index='month', columns = 'year', values='passengers')
print(flights_pivot.head(10))
plt.figure(figsize=(10,9))
# annotate each cell with numberic value : 각 셀에 숫자를 입력
# fmt='d' : 정수형태로 숫자 입력
# cbar=False : 컬러 바 제거 , 디폴트 : True
# cmap : 컬러맵 (팔레트 이름전달) , seaborn_palette_name.png 파일참조
# linewidths : 구분선 크기
sns.heatmap(data=flights_pivot, annot=True, fmt="d", linewidths=4, cmap="flare")
plt.show()