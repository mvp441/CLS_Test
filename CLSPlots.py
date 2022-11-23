import pandas as pd
import numpy as np
import scipy as sci
import matplotlib as mpl
import matplotlib.pyplot as plt
# import moment

mpl.use('TkAgg')

def PandaPlot1():
    df = pd.read_csv("SR1_BCaL_8h.csv")  # read in csv file containing data
    dfminiNA = df.iloc[1:20, 0:2]  # take small data set containing only Timestamp and fbk values
    dfminiNA = dfminiNA.dropna()  # remove Timestamps with NA fbk values
    # separate into individual variables
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]
    dfmNAcs = dfminiNA.cumsum()  # calculate the cumulative summation

    plt.close("all")  # close all open plots
    # first plot
    df.plot()  # plot using pandas method
    plt.show(block = False)  # show plot but don't pause for input
    # second plot
    dfminiNA.plot()  # to show only fbk curve
    plt.show()  # show all plots and wait

#define function to calculate adjusted r-squared
def adjR(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['r_squared'] = 1- (((1-(ssreg/sstot))*(len(y)-1))/(len(y)-degree-1))
    print(results)
    return results

def CurveFit1():
    df = pd.read_csv("SR1_BCaL_8h.csv")  # , parse_dates=["Timestamp"])
    data = df.values
    dfminiNA = df.iloc[1:100, 0:2]
    dfminiNA = dfminiNA.dropna()
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]
    ax = [i for i in range(len(fbky))]
    x1 = dfminiNA.iloc[0, 0]  # single string value
    x2 = pd.to_datetime(TSx, infer_datetime_format=True)  # series of Timestamps
    x3 = pd.to_numeric(x2)  # single timestamp value
    x4 = (x3 - x2.values[0]) / pow(10, 9) # single timestamp value
    # converts to float
    # convert datetime to timedelta for plotting and curve fitting?
    # pltx = mpl.dates.date2num(x4)  #.to_datetime()) # converts to float

    TSx = x4
    # degree 1-4+
    m1 = np.poly1d(np.polyfit(TSx, fbky, 1))
    m2 = np.poly1d(np.polyfit(TSx, fbky, 2))
    m3 = np.poly1d(np.polyfit(TSx, fbky, 3))
    m4 = np.poly1d(np.polyfit(TSx, fbky, 4))
    m5 = np.poly1d(np.polyfit(TSx, fbky, 35))  # should be max 5 put higher to test
    polyline = np.linspace(1, 40, 100)  # fill xdata
    plt.scatter(TSx, fbky)  # plot data
    # plot fit curves
    plt.plot(polyline, m1(polyline), color='orange')
    plt.plot(polyline, m2(polyline), color='red')
    plt.plot(polyline, m3(polyline), color='purple')
    plt.plot(polyline, m4(polyline), color='blue')
    plt.plot(polyline, m5(polyline), color='green')
    # plt.draw()
    plt.show(block=False)
    # print equation term values
    print('y1 = ')
    print(m1)
    # Calculate adjusted R values
    adjR(TSx, fbky, 1)
    adjR(TSx, fbky, 2)
    adjR(TSx, fbky, 3)
    adjR(TSx, fbky, 4)
    adjR(TSx, fbky, 5)
    plt.show()  # call at end to ensure windows dont close


def CurveFit2():
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
    TS4 = (TS3 - TS3.values[0]) / pow(10, 9)
    fbky = dfminiNA.iloc[:, 1]

    # degree 1-4+
    m1 = np.poly1d(np.polyfit(TS4, fbky, 1))
    m2 = np.poly1d(np.polyfit(TS4, fbky, 2))
    m3 = np.poly1d(np.polyfit(TS4, fbky, 3))
    m4 = np.poly1d(np.polyfit(TS4, fbky, 4))
    m5 = np.poly1d(np.polyfit(TS4, fbky, 35))  # should be max 5 put higher to test
    polyline = TS4 #np.linspace(1, 40, 100)  # fill xdata
    plt.scatter(TS4, fbky)  # plot data
    # plot fit curves
    plt.plot(polyline, m1(polyline), color='orange')
    plt.plot(polyline, m2(polyline), color='red')
    plt.plot(polyline, m3(polyline), color='purple')
    plt.plot(polyline, m4(polyline), color='blue')
    plt.plot(polyline, m5(polyline), color='green')
    plt.legend()
    # format plot
    plt.xlabel(r'$\mu$s')
    plt.title('FBK starting from ' + TS1.values[0])

    # plt.draw()
    plt.show(block=False)
    # print equation term values
    print('y1 = ')
    print(m1)
    # Calculate adjusted R values
    adjR(TS4, fbky, 1)
    adjR(TS4, fbky, 2)
    adjR(TS4, fbky, 3)
    adjR(TS4, fbky, 4)
    adjR(TS4, fbky, 5)
    plt.show()  # call at end to ensure windows dont close
    print('done')

#PandaPlot1()
#CurveFit1()
CurveFit2()
