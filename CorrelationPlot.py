import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("SR1_BCaL_8h.csv")
df_pad = df.copy().fillna(method='pad')
x = []
y = []
x = [i for i in range(100)]
y = x
data = {'x' : [1,2,3,4,5,6,7,8,9,10], 'y' : [1,2,3,4,5,6,7,8,9,10]}
dfs = pd.DataFrame(data=data) #, index=['x','y'], columns=[0, 1,2,3,4,5,6,7,8,9])
#dfs = dfs.append({'x_data' : x}, ignore_index=True)
#dfs = dfs.append({'y_data' : y}, ignore_index=True)
df['PCT1402-01:mA:fbk_Ret'] = df['PCT1402-01:mA:fbk'].pct_change()
df['PCT1402-01:mAChange_Ret'] = df['PCT1402-01:mAChange'].pct_change()
df_pad['PCT1402-01:mA:fbk_Ret'] = df_pad['PCT1402-01:mA:fbk'].pct_change()
df_pad['PCT1402-01:mAChange_Ret'] = df_pad['PCT1402-01:mAChange'].pct_change()
dfs['x_Ret'] = dfs['x'].pct_change()
dfs['y_Ret'] = dfs['y'].pct_change()

plt.figure(1)
plt.scatter(dfs['x_Ret'], dfs['y_Ret'], color='green')
plt.title('Correlation of Sample Data')
plt.xlabel('x percent change')
plt.ylabel('y percent change')
plt.figure(2)
plt.scatter(df['PCT1402-01:mA:fbk_Ret'], df['PCT1402-01:mAChange_Ret'], color='blue')
plt.scatter(df_pad['PCT1402-01:mA:fbk_Ret'], df_pad['PCT1402-01:mAChange_Ret'], color='red')
plt.title('Correlation of Actual Data')
plt.xlabel('fbk percent change')
plt.ylabel('mAChange percent change')
plt.show(block='False')

correlation_s = dfs['x_Ret'].corr(dfs['y_Ret'])
correlation = df['PCT1402-01:mA:fbk_Ret'].corr(df['PCT1402-01:mAChange_Ret'])
correlation_pad = df_pad['PCT1402-01:mA:fbk_Ret'].corr(df_pad['PCT1402-01:mAChange_Ret'])

print("Sample correlation is: ", correlation_s)
print("Correlation is: ", correlation)
print("Padded correlation is: ", correlation_pad)

