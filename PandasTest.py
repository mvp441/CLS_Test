import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SR1_BCaL_8h.csv')  # , parse_dates=['Timestamp']) doesn't plot properly when loaded in with Timestamp in datetime format

df.plot()
df2 = df
df2['Timestamp'] = pd.to_datetime(df2['Timestamp']) #, infer_datetime_format=True)
# df2.plot()
plt.show()

dfmini = df.iloc[1:100, 0:2]
dfminiNA = dfmini.dropna()

TSx = dfminiNA.iloc[:, 0]
TSx2 = pd.to_datetime(dfminiNA.Timestamp, infer_datetime_format=True)
TSx3 = pd.to_timedelta(TSx, unit='ns')
TSx4 = pd.to_numeric(dfminiNA.Timestamp)


fbky = dfminiNA.iloc[:, 1]

dfminiNA.info()
dfminiNA.plot()
dfminiNA['Timestamp'] = pd.to_datetime(dfminiNA['Timestamp'])
print('after conversion \n')
dfminiNA.info()
dfminiNA.plot()
print('done conversion plot')



'''
ax = [i for i in range(len(fbky))]
x1 = dfminiNA.iloc[0, 0]  # single string value
x2 = pd.to_datetime(TSx, infer_datetime_format=True)  # series of Timestamps
x3 = pd.to_datetime(x1)  # single timestamp value
x4 = x2.iloc[0]  # single timestamp value
'''


