import pandas
df = pandas.read_csv('SR1_BCaL_8h.csv')
print(df)
#print('\n Description: ')
#print(df.describe()) # quick statistical summary of data
print("\n Series:")
df2 = pandas.Series([df])
print(df2)
#df.fillna(0)
# print(df.sample(n=10))
#print(df.to_numpy())
#print("\n")
#print(df.columns)
#print("\n")




