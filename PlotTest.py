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
    # f1, f2 = plt.figure(), plt.figure()
    # af1 = f1.add_subplot(111)
    # af2 = f2.add_subplot(111)
    # af1.plot(TSx)
    # af2.plot(fbky)
    # plt.draw()
    # print 'continue computing'
    # plt.show(block = False)
    # print ('Test plotting 1 done')

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
    df = pd.read_csv("SR1_BCaL_8h.csv", parse_dates=["Timestamp"])
    #df.dropna()
    dfminiNA = df.iloc[1:20, 0:2]
    dfminiNA = dfminiNA.dropna()

    # df = pd.DataFrame({'Timestamp': [pd.to_datetime('2022/06/02 05:44:14.975')]})

    # dfminiNA = dfminiNA.values
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]


    # choose the input and output variables
    x, y = dfminiNA.iloc[:, 0], dfminiNA.iloc[:, 1]
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

'''
df = pd.read_csv("SR1_BCaL_8h.csv")  #, parse_dates=["Timestamp"])
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
'''