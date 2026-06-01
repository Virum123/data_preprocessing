import numpy as np
import pandas as pd


pd.set_option('display.max_rows',1000) # 출력 옵션  제어
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

sale_df = pd.read_excel('salesfunnel.xlsx')
print(sale_df.head())

pvdf = sale_df.pivot_table(index=['Manager', 'Rep', 'Product'], values=['Price', 'Quantity'], aggfunc=['sum', 'mean'], margins=True)
# margins의 기본 이름은 All이다
print(pvdf)
print(pvdf.index)
print(pvdf.columns)

pvdf.columns = [ 'sum_price', 'sum_quantity', 'mean_price', 'mean_quantity' ]
print(pvdf.columns)