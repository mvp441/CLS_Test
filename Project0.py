import pandas as pd
from matplotlib import pyplot as plt

def df_pct_corr(df):
    dft = df.copy().interpolate(method='polynomial', order=5)
    dft['PCT1402-01:mA:fbk_Ret'] = dft['PCT1402-01:mA:fbk'].pct_change()
    dft['PCT1402-01:mAChange_Ret'] = dft['PCT1402-01:mAChange'].pct_change()
    for column in dft.columns[1:]:
        mean = dft[column].abs().mean()
        std = dft[column].abs().std()
        check2 = dft[abs(dft[column]) > (mean + std)].index
        dft.drop(check2, inplace=True)
    dfts = dft.sort_values(by=['PCT1402-01:mA:fbk_Ret', 'PCT1402-01:mAChange_Ret'])
    dftsx = dft.sort_values('PCT1402-01:mA:fbk_Ret', ascending=False)
    dftsx2 = dftsx.iloc[:, [4]]
    dftsy = dft.sort_values('PCT1402-01:mAChange_Ret', ascending=True)
    dftsy2 = dftsy.iloc[:, [5]]
    dfc = dft['PCT1402-01:mA:fbk_Ret'].corr(dft['PCT1402-01:mAChange_Ret'])  # method = pearson, kendall, etc.
    return dft, dfc

def cor_plot(dfs, dfc):
    plt.figure(1)
    plt.scatter(dfs['PCT1402-01:mA:fbk_Ret'], dfs['PCT1402-01:mAChange_Ret'], color='green')
    plt.title('Correlation of all data points using interpolation and ignoring outliers is: ' + str(dfc))
    plt.xlabel('x percent change')
    plt.ylabel('y percent change')

def dfpc_plot(df_int, dfi2):
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

df = pd.read_csv("SR1_BCaL_8h.csv")

dft, dfc = df_pct_corr(df)
cor_plot(dft, dfc)
plt.show()











