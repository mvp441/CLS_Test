# fit a line to the economic data
from numpy import sin
from numpy import sqrt
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
from matplotlib import dates
import pandas as pd
from lmfit.models import LorentzianModel
import time

# define the true objective function
def objective(x, a, b, c, d):
    return a * sin(b - x) + c * x ** 2 + d

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
x = [i for i in range(len(y))]
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
pyplot.show()


'''
# seperate df into mini of each variable to plot
# dfmNAcs = dfminiNA.cumsum() #calculate the cumulative summation
model = LorentzianModel()
params = model.guess(fbky, x=TSx)
result = model.fit(fbky, params, TSx)
print(result.fit_report())
result.plot_fit()
'''
