import pandas as pd
import os

lst = ['a', 'b', 'c', 'd']
df1 = pd.DataFrame(lst)
# print(df1)

mulLis = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df2 = pd.DataFrame(mulLis)
# print(df2)

disList = {'ID': pd.Series([1, 2, 3]), 'Name': ['a', 'b', 'c']}
df3 = pd.DataFrame(disList)
# print(df3)

csFile = pd.read_csv('C:\\Users\\test\Documents\\learn ML & AI\\pandas\\annual-enterprise.csv', nrows=1)
# print(csFile.columns)
# print(csFile)


