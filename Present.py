import pandas as pd
import numpy as np
import csv
import scipy as sci
import scipy.stats
import matplotlib as mpl
import matplotlib.pyplot as plt

def print_data(df):
    for column in df:
        print(df[column])
        print('\n')

def get_list_desc(df):
    dfdesc = list()
    dfdesc.append(df.describe())
    for column in df:
        dfdesc.append(df[column].describe())
    return dfdesc

def get_dict_desc(df):
    dfdesc = {}
    for column in df:
        dfdesc[column] = df[column].describe()
    return dfdesc

def PandasTest3():
    df = pd.read_csv("SR1_BCaL_8h.csv")

    print(df.columns)
    print(df)

    dfminiNA = df.iloc[1:100, 0:4]
    print("dfmini with N/A")
    print(dfminiNA)

    dfmini = dfminiNA.copy()

    dfminiNA['Timestamp'] = pd.to_datetime(dfminiNA['Timestamp'], infer_datetime_format=True)
    dfminiNA['Timestamp'] = pd.to_numeric(dfminiNA['Timestamp'])

    TSNA = dfminiNA.iloc[:, [0]]
    fbkNA = dfminiNA.iloc[:, [1]]
    mAChangeNA = dfminiNA.iloc[:, [2]]
    timeConstantNA = dfminiNA.iloc[:, [3]]

    NA_dict_desc = get_dict_desc(dfminiNA)
    print("columns with N/A")
    print(dfminiNA)
    print("description with N/A")
    print_data(NA_dict_desc)

    TS = TSNA.dropna()
    fbk = fbkNA.dropna()
    mAChange = mAChangeNA.dropna()
    timeConstant = timeConstantNA.dropna()
    print("columns without N/A")
    print(fbk)
    print(mAChange)
    print(timeConstant)
    print("description N/A dropped")
    print(fbk.describe())
    print(mAChange.describe())
    print(timeConstant.describe())

    dfmini0 = dfmini.copy().fillna(0)
    dfm0_dict_desc = get_dict_desc(dfmini0)
    print("columns with N/A filled by 0")
    print(dfmini0)
    print("description N/A 0")
    print_data(dfm0_dict_desc)

    dfmmean = dfmini.copy()
    for column in dfmmean.columns[1:]:
        mean = dfmmean[column].mean()
        dfmmean[column] = dfmmean[column].fillna(mean)
    dfmean_dict_desc = get_dict_desc(dfmmean)
    print("columns with N/A filled by mean")
    print(dfmmean)
    print("description N/A mean")
    print_data(dfmean_dict_desc)

    dfmmedian = dfmini.copy()
    for column in dfmmedian.columns[1:]:
        median = dfmmedian[column].mean()
        dfmmedian[column] = dfmmedian[column].fillna(median )
    dfmedian_dict_desc = get_dict_desc(dfmmedian)
    print("columns with N/A filled by median")
    print(dfmmedian)
    print("description N/A median")
    print_data(dfmedian_dict_desc)

    dfmmode = dfmini.copy().mode()
    for column in dfmmode.columns[1:]:
        mode = dfmmode[column].mode()
        dfmmode[column] = dfmmode[column].fillna(mode)
    dfmode_dict_desc = get_dict_desc(dfmmode)
    print("columns with N/A filled by mode")
    print(dfmmode)
    print("description N/A mode")
    print_data(dfmode_dict_desc)

    dfminipad = dfmini.copy().fillna(method='pad')
    dfmpad_dict_desc = get_dict_desc(dfminipad)
    print("columns fill N/A padded")
    print(dfminipad)
    print("description N/A padded")
    print_data(dfmpad_dict_desc)

    dfminibackfill = dfmini.copy().fillna(method='backfill')
    dfmbackfill_dict_desc = get_dict_desc(dfminibackfill)
    print("columns fill N/A padded")
    print(dfminibackfill)
    print("description N/A padded")
    print_data(dfmbackfill_dict_desc)

    dfminibf = dfmini.copy().fillna(method='bfill')
    dfmbf_dict_desc = get_dict_desc(dfminibf)
    print("columns fill N/A padded")
    print(dfminibf)
    print("description N/A padded")
    print_data(dfmbf_dict_desc)

    dfminiff = dfmini.copy().fillna(method='ffill')
    dfmff_dict_desc = get_dict_desc(dfminiff)
    print("columns fill N/A padded")
    print(dfminiff)
    print("description N/A padded")
    print_data(dfmff_dict_desc)

    TSNAx = (TSNA - TSNA.values[0]) / pow(10, 9)
    TSx = (TS - TS.values[0]) / pow(10, 9)

    df0 = dfmini0.copy()
    df0['Timestamp'] = pd.to_datetime(df0['Timestamp'], infer_datetime_format=True)
    df0['Timestamp'] = pd.to_numeric(df0['Timestamp'])
    TS0 = df0.iloc[:, 0]
    TSx0 = (TS0 - TS0.values[0]) / pow(10, 9)
    fbky0 = df0.iloc[:, 1]

    dfp = dfminipad.copy()
    dfp['Timestamp'] = pd.to_datetime(dfp['Timestamp'], infer_datetime_format=True)
    dfp['Timestamp'] = pd.to_numeric(dfp['Timestamp'])
    TSp = dfp.iloc[:, 0]
    TSxp = (TSp - TSp.values[0]) / pow(10, 9)
    fbkyp = dfp.iloc[:, 1]

    dfback = dfminibackfill.copy()
    dfback['Timestamp'] = pd.to_datetime(dfback['Timestamp'], infer_datetime_format=True)
    dfback['Timestamp'] = pd.to_numeric(dfback['Timestamp'])
    TSback = dfback.iloc[:, 0]
    TSxback = (TSback - TSback.values[0]) / pow(10, 9)
    fbkyback = dfback.iloc[:, 1]

    dfbf = dfminibf.copy()
    dfbf['Timestamp'] = pd.to_datetime(dfbf['Timestamp'], infer_datetime_format=True)
    dfbf['Timestamp'] = pd.to_numeric(dfbf['Timestamp'])
    TSbf = dfbf.iloc[:, 0]
    TSxbf = (TSbf - TSbf.values[0]) / pow(10, 9)
    fbkybf = dfbf.iloc[:, 1]

    dfff = dfminiff.copy()
    dfff['Timestamp'] = pd.to_datetime(dfff['Timestamp'], infer_datetime_format=True)
    dfff['Timestamp'] = pd.to_numeric(dfff['Timestamp'])
    TSff = dfff.iloc[:, 0]
    TSxff = (TSff - TSff.values[0]) / pow(10, 9)
    fbkyff = dfff.iloc[:, 1]

    plt.plot(TSNAx, fbkNA, 'X', label='With NaN')
    plt.show(block=False)
    # plt.plot(TSx,  fbk, 'o-', label='No NaN')
    #plt.plot(TSx0, fbky0, 'x', label='NaN = 0')
    plt.plot(TSxp, fbkyp, '*', label='NaN padded')
    plt.plot(TSxback, fbkyback, '.', label='NaN backfill')
    plt.plot(TSxbf, fbkybf, '-', label='NaN bfill')
    plt.plot(TSxff, fbkyff, '+', label='NaN ffill')
    plt.legend()
    plt.title('Masked and NaN data')
    plt.show()

