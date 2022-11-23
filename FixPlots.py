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

# define the true objective function
def objective(x, a, b, c, d):
    return a * sin(b - x) + c * x ** 2 + d

def test_func(x, a, b):
    return a * np.sin(b * x)

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
    print('done')

def original_functions():
    FitLine()
    CurveFit()
    PlotMaskNaN()

original_functions()