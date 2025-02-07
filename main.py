import pandas as pd

lst = ['a', 'b', 'c', 'd']
df1 = pd.DataFrame(lst)
# print(df1)

mulLis = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df2 = pd.DataFrame(mulLis)
# print(df2)

disList = {'ID': pd.Series([1, 2, 3]), 'Name': ['a', 'b', 'c']}
df3 = pd.DataFrame(disList)
# print(df3)

csFile = pd.read_csv('student_results.csv', nrows=6, dtype={'Year':'float64'})
# print(csFile.columns)
# print(csFile)


csFile1 = pd.read_csv('student_results.csv', nrows=500)
# print(csFile1.isnull().sum())


df = pd.read_csv('student.csv')
print(df)

print(df.interpolate())