def PandaPlot1():
    df = pd.read_csv("SR1_BCaL_8h.csv")  # read in csv file containing data
    dfminiNA = df.iloc[1:20, 0:2]  # take small data set containing only Timestamp and fbk values
    dfminiNA = dfminiNA.dropna()  # remove Timestamps with NA fbk values
    plt.close("all")  # close all open plots
    # first plot
    df.plot(title='Entire Dataframe')  # plot using pandas method
    plt.show(block = False)  # show plot but don't pause for input
    # second plot
    dfminiNA.plot(title='Mini Dataframe')  # to show only fbk curve
    plt.show()  # show all plots and wait

def Test2():
    ''' Using Timestamp format. Doesn't show correct pattern. Converts entire original df.'''
    df = pd.read_csv('SR1_BCaL_8h.csv')
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TS1 = dfminiNA.iloc[:, 0]
    df2 = dfminiNA.copy()
    df2['Timestamp'] = pd.to_datetime(df2['Timestamp'], infer_datetime_format=True)
    TS2 = df2.iloc[:, 0]
    df3 = df2.copy()
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

def adjR(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['r_squared'] = 1-(((1-(ssreg/sstot))*(len(y)-1))/(len(y)-degree-1))
    return results

def CurveFit2():
    df = pd.read_csv('SR1_BCaL_8h.csv')
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TS1 = dfminiNA.iloc[:, 0]
    df2 = dfminiNA.copy()
    df2['Timestamp'] = pd.to_datetime(df2['Timestamp'], infer_datetime_format=True)
    TS2 = df2.iloc[:, 0]
    df3 = df2.copy()
    df3['Timestamp'] = pd.to_numeric(df3['Timestamp'])
    TS3 = df3.iloc[:, 0]
    TS4 = (TS3 - TS3.values[0]) / pow(10, 9)
    fbky = dfminiNA.iloc[:, 1]
    # degree 1-4+
    m1 = np.poly1d(np.polyfit(TS4, fbky, 1))
    m2 = np.poly1d(np.polyfit(TS4, fbky, 2))
    m3 = np.poly1d(np.polyfit(TS4, fbky, 3))
    m4 = np.poly1d(np.polyfit(TS4, fbky, 4))
    m5 = np.poly1d(np.polyfit(TS4, fbky, 5))  # should be max 5 put higher to test
    mhigh = np.poly1d(np.polyfit(TS4, fbky, 35))
    polyline = TS4
    plt.figure(1)
    plt.scatter(TS4, fbky)  # plot data
    # plot fit curves
    plt.plot(polyline, m1(polyline), color='orange', label='degree 1')
    plt.plot(polyline, m2(polyline), color='red', label='degree 2')
    plt.plot(polyline, m3(polyline), color='purple', label='degree 3')
    plt.plot(polyline, m4(polyline), color='blue', label='degree 4')
    plt.plot(polyline, m5(polyline), color='green', label='degree 5')
#    plt.plot(polyline, mhigh(polyline), color='green', label='degree 35')
    plt.legend()
    # format plot
    plt.xlabel(r'$\mu$s')
    plt.title('FBK starting from ' + TS1.values[0])
    plt.figure(2)
    plt.scatter(TS4, fbky)  # plot data
    plt.plot(polyline, mhigh(polyline), color='green', label='degree 35')
    plt.legend()
    plt.xlabel(r'$\mu$s')
    plt.title('FBK starting from ' + TS1.values[0])
    # plt.draw()
    plt.show(block=False)
    # Calculate adjusted R values
    m1aR = adjR(TS4, fbky, 1)
    m2aR = adjR(TS4, fbky, 2)
    m3aR = adjR(TS4, fbky, 3)
    m4aR = adjR(TS4, fbky, 4)
    m5aR = adjR(TS4, fbky, 5)
    mhighaR = adjR(TS4, fbky, 35)
    # print equation term values
    print('y1 = ')
    print(m1)
    print(m1aR)
    print('\ny2 = ')
    print(m2)
    print(m2aR)
    print('\ny3 = ')
    print(m3)
    print(m3aR)
    print('\ny4 = ')
    print(m4)
    print(m4aR)
    print('\ny5 = ')
    print(m5)
    print(m5aR)
    print('\ny35 = ')
    print(mhigh)
    print(mhighaR)
    plt.show()  # call at end to ensure windows don't close

def corr_calc():
    file = open("SR1_BCaL_8h.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    TimeStamp = []
    fbk = []
    Change = []
    TimeConstant = []
    for row in csvreader:
        rows.append(row)
        TimeStamp.append(row[0])
        fbk.append(row[1])
        Change.append(row[2])
        TimeConstant.append(row[3])
    print('\ninitial Change length: ' + str(len(Change)))
    print('initial fbkNA length: ' + str(len(fbk)))
    print('initial TimeConstant length: ' + str(len(TimeConstant)) + '\n')
    valueToBeRemoved = 'N/A'
    Change = filter(lambda val: val != valueToBeRemoved, Change)
    try:
        while True:
            fbk.remove(valueToBeRemoved)
    except ValueError:
        pass
    TimeConstant = [value for value in TimeConstant if value != valueToBeRemoved]
    print('final Change length: ' + str(len(Change)))
    print('final fbkNA length: ' + str(len(fbk)))
    print('final TimeConstant length: ' + str(len(TimeConstant)) + '\n')
    fbk = [float(x) for x in fbk]
    Change = [float(x) for x in Change]
    print('numpy corrcoef:')
    print(np.corrcoef(fbk, Change))
    print('\nSciPy Pearsonr:' + str(sci.stats.pearsonr(fbk, Change)))
    print(sci.stats.spearmanr(fbk, Change))
    print(sci.stats.kendalltau(fbk, Change))
    file.close()

def main():
    PandaPlot1()
    Test2()
    PandasTest3()
    CurveFit2()
    corr_calc()

PandasTest3()
#corr_calc()
#main()

