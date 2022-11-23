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
    polyline = TS4
    plt.scatter(TS4, fbky)  # plot data
    # plot fit curves
    plt.plot(polyline, m1(polyline), color='orange', label='degree 1')
    plt.plot(polyline, m2(polyline), color='red', label='degree 2')
    plt.plot(polyline, m3(polyline), color='purple', label='degree 3')
    plt.plot(polyline, m4(polyline), color='blue', label='degree 4')
    plt.plot(polyline, m5(polyline), color='green', label='degree 5')
    plt.legend()
    # format plot
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
    CurveFit2()
    corr_calc()

main()

