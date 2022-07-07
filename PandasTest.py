import pandas
df = pandas.read_csv('SR1_BCaL_8h.csv')
print(df)
df.describe()   # quick statistical summary of data