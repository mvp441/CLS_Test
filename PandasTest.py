import pandas
df = pandas.read_csv('SR1_BCaL_8h.csv')
print(df)
print('description: ')
df2 = pandas.Series([df])
df2.describe(exclude=['N/A'])   # quick statistical summary of data