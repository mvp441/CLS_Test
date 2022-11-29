import pandas as pd
from matplotlib import pyplot as plt

def sample_df():
    x = []
    y = []
    x = [i for i in range(100)]
    y = x
    data = {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    dfs = pd.DataFrame(data=data)
    return dfs

def dfs_pct_c(dfs):
    dfs['x_Ret'] = dfs['x'].pct_change()
    dfs['y_Ret'] = dfs['y'].pct_change()
    return dfs

def dfs_pct_c1(df):
    df['PCT1402-01:mA:fbk_Ret'] = df['PCT1402-01:mA:fbk'].pct_change()
    df['PCT1402-01:mAChange_Ret'] = df['PCT1402-01:mAChange'].pct_change()
    df1s = df.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
    dfsx = df.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
    dfsy = df.sort_values('PCT1402-01:mAChange_Ret', ascending=False)
    return df, df1s, dfsx, dfsy

def dfs_pct_c2(df):
    df2 = df.copy()
    df2['PCT1402-01:mA:fbk_Ret'] = df2['PCT1402-01:mA:fbk'].pct_change(fill_method='pad')
    df2['PCT1402-01:mAChange_Ret'] = df2['PCT1402-01:mAChange'].pct_change(fill_method='pad')
    df2s = df2.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
    df2sx =df2.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
    df2sx2 = df2sx.iloc[:, [4]]
    df2sy = df2.sort_values('PCT1402-01:mAChange_Ret', ascending=True)
    df2sy2 = df2sy.iloc[:, [5]]
    return df2, df2s, df2sx2, df2sy2

def dfs_pct_c3(df):
    df_pad = df.copy().fillna(method='pad')
    df_pad['PCT1402-01:mA:fbk_Ret'] = df_pad['PCT1402-01:mA:fbk'].pct_change()
    df_pad['PCT1402-01:mAChange_Ret'] = df_pad['PCT1402-01:mAChange'].pct_change()
    dfps = df_pad.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
    dfpsx = df_pad.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
    dfpsx2 = dfpsx.iloc[:, [4]]
    dfpsy = df_pad.sort_values('PCT1402-01:mAChange_Ret', ascending=True)
    dfpsy2 = dfpsy.iloc[:, [5]]
    return df_pad, dfps, dfpsx2, dfpsy2

def dfs_pct_c4(df):
    df_int = df.copy().interpolate(method='polynomial', order=5)
    df_int['PCT1402-01:mA:fbk_Ret'] = df_int['PCT1402-01:mA:fbk'].pct_change()
    df_int['PCT1402-01:mAChange_Ret'] = df_int['PCT1402-01:mAChange'].pct_change()
    dfis = df_int.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
    dfisx = df_int.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
    dfisx2 = dfisx.iloc[:, [4]]
    dfisy = df_int.sort_values('PCT1402-01:mAChange_Ret', ascending=True)
    dfisy2 = dfisy.iloc[:, [5]]
    return df_int, dfis, dfisx2, dfisy2

def sample_plot(dfs):
    plt.figure(1)
    plt.scatter(dfs['x_Ret'], dfs['y_Ret'], color='green')
    plt.xlabel('x percent change')
    plt.ylabel('y percent change')

def plot_scatter_1(df0):
    plt.figure(2)
    plt.scatter(df0['PCT1402-01:mA:fbk_Ret'], df0['PCT1402-01:mAChange_Ret'], color='blue')
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')

def cmp_2_plot_1(df2, df_pad):
    plt.figure(3)
    plt.subplot(211)
    plt.scatter(df2['PCT1402-01:mA:fbk_Ret'], df2['PCT1402-01:mAChange_Ret'], color='blue')
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')
    plt.subplot(212)
    plt.scatter(df_pad['PCT1402-01:mA:fbk_Ret'], df_pad['PCT1402-01:mAChange_Ret'], color='red')
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')

def cmp_2_plot_2(df_int, dfi2):
    plt.figure(4)
    plt.subplot(211)
    plt.scatter(df_int['PCT1402-01:mA:fbk_Ret'], df_int['PCT1402-01:mAChange_Ret'], color='green')
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')
    plt.subplot(212)
    plt.scatter(dfi2['PCT1402-01:mA:fbk_Ret'], dfi2['PCT1402-01:mAChange_Ret'], color='red')
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')

def plot_all(dfs, df2, df_pad, df_int, dfi2):
    plt.close('all')

    sample_plot(dfs)
    plt.title('Correlation of Sample Data')

    plot_scatter_1(df0)
    plt.title('Correlation of Actual Data with NA')

    cmp_2_plot_1(df2, df_pad)
    plt.subplot(211)
    plt.title('Correlation of Actual Data with NA filled')
    plt.subplot(212)
    plt.title('Correlation of Actual Data with NA Padded')

    cmp_2_plot_2(df_int, dfi2)
    plt.subplot(211)
    plt.title('Correlation of Actual Data with NA Interpolated')
    plt.subplot(212)
    plt.title('Correlation of first 230 points of Actual Data with NA Interpolated')
    plt.show(block='False')

def corr_calc(dfs, df2, df_pad, df_int, dfi2):
    correlation_s = dfs['x_Ret'].corr(dfs['y_Ret'])
    correlation0 = df0['PCT1402-01:mA:fbk_Ret'].corr(df0['PCT1402-01:mAChange_Ret'])
    correlation2 = df2['PCT1402-01:mA:fbk_Ret'].corr(df2['PCT1402-01:mAChange_Ret'])
    correlation_pad = df_pad['PCT1402-01:mA:fbk_Ret'].corr(df_pad['PCT1402-01:mAChange_Ret'])
    correlation_int = df_int['PCT1402-01:mA:fbk_Ret'].corr(df_int['PCT1402-01:mAChange_Ret'])
    correlation_i2 = dfi2['PCT1402-01:mA:fbk_Ret'].corr(dfi2['PCT1402-01:mAChange_Ret'])
    return correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2

def print_corr(correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2):
    print("Sample correlation is: ", correlation_s)
    print("Correlation is: ", correlation0)
    print("Padded correlation using pct_change fill is: ", correlation2)
    print("Padded correlation using fillna is: ", correlation_pad)
    print("Correlation of all data points using interpolation is: ", correlation_int)
    print("Correlation of first 230 data points using interpolation is: ", correlation_i2)

df = pd.read_csv("SR1_BCaL_8h.csv")
dfm = df.iloc[1:230, 0:4]

dfs = sample_df()
dfs = dfs_pct_c(dfs)

df0, df1s, dfsx, dfsy = dfs_pct_c1(df)
df2, df2s, df2sx2, df2sy2 = dfs_pct_c2(df)
df_pad, dfps, dfpsx2, dfpsy2 = dfs_pct_c3(df)
df_int, dfis, dfisx2, dfisy2 = dfs_pct_c4(df)
dfi2, dfi2s, dfi2sx2, dfi2sy2 = dfs_pct_c4(dfm)

plot_all(dfs, df2, df_pad, df_int, dfi2)
correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2 = corr_calc(dfs, df2, df_pad, df_int, dfi2)
print_corr(correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2)


