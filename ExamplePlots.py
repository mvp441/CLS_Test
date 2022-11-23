# fit a line to the economic data
import numpy as np
import pandas as pd
from numpy import sin
from numpy import sqrt
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
from lmfit.models import LorentzianModel



def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def test_func(x, a, b):
    return a * np.sin(b * x)

# define the true objective function
def objective(x, a, b, c, d):
    return a * sin(b - x) + c * x ** 2 + d

def Gauss(x, A, B):
    y = A*np.exp(-1*B*x**2)
    return y

def AdjXEx():
    # https://matplotlib.org/2.0.2/users/recipes.html
    pyplot.close('all')
    fig, ax = pyplot.subplots(1)
    ax.plot(r.date, r.close)
    # rotate and align the tick labels so they look better
    fig.autofmt_xdate()
    # use a more precise date string for the x axis locations in the
    # toolbar
    import matplotlib.dates as mdates
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    pyplot.title('fig.autofmt_xdate fixes the labels')

# Multiple plot figures without stopping and waiting for input at each window
def MultiFigPlot():
    f1, f2 = pyplot.figure(), pyplot.figure()
    af1 = f1.add_subplot(111)
    af2 = f2.add_subplot(111)
    af1.plot([1,2,3])
    af2.plot([4,5,6])
    pyplot.draw()
    print 'continue computing'
    pyplot.show(block = False)

def MultiPlotFig():
    # https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    pyplot.figure()
    pyplot.subplot(211)
    pyplot.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    pyplot.subplot(212)
    pyplot.plot(t2, np.cos(2 * np.pi * t2), 'r--')
    pyplot.show()

def MultiMatFig():
    # https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    pyplot.figure(1)  # the first figure
    pyplot.subplot(211)  # the first subplot in the first figure
    pyplot.plot([1, 2, 3])
#    pyplot.title('Check 1')
#    pyplot.suptitle('Check 2')
    pyplot.subplot(212)  # the second subplot in the first figure
    pyplot.plot([4, 5, 6])
    pyplot.figure(2)  # a second figure
    pyplot.plot([4, 5, 6])  # creates a subplot() by default
    pyplot.figure(1)  # figure 1 current; subplot(212) still current
    pyplot.subplot(211)  # make subplot(211) in figure1 current
    pyplot.title('Easy as 1, 2, 3')  # subplot 211 title

def PlotMaskNaN():
    # https://matplotlib.org/stable/gallery/lines_bars_and_markers/masked_demo.html#sphx-glr-gallery-lines-bars-and-markers-masked-demo-py
    x = np.linspace(-np.pi / 2, np.pi / 2, 31)
    y = np.cos(x) ** 3
    # 1) remove points where y > 0.7
    x2 = x[y <= 0.7]
    y2 = y[y <= 0.7]
    # 2) mask points where y > 0.7
    y3 = np.ma.masked_where(y > 0.7, y)
    # 3) set to NaN where y > 0.7
    y4 = y.copy()
    y4[y3 > 0.7] = np.nan
    pyplot.plot(x * 0.1, y, 'o-', color='lightgrey', label='No mask')
    pyplot.plot(x2 * 0.4, y2, 'o-', label='Points removed')
    pyplot.plot(x * 0.7, y3, 'o-', label='Masked values')
    pyplot.plot(x * 1.0, y4, 'o-', label='NaN values')
    pyplot.legend()
    pyplot.title('Masked and NaN data')
    pyplot.show()

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

# Method for curve fitting using a basis function
def FitLine():
    # https://machinelearningmastery.com/curve-fitting-with-python/
    # load the dataset
    url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
    dataframe = read_csv(url, header=None)
    data = dataframe.values
    # choose the input and output variables
    x, y = data[:, 4], data[:, -1]
    # curve fit
    popt, _ = curve_fit(objective, x, y)
    # summarize the parameter values
    a, b, c, d = popt
    print(popt)
    # plot input vs output
    pyplot.scatter(x, y)
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = arange(min(x), max(x), 1)
    # calculate the output for the range
    y_line = objective(x_line, a, b, c, d)
    # create a line plot for the mapping function
    pyplot.plot(x_line, y_line, '--', color='red')
    pyplot.xlim([x[0]-1, x[-1]+1])
    pyplot.title("Fit Curve")
    pyplot.show(block = False)
    print ('Test plotting 1 done')
    pyplot.show()

