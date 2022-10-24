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


df = pd.read_csv("SR1_BCaL_8h.csv")#, parse_dates=["Timestamp"])
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




# choose the input and output variables
x, y = dfminiNA[:, 0], dfminiNA[:, 1]
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




# seperate df into mini of each variable to plot
# dfmNAcs = dfminiNA.cumsum() #calculate the cumulative summation
model = LorentzianModel()
params = model.guess(fbky, x=TSx)
result = model.fit(fbky, params, TSx)
print(result.fit_report())
result.plot_fit()
