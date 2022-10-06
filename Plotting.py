import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#from scipy import optimize

def test_func(x, a, b):
    return a * np.sin(b * x)

mpl.use('TkAgg')


df = pd.read_csv("SR1_BCaL_8h.csv")
df.dropna()

dfminiNA = df.iloc[1:20, 0:2]
dfminiNA = dfminiNA.dropna()
TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]

# seperate df into mini of each variable to plot

dfmNAcs = dfminiNA.cumsum() #calculate the cumulative summation

plt.close("all") #close all open plots

#first plot
#plt.figure(1) #open plot figure
df.plot() #plot
#plt.show() #display plot

print('Done1')

#plt.figure(2)
dfminiNA.plot() #to show only fbk curve
#plt.show()
#dfminiNA.iloc[1].plot.bar() #causes error
#dfmNAcs.plot(x="Timestamp", y="fbk") #causes error
#plt.axline(0,color="k") #causes error

print('Done2')

plt.show()

#  params, params_covariance = optimize.curve_fit(test_func, TSx, fbky, p0=[2, 2])
# print(params)
#
# plt.figure(figsize=(6, 4))
# plt.scatter(TSx, fbky, label='Data')
# plt.plot(TSx, test_func(TSx, params[0], params[1]), label='Fitted function')
# plt.legend(loc='best')
# plt.show()
#
# print('Done3')