def CurveFit ():
    # https://scipy-lectures.org/intro/scipy/auto_examples/plot_curve_fit.html
    np.random.seed(0)
    x_data = np.linspace(-5, 5, num=50)
    y_data = 2.9 * np.sin(1.5 * x_data) + np.random.normal(size=50)
    params, params_covariance = curve_fit(test_func, x_data, y_data, p0=[2, 2])
    print(params)
    pyplot.figure(figsize=(6, 4))
    pyplot.scatter(x_data, y_data, label='Data')
    pyplot.plot(x_data, test_func(x_data, params[0], params[1]), label='Fitted function')
    pyplot.legend(loc='best')
    pyplot.show()

def PandaCuveFit():
    # Step 1: Create and visualize the data
    # create DataFrame
    df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                       'y': [3, 14, 23, 25, 23, 15, 9, 5, 9, 13, 17, 24, 32, 36, 46]})
    # create scatter plot of x vs. y
    pyplot.scatter(df.x, df.y)

    # Step 2: Fit several curves
    # fit polynomial models up to degree 5
    model1 = np.poly1d(np.polyfit(df.x, df.y, 1))
    model2 = np.poly1d(np.polyfit(df.x, df.y, 2))
    model3 = np.poly1d(np.polyfit(df.x, df.y, 3))
    model4 = np.poly1d(np.polyfit(df.x, df.y, 4))
    model5 = np.poly1d(np.polyfit(df.x, df.y, 5))
    # create scatterplot
    polyline = np.linspace(1, 15, 50)
    pyplot.scatter(df.x, df.y)
    # add fitted polynomial lines to scatterplot
    pyplot.plot(polyline, model1(polyline), color='green')
    pyplot.plot(polyline, model2(polyline), color='red')
    pyplot.plot(polyline, model3(polyline), color='purple')
    pyplot.plot(polyline, model4(polyline), color='blue')
    pyplot.plot(polyline, model5(polyline), color='orange')
    pyplot.show()

    # Step 2.5: Calculate adjusted R-squared of each model
    adjR(df.x, df.y, 1)
    adjR(df.x, df.y, 2)
    adjR(df.x, df.y, 3)
    adjR(df.x, df.y, 4)
    adjR(df.x, df.y, 5)

    # Step 3: Visualize the Final Curve
    # fit fourth-degree polynomial
    model4 = np.poly1d(np.polyfit(df.x, df.y, 4))
    # define scatter plot
    polyline = np.linspace(1, 15, 50)
    pyplot.scatter(df.x, df.y)
    # add fitted polynomial curve to scatter plot
    pyplot.plot(polyline, model4(polyline), '--', color='red')
    pyplot.show()

def PandaFit2():
    # https://lmfit.github.io/lmfit-py/examples/example_use_pandas.html#sphx-glr-download-examples-example-use-pandas-py
    dframe = pd.read_csv('peak.csv')  # CSV file with data could not be downloaded from site
    model = LorentzianModel()
    params = model.guess(dframe['y'], x=dframe['x'])
    result = model.fit(dframe['y'], params, x=dframe['x'])
    print(result.fit_report())

def OOStyle():
    # https://matplotlib.org/stable/tutorials/introductory/quick_start.html
    x = np.linspace(0, 2, 100)  # Sample data.
    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig, ax = pyplot.subplots()  #figsize=(5, 2.7), layout='constrained') doesn't work with layout option
    ax.plot(x, x, label='linear')  # Plot some data on the axes.
    ax.plot(x, x ** 2, label='quadratic')  # Plot more data on the axes...
    ax.plot(x, x ** 3, label='cubic')  # ... and some more.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("Simple Plot")  # Add a title to the axes.
    ax.legend();  # Add a legend.
    pyplot.show()  # Display figure

def PyPlotStyle():
    # https://matplotlib.org/stable/tutorials/introductory/quick_start.html
    x = np.linspace(0, 2, 100)  # Sample data.
    pyplot.figure(figsize=(5, 2.7))  # , layout='constrained')
    pyplot.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
    pyplot.plot(x, x ** 2, label='quadratic')  # etc.
    pyplot.plot(x, x ** 3, label='cubic')
    pyplot.xlabel('x label')
    pyplot.ylabel('y label')
    pyplot.title("Simple Plot")
    pyplot.legend();
    pyplot.show()

# MultiFigPlot()
# MultiPlotFig()
# MultiMatFig()  # Only plots if paused with debugger and stepped through
# FitLine()  # FitLine plots on the second window and overwrites the plot created by the first function
# PandaCurveFit()
# PandaFit2()
# OOStyle()
# PyPlotStyle()


