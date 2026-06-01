import pandas as pd
import numpy as np

mydf = pd.DataFrame([ [ 80, 90, 70], [75,65,95] ], index = pd.Index(['kor', 'math'], name='subdect'),
                    columns=pd.Index(['stu1', 'stu2','stu3'], name='studednt'))
print(mydf)
# 데이터프레인 형태를 바꿀때 필요한 문법 ==> 재형성
# pivot은 안쓴대 왜? 단점이 있음
# 
stdf = mydf.stack()
print(stdf)
print(stdf, type(stdf))

unstdf = stdf.unstack()
print(unstdf)