import pandas as pd
import matplotlib.pyplot as plt

def TSFc():
    '''Using original data format. Shows correct pattern'''
    df = pd.read_csv('SR1_BCaL_8h.csv')
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]
    dfminiNA.plot()  # Plot uses x position for x-axis
    plt.figure()
    plt.scatter(TSx, fbky)  # Plot uses Timestamp for x-axis
    plt.show()
    print('DONE')


def PreFT():
    df = pd.read_csv('SR1_BCaL_8h.csv')  # , parse_dates=['Timestamp']) doesn't plot properly when loaded in with Timestamp in datetime format
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    df2 = df
    df2['Timestamp'] = pd.to_datetime(df2['Timestamp'], infer_datetime_format=True)
    df3 = df
    df3['Timestamp'] = pd.to_numeric(df3['Timestamp'])
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]
    plt.scatter(TSx, fbky)  # plot data
    TSx2 = pd.to_datetime(dfminiNA.Timestamp, infer_datetime_format=True)
    # plt.scatter(TSx2, fbky)  # plot data
    # TSx3 = pd.to_timedelta(TSx, unit='ns')
    # plt.scatter(TSx3, fbky)  # plot data
    TSx4 = pd.to_numeric(dfminiNA.Timestamp)
    plt.scatter(TSx4, fbky)  # plot data
    print('done')
    '''
    ax = [i for i in range(len(fbky))]
    x1 = dfminiNA.iloc[0, 0]  # single string value
    x2 = pd.to_datetime(TSx, infer_datetime_format=True)  # series of Timestamps
    x3 = pd.to_datetime(x1)  # single timestamp value
    x4 = x2.iloc[0]  # single timestamp value
    '''

def Test1():
    ''' Using Timestamp format. Doesn't show correct pattern.'''
    df = pd.read_csv('SR1_BCaL_8h.csv')
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TSx = pd.to_datetime(dfminiNA.Timestamp, infer_datetime_format=True)
    fbky = dfminiNA.iloc[:, 1]
    plt.scatter(TSx, fbky)  # plot data
    print('done')

def Test2():
    ''' Using Timestamp format. Doesn't show correct pattern.'''
    df = pd.read_csv('SR1_BCaL_8h.csv')
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]

    ax = [i for i in range(len(fbky))]
    x1 = dfminiNA.iloc[:, 0]
    x2 = pd.to_datetime(TSx, infer_datetime_format=True)
    x3 = pd.to_timedelta(TSx)


    plt.scatter(TSx, fbky)  # plot data
    print('done')

# PreFT()
# TSFc()
# Test1()
Test2()


