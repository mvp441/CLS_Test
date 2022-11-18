import pandas as pd

#keep_default_na = False
#na_filter = True

df = pd.read_csv('SR1_BCaL_8h.csv')

dfminiNA = df.iloc[1:100, 0:2]

dfminiNA = dfminiNA.dropna()

TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]

x1 = dfminiNA.iloc[:, 0]

dfminiNA.info()
dfminiNA['Timestamp'] = pd.to_datetime(dfminiNA['Timestamp'])
print('after conversion \n')
dfminiNA.info()

x2 = dfminiNA.iloc[:, 0]

print(x1)
print(x2)


'''
ax = [i for i in range(len(fbky))]
x1 = dfminiNA.iloc[0, 0]  # single string value
x2 = pd.to_datetime(TSx, infer_datetime_format=True)  # series of Timestamps
x3 = pd.to_datetime(x1)  # single timestamp value
x4 = x2.iloc[0]  # single timestamp value
'''

df2 = pd.to_datetime(df.Timestamp)
print(df2)

#print("\n na reaplced? \n")
#print(df.fillna(method="pad")) # filled NaN with data based on surrounding values, only works when printing
#print(df)
#print('\n Description: ')
#print(df.describe()) # quick statistical summary of data
#print(df.sample(n=10))
#print(df.to_numpy())
#print("\n")
#print(df.columns)
#print("\n")
#df.plot.hist() # histogram for each column


