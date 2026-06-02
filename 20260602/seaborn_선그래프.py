import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2,1)
dateidx = np.arange(0,100,10)
data = np.random.randn(10,4).cumsum(axis=0)

mydf = pd.DataFrame(data, index=dateidx, columns=['A', 'B', 'C', 'D']) # list("ABCD") 로 넣어도 나옴
print(mydf)

sns.barplot(ax=axes[0], data=mydf)
sns.barplot(ax=axes[1], data=mydf['C'])
plt.show()