import pandas as pd
import matplotlib.pyplot as plt

def TSFc():
    '''Using original data format. Shows correct pattern'''
    df = pd.read_csv('../PV Data/SR1_BCaL_8h.csv')
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
    df = pd.read_csv('../PV Data/SR1_BCaL_8h.csv')  # , parse_dates=['Timestamp']) doesn't plot properly when loaded in with Timestamp in datetime format
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
    df = pd.read_csv('../PV Data/SR1_BCaL_8h.csv', parse_dates=['Timestamp'])
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]
    plt.scatter(TSx, fbky)  # plot data
    print('done')

def Test2():
    ''' Using Timestamp format. Doesn't show correct pattern. Converts entire original df.'''
    df = pd.read_csv('../PV Data/SR1_BCaL_8h.csv')
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TS1 = dfminiNA.iloc[:, 0]
    df2 = dfminiNA
    df2['Timestamp'] = pd.to_datetime(df2['Timestamp'], infer_datetime_format=True)
    TS2 = df2.iloc[:, 0]
    df3 = dfminiNA
    df3['Timestamp'] = pd.to_numeric(df3['Timestamp'])
    TS3 = df3.iloc[:, 0]
    TS4 = (TS3 - TS3.values[0])/pow(10,9)
    fbky = dfminiNA.iloc[:, 1]
    plt.figure(1)  # the first figure
    plt.subplot(311)  # the first subplot in the first figure
    plt.scatter(TS1, fbky)  # Timestamp x-axis (unreadable)
    plt.title('Timestamp')
    plt.subplot(312)  # the second subplot in the first figure
    plt.scatter(TS2, fbky)  # datetime x-axis (wrong plot)
    plt.title('datetime')
    plt.subplot(313)    # the third subplot in the first figure
    plt.scatter(TS3, fbky)  # Numeric x-axis (unusable)
    plt.title('Numeric')
    plt.figure(2)   # the second figure
    plt.scatter(TS4, fbky)  # Numeric x-axis (usable)
    plt.xlabel(r'$\mu$s')
    plt.title('FBK starting from ' + TS1.values[0])
    plt.show()
    print('done')

def Test3():
    ''' Using Timestamp format. Doesn't show correct pattern. Only converts column value types.'''
    df = pd.read_csv('../PV Data/SR1_BCaL_8h.csv')
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]

    x0 = TSx
    x1 = pd.to_datetime(TSx, infer_datetime_format=True)
    x2 = pd.to_datetime(x0)
    x3 = pd.to_timedelta(x2)
    x4 = pd.to_numeric(x2)

    ax = x4
    for i in range(len(x4)):
        ax.iloc[i] = x4.iloc[i] - x4.iloc[1]  # doesn't work currently only changes first value of ax

    plt.figure(2)  # open the figure
    plt.subplot(311)  # the first subplot in the first figure
    plt.scatter(x1, fbky)  # Timestamp x-axis (unreadable)
    plt.title('Timestamp')
    plt.subplot(312)  # the second subplot in the first figure
    plt.scatter(x2, fbky)  # datetime x-axis (wrong plot)
    plt.title('datetime')
    plt.subplot(313)  # the third subplot in the first figure
    plt.scatter(x4, fbky)  # Numeric x-axis (unusable)
    plt.title('Numeric')
    plt.show()

    print('done')

# PreFT()
# TSFc()
# Test1()
Test2()
Test3()
print('idk')


