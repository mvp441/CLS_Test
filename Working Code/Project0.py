import pandas as pd
from matplotlib import pyplot as plt
from lib import CSV

# add function for calculating correlation between multiple variables and sorting them

def corr_check(df):
    dft = df.copy().interpolate(method='polynomial', order=5)
    dfc1= dft.corrwith(dft, axis =1)  # method = pearson, kendall, etc.
    dfc2 = dft.corrwith(dft, axis=1, drop=True)  # method = pearson, kendall, etc.
    print(dfc1, '\n', dfc2)
#    dfc3 = dft.corrwith(dft, axis=1, method = pearson) #, kendall, etc.

# add function for pulling live data and compairing to fault patterns

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

# df = pd.read_csv("../PV Data/SR1_BCaL_8h.csv")
# dfColumns = df.columns.to_list()
#
# corr_check((df))
#
# dft, dfc = df_pct_corr(df)
# cor_plot(dft, dfc)
# plt.show()
#

csv_list = CSV.CSVList(["../PV Data/Trip 1 data/gLYHVdm+.csv"])

csv_list.add_csv('../PV Data/Trip 1 data/tdL5QoZo.csv')
# csv_list.add_csv("../PV Data/Trip 1 data/gLYHVdm+.csv")

csv_list.sort_by_column("Timestamp")

csv_list.interpolate_data()
csv_list.output_dataframe_to_console()

