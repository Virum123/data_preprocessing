import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("whitegrid")

tips = sns.load_dataset("tips")
# tips.describe 사용해서 전체 데이터중 수치 데이터 컬럼만 선별해서 기본 통ㄱㅖ 데이터를 제공
#.max 같은거 이용해서 추가해줄 수 있음
plt.figure(figsize=(5,5))

sns.boxplot(x="day", y="total_bill", hue='smoker', data=tips, palette="flare")
plt.show()