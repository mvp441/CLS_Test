import numpy as np
from numpy import sin
from numpy import sqrt
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import dates
import pandas as pd
from lmfit.models import LorentzianModel
import time

mpl.use('TkAgg')

def MultiFigPlot():
    f1, f2 = plt.figure(), plt.figure()
    af1 = f1.add_subplot(111)
    af2 = f2.add_subplot(111)
    af1.plot([1,2,3])
    af2.plot([4,5,6])
    plt.draw()
    print 'continue computing'
    plt.show(block = False)

def TestPlot1(TS1, TS2, fbky):
    f1, f2 = plt.figure(), plt.figure()
    af1 = f1.add_subplot(111)
    af2 = f2.add_subplot(111)
    af1.plot(TS1, fbky)
    af2.plot(TS2, fbky)
    plt.draw()
    print 'continue computing'
    plt.show(block = False)
    print ('Test plotting 1 done')

def MultiMatFig():
    # https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    plt.figure(1)  # the first figure
    plt.subplot(211)  # the first subplot in the first figure
    plt.plot([1, 2, 3])
#    pyplot.title('Check 1')
#    pyplot.suptitle('Check 2')
    plt.subplot(212)  # the second subplot in the first figure
    plt.plot([4, 5, 6])
    plt.figure(2)  # a second figure
    plt.plot([4, 5, 6])  # creates a subplot() by default
    plt.figure(1)  # figure 1 current; subplot(212) still current
    plt.subplot(211)  # make subplot(211) in figure1 current
    plt.title('Easy as 1, 2, 3')  # subplot 211 title

def PlotMaskNan():
    df = pd.read_csv('../PV_Data/SR1_BCaL_8h.csv')
    dfmini = df.iloc[1:100, 0:2]
    dfminiNA = dfmini.dropna()
    TS1 = dfminiNA.iloc[:, 0]
    df2 = dfminiNA
    df2['Timestamp'] = pd.to_datetime(df2['Timestamp'], infer_datetime_format=True)
    TS2 = df2.iloc[:, 0]
    df3 = dfminiNA
    df3['Timestamp'] = pd.to_numeric(df3['Timestamp'])
    TS3 = df3.iloc[:, 0]
    TS4 = (TS3 - TS3.values[0]) / pow(10, 9)
    fbky = dfminiNA.iloc[:, 1]
    x = TS4
    y = fbky
    # 1) remove points where y > 0.7
    x2 = x[y == 'NaN']
    y2 = y[y == 'NaN']
    # 2) mask points where y > 0.7
    y3 = np.ma.masked_where(y == 'NaN', y)
    # 3) set to NaN where y > 0.7
    y4 = y.copy()
    y4[y3 == 'NaN'] = np.nan
    plt.plot(x * 0.1, y, 'o-', color='lightgrey', label='No mask')
    plt.plot(x2 * 0.4, y2, 'o-', label='Points removed')
    plt.plot(x * 0.7, y3, 'o-', label='Masked values')
    plt.plot(x * 1.0, y4, 'o-', label='NaN values')
    plt.legend()
    plt.title('Masked and NaN data')
    plt.show()
    print('done')

def PandaPlot1():
    df = pd.read_csv("../PV_Data/SR1_BCaL_8h.csv")  # read in csv file containing data
    dfminiNA = df.iloc[1:20, 0:2]  # take small data set containing only Timestamp and fbk values
    dfminiNA = dfminiNA.dropna()  # remove Timestamps with NA fbk values
    # separate into individual variables
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]
    dfmNAcs = dfminiNA.cumsum()  # calculate the cumulative summation

    plt.close("all")  # close all open plots
    # first plot
    plt.figure(1)
    df.plot()  # plot using pandas method
    plt.show(block = False)  # show plot but don't pause for input
    # second plot
    dfminiNA.plot()  # to show only fbk curve
    plt.show()  # show all plots and wait

# define the true objective function
def objective(x, a, b, c, d):
    return a * sin(b - x) + c * x ** 2 + d

def CurveFit1():
    df = pd.read_csv("../PV_Data/SR1_BCaL_8h.csv", parse_dates=["Timestamp"])
    #df.dropna()
    dfminiNA = df.iloc[1:20, 0:2]
    dfminiNA = dfminiNA.dropna()

    # df = pd.DataFrame({'Timestamp': [pd.to_datetime('2022/06/02 05:44:14.975')]})

    # dfminiNA = dfminiNA.values
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]


    # choose the input and output variables
    x, y = dfminiNA.iloc[:, 0], dfminiNA.iloc[:, 1]
    y = fbky
    x = [i for i in range(len(y))]  # replace with actual x values depending on what information is necessary
    # curve fit
    popt, _ = curve_fit(objective, x, y)
    # summarize the parameter values
    a, b, c, d = popt
    print(popt)
    # plot input vs output
    plt.scatter(x, y)
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = arange(min(x), max(x), 1)
    # calculate the output for the range
    y_line = objective(x_line, a, b, c, d)
    # create a line plot for the mapping function
    plt.plot(x_line, y_line, '--', color='red')
    plt.show()

def Test0():
    df = pd.read_csv("../PV_Data/SR1_BCaL_8h.csv", parse_dates=["Timestamp"])
    data = df.values

    dfminiNA = df.iloc[1:100, 0:2]
    dfminiNA = dfminiNA.dropna()
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]

    date1 = TSx.min
    date2 = TSx.max
    # datetime.resolution(date1, date2)

    # td = date2 - date1

    #start = TSx.iloc[0, 0]
    #end = TSx.iloc[-1, 0]
    #index = pd.date_range(start, end)
    #print(index)

    #TSx = TSx.astype('float64')
    ax = []
    ax = [i for i in range(len(fbky))]
    #print(ax)
    TSx = ax
    # dfminiNA.astype('int32').dtypes

    # seperate df into mini of each variable to plot
    # dfmNAcs = dfminiNA.cumsum() #calculate the cumulative summation
    model = LorentzianModel()
    params = model.guess(fbky, x=TSx)
    result = model.fit(fbky, params, TSx)
    print(result.fit_report())
    result.plot_fit()

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
    df = pd.read_csv("../PV_Data/SR1_BCaL_8h.csv")

    print(df.columns)
    print(df)

    dfminiNA = df.iloc[1:20, 0:4]
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

    print('done')

#MultiFigPlot()
#MultiMatFig()
#PlotMaskNan()
PandasTest3()
#Test0()
#CurveFit1()