# fit a line to the economic data
import numpy as np
from numpy import sin
from numpy import sqrt
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot


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

# PlotMultiple()

# FitLine plots on the second window and overwrites the plot created by the first function
# FitLine()


