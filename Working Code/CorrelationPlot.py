import pandas as pd
from matplotlib import pyplot as plt

def sample_df():
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

def dfs_pct_test(df):
    df_test = df.copy().interpolate(method='polynomial', order=5)
    df_test['PCT1402-01:mA:fbk_Ret'] = df_test['PCT1402-01:mA:fbk'].pct_change()
    df_test['PCT1402-01:mAChange_Ret'] = df_test['PCT1402-01:mAChange'].pct_change()
    for column in df_test.columns[1:]:
        mean = df_test[column].abs().mean()
        std = df_test[column].std()
        std2 = df_test[column].abs().std()
        check = df_test[abs(df_test[column]) > (2*mean)].index
        check1 = df_test[abs(df_test[column]) > (mean + (2 * std))].index
        check2 = df_test[abs(df_test[column]) > (mean + (std2))].index
        dfc1 =df_test.copy()
        dfc1.drop(check1, inplace=True)
        dfc2 =df_test.copy()
        dfc2.drop(check2, inplace=True)
        df_test.drop(check2, inplace=True)
    dfts = df_test.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
    dftsx = df_test.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
    dftsx2 = dftsx.iloc[:, [4]]
    dftsy = df_test.sort_values('PCT1402-01:mAChange_Ret', ascending=True)
    dftsy2 = dftsy.iloc[:, [5]]
    return df_test, dfts, dftsx2, dftsy2

def sample_plot(dfs):
    plt.figure(1)
    plt.scatter(dfs['x_Ret'], dfs['y_Ret'], color='green')
    plt.xlabel('x percent change')
    plt.ylabel('y percent change')

def plot_scatter_1(df0):
    plt.figure(2)
    plt.subplot(211)
    plt.scatter(df0['PCT1402-01:mA:fbk_Ret'], df0['PCT1402-01:mAChange_Ret'], color='blue')
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')

    plt.subplot(212)
    plt.scatter(df0['PCT1402-01:mA:fbk_Ret'], df0['PCT1402-01:mAChange_Ret'], color='red')
    plt.ylim([-1, 3])
    plt.xlim([-0.002, 0.0045])
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
    plt.scatter(df_int['PCT1402-01:mA:fbk_Ret'], df_int['PCT1402-01:mAChange_Ret'], color='blue')
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')

    plt.subplot(212)
    plt.scatter(dfi2['PCT1402-01:mA:fbk_Ret'], dfi2['PCT1402-01:mAChange_Ret'], color='red')
    plt.xlim([-0.001, 0.002])
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')

def plot_scatter_2(df_test):
    plt.figure(5)
    plt.scatter(df_test['PCT1402-01:mA:fbk_Ret'], df_test['PCT1402-01:mAChange_Ret'], color='blue')
    plt.xlabel('fbk percent change')
    plt.ylabel('mAChange percent change')

def corr_calc(dfs, df2, df_pad, df_int, dfi2, df_test):
    correlation_s = dfs['x_Ret'].corr(dfs['y_Ret'])
    correlation0 = df0['PCT1402-01:mA:fbk_Ret'].corr(df0['PCT1402-01:mAChange_Ret']) # method = pearson, kendall, etc.
    correlation2 = df2['PCT1402-01:mA:fbk_Ret'].corr(df2['PCT1402-01:mAChange_Ret'])
    correlation_pad = df_pad['PCT1402-01:mA:fbk_Ret'].corr(df_pad['PCT1402-01:mAChange_Ret'])
    correlation_int = df_int['PCT1402-01:mA:fbk_Ret'].corr(df_int['PCT1402-01:mAChange_Ret'])
    correlation_i2 = dfi2['PCT1402-01:mA:fbk_Ret'].corr(dfi2['PCT1402-01:mAChange_Ret'])
    correlation_test = df_test['PCT1402-01:mA:fbk_Ret'].corr(df_test['PCT1402-01:mAChange_Ret'])
    return correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2, correlation_test

def plot_all(dfs, df2, df_pad, df_int, dfi2, df_test, correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2, correlation_test):
    plt.close('all')

    sample_plot(dfs)
    plt.title('Correlation of Sample Data \n correlation = ' + str(correlation_s))

    plot_scatter_1(df0)
    plt.subplot(211)
    plt.title('Correlation of Actual Data with NA \n correlation = ' + str(correlation0))
    plt.subplot(212)
    plt.title('Correlation of Actual Data with NA zoomed in \n correlation = ' + str(correlation0))

    cmp_2_plot_1(df2, df_pad)
    plt.subplot(211)
    plt.title('Correlation of Actual Data with NA filled \n correlation = ' + str(correlation2))
    plt.subplot(212)
    plt.title('Correlation of Actual Data with NA Padded \n correlation = ' + str(correlation_pad))

    cmp_2_plot_2(df_int, dfi2)
    plt.subplot(211)
    plt.title('Correlation of Actual Data with NA Interpolated \n correlation = ' + str(correlation_int))
    plt.subplot(212)
    plt.title('Correlation of first 225 points of Actual Data with NA Interpolated \n correlation = ' + str(correlation_i2))

    plot_scatter_2(df_test)
    plt.title('Correlation of Actual Data with NA and outliers ignored \n correlation = ' + str(correlation_test))

    plt.show(block='False')

def print_corr(correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2, correlation_test):
    print("Sample correlation is: ", correlation_s)
    print("Correlation is: ", correlation0)
    print("Padded correlation using pct_change fill is: ", correlation2)
    print("Padded correlation using fillna is: ", correlation_pad)
    print("Correlation of all data points using interpolation is: ", correlation_int)
    print("Correlation of first 225 data points using interpolation is: ", correlation_i2)
    print("Correlation of all data points using interpolation and ignoring outliers is: ", correlation_test)

df = pd.read_csv("../PV Data/SR1_BCaL_8h.csv")
dfm = df.iloc[1:225, 0:4]

dfs = sample_df()
dfs = dfs_pct_c(dfs)

df0, df1s, dfsx, dfsy = dfs_pct_c1(df)
df2, df2s, df2sx2, df2sy2 = dfs_pct_c2(df)
df_pad, dfps, dfpsx2, dfpsy2 = dfs_pct_c3(df)
df_int, dfis, dfisx2, dfisy2 = dfs_pct_c4(df)
dfi2, dfi2s, dfi2sx2, dfi2sy2 = dfs_pct_c4(dfm)

df_test, dfts, dftsx2, dftsy2 = dfs_pct_test(df)

#plot_scatter_2(df_test)
#plt.title('Correlation of all data points using interpolation and ignoring outliers')
#plt.savefig("CorrelationPlot")
plt.show()



correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2, correlation_test = corr_calc(dfs, df2, df_pad, df_int, dfi2, df_test)
plot_all(dfs, df2, df_pad, df_int, dfi2, df_test, correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2, correlation_test)
print_corr(correlation_s, correlation0, correlation2, correlation_pad, correlation_int, correlation_i2, correlation_test)

# statology.org/partial-correlation-python/
#pingouin-stats.org/build/html/index.html
# pairwise correlation between columns of a dataframe

