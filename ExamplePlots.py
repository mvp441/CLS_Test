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

# Multiple plot figures without stopping and waiting for input at each window
def PlotMultiple():
    f1, f2 = pyplot.figure(), pyplot.figure()
    af1 = f1.add_subplot(111)
    af2 = f2.add_subplot(111)
    af1.plot([1,2,3])
    # af2.plot([4,5,6])
    pyplot.draw()
    print 'continue computing'
    pyplot.show(block = False)

def test_func(x, a, b):
    return a * np.sin(b * x)

# define the true objective function
def objective(x, a, b, c, d):
    return a * sin(b - x) + c * x ** 2 + d


def Gauss(x, A, B):
    y = A*np.exp(-1*B*x**2)
    return y

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

    # create scatterplot of x vs. y
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
    dframe = pd.read_csv('peak.csv')
    model = LorentzianModel()
    params = model.guess(dframe['y'], x=dframe['x'])
    result = model.fit(dframe['y'], params, x=dframe['x'])
    print(result.fit_report())

# PlotMultiple()

# FitLine plots on the second window and overwrites the plot created by the first function
# FitLine()
# PandaCuveFit()

