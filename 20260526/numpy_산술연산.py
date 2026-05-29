import numpy as np
import matplotlib.pyplot as plt
arr1 = np.array([ [5,7], [3,7]])
arr2 = np.array([[3,5], [2,5]])
print(arr1)
print(arr2)
print(arr1 + arr2)

arr3 = np.array([3,4,5])
print(arr3 + [3,4,5])
print(arr3 + 3)

arr4 = np.linspace(1,10,5)
# 메모리에 차트를 렌더링
arr5 = np.array([1,3,6,10,15])
plt.plot(arr4)
plt.show()