import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sci

from scipy import optimize

def test_func(x, a, b):
    return a * np.sin(b * x)

def Gauss(x, A, B):
    y = A*np.exp(-1*B*x**2)
    return y

mpl.use('TkAgg')


df = pd.read_csv("SR1_BCaL_8h.csv")
df.dropna()



dfminiNA = df.iloc[1:100, 0:2]
dfminiNA = dfminiNA.dropna()
TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]

ax = []
ax = [i for i in range(len(fbky))]
#print(ax)
TSx = ax
# dfminiNA.astype('int32').dtypes


# seperate df into mini of each variable to plot

dfmNAcs = dfminiNA.cumsum() #calculate the cumulative summation

plt.close("all") #close all open plots

#first plot
#plt.figure(1) #open plot figure


#df.plot() #plot # working still


#plt.show() #display plot

#print('Done1')

#plt.figure(2)
#dfminiNA.plot() #to show only fbk curve also working
#plt.show()
print('Done 1')

#plt.show()
#dfminiNA.iloc[1].plot.bar() #causes error
#dfmNAcs.plot(x="Timestamp", y="fbk") #causes error
#plt.axline(0,color="k") #causes error

print('Done 2')

m1 = np.poly1d(np.polyfit(TSx, fbky, 1))
m2 = np.poly1d(np.polyfit(TSx, fbky, 2))
m3 = np.poly1d(np.polyfit(TSx, fbky, 3))
m4 = np.poly1d(np.polyfit(TSx, fbky, 4))
m5 = np.poly1d(np.polyfit(TSx, fbky, 30)) #should be max 5 put higher to test

polyline = np.linspace(1, 40, 100)
plt.scatter(TSx, fbky)

plt.plot(polyline, m1(polyline), color='orange')
plt.plot(polyline, m2(polyline), color='red')
plt.plot(polyline, m3(polyline), color='purple')
plt.plot(polyline, m4(polyline), color='blue')
plt.plot(polyline, m5(polyline), color='green')




plt.show()

#  params, params_covariance = optimize.curve_fit(test_func, TSx, fbky, p0=[2, 2])
#  print(params)
#
# plt.figure(figsize=(6, 4))
# plt.scatter(TSx, fbky, label='Data')
# plt.plot(TSx, test_func(TSx, params[0], params[1]), label='Fitted function')
# plt.legend(loc='best')
# plt.show()
#
print('Done3')

