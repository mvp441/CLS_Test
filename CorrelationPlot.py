import pandas as pd
from matplotlib import pyplot as plt

x = []
y = []
x = [i for i in range(100)]
y = x
data = {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

dfs = pd.DataFrame(data=data)
dfs['x_Ret'] = dfs['x'].pct_change()
dfs['y_Ret'] = dfs['y'].pct_change()

df = pd.read_csv("SR1_BCaL_8h.csv")
df = df.iloc[1:230, 0:4]
df['PCT1402-01:mA:fbk_Ret'] = df['PCT1402-01:mA:fbk'].pct_change()  #fill_method='pad')
df['PCT1402-01:mAChange_Ret'] = df['PCT1402-01:mAChange'].pct_change()  #fill_method='pad')
df1s = df.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
dfsx = df.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
dfsy = df.sort_values('PCT1402-01:mAChange_Ret', ascending=False)

df2 = df.copy()
df2['PCT1402-01:mA:fbk_Ret'] = df2['PCT1402-01:mA:fbk'].pct_change(fill_method='bfill')
df2['PCT1402-01:mAChange_Ret'] = df2['PCT1402-01:mAChange'].pct_change(fill_method='bfill')
df2s = df2.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
df2sx =df2.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
df2sx2 = df2sx.iloc[:, [4]]
df2sy = df2.sort_values('PCT1402-01:mAChange_Ret', ascending=True)
df2sy2 = df2sy.iloc[:, [5]]

df_pad = df.copy().fillna(method='pad')
df_pad['PCT1402-01:mA:fbk_Ret'] = df_pad['PCT1402-01:mA:fbk'].pct_change()
df_pad['PCT1402-01:mAChange_Ret'] = df_pad['PCT1402-01:mAChange'].pct_change()
dfps = df_pad.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
dfpsx = df_pad.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
dfpsx2 = dfpsx.iloc[:, [4]]
dfpsy = df_pad.sort_values('PCT1402-01:mAChange_Ret', ascending=True)
dfpsy2 = dfpsy.iloc[:, [5]]

df_int = df.copy().interpolate()
df_int['PCT1402-01:mA:fbk_Ret'] = df_int['PCT1402-01:mA:fbk'].pct_change()
df_int['PCT1402-01:mAChange_Ret'] = df_int['PCT1402-01:mAChange'].pct_change()
dfis = df_int.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
dfisx = df_int.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
dfisx2 = dfisx.iloc[:, [4]]
dfisy = df_int.sort_values('PCT1402-01:mAChange_Ret', ascending=True)
dfisy2 = dfisy.iloc[:, [5]]

plt.figure(1)
plt.scatter(dfs['x_Ret'], dfs['y_Ret'], color='green')
plt.title('Correlation of Sample Data')
plt.xlabel('x percent change')
plt.ylabel('y percent change')

plt.figure(2)
plt.scatter(df['PCT1402-01:mA:fbk_Ret'], df['PCT1402-01:mAChange_Ret'], color='blue')
plt.title('Correlation of Actual Data with NA ')
plt.xlabel('fbk percent change')
plt.ylabel('mAChange percent change')

plt.figure(3)
plt.subplot(311)
plt.scatter(df2['PCT1402-01:mA:fbk_Ret'], df2['PCT1402-01:mAChange_Ret'], color='blue')
plt.title('Correlation of Actual Data with NA filled')
plt.xlabel('fbk percent change')
plt.ylabel('mAChange percent change')
plt.subplot(312)
plt.scatter(df_pad['PCT1402-01:mA:fbk_Ret'], df_pad['PCT1402-01:mAChange_Ret'], color='red')
plt.title('Correlation of Actual Data with NA Padded')
plt.xlabel('fbk percent change')
plt.ylabel('mAChange percent change')
plt.subplot(313)
plt.scatter(df_int['PCT1402-01:mA:fbk_Ret'], df_int['PCT1402-01:mAChange_Ret'], color='green')
plt.title('Correlation of Actual Data with NA Interpolated')
plt.xlabel('fbk percent change')
plt.ylabel('mAChange percent change')

plt.figure(4)
plt.scatter(df_pad['PCT1402-01:mA:fbk_Ret'], df_pad['PCT1402-01:mAChange_Ret'], color='red')
plt.title('Correlation of Actual Data with NA Padded')
plt.xlabel('fbk percent change')
plt.ylabel('mAChange percent change')
plt.show(block='False')

correlation_s = dfs['x_Ret'].corr(dfs['y_Ret'])
correlation = df['PCT1402-01:mA:fbk_Ret'].corr(df['PCT1402-01:mAChange_Ret'])
correlation_pad = df_pad['PCT1402-01:mA:fbk_Ret'].corr(df_pad['PCT1402-01:mAChange_Ret'])

print("Sample correlation is: ", correlation_s)
print("Correlation is: ", correlation)
print("Padded correlation is: ", correlation_pad)

