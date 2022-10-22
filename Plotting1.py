import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sci
import datetime

from scipy import optimize

def test_func(x, a, b):
    return a * np.sin(b * x)

def objective(x, a, b, c, d):
	return a * np.sin(b - x) + c * x**2 + d


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

mpl.use('TkAgg')


df = pd.read_csv("SR1_BCaL_8h.csv", parse_dates=["Timestamp"])
data = df.values
df.dropna()



dfminiNA = df.iloc[1:100, 0:2]
dfminiNA = dfminiNA.dropna()
TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]



date1 = TSx.min
date2 = TSx.max
datetime.resolution(date1, date2)

td = date2 - date1

start = TSx.iloc[0, 0]
end = TSx.iloc[-1, 0]
index = pd.date_range(start, end)
print(index)


TSx = TSx.astype('float64')
ax = []
ax = [i for i in range(len(fbky))]
#print(ax)

# dfminiNA.astype('int32').dtypes


# seperate df into mini of each variable to plot

#dfmNAcs = dfminiNA.cumsum() #calculate the cumulative summation


params, params_covariance = optimize.curve_fit(test_func, TSx, fbky, p0=[2, 2])
print(params)


plt.close("all") #close all open plots

#first plot
#plt.figure(1) #open plot figure


#df.plot() #plot # working still


#plt.show() #display plot

#print('Done1')

#plt.figure(2)
#dfminiNA.plot() #to show only fbk curve also working
#plt.show()


#plt.show()
#dfminiNA.iloc[1].plot.bar() #causes error
#dfmNAcs.plot(x="Timestamp", y="fbk") #causes error
#plt.axline(0,color="k") #causes error


# plt.ion() #enables interactive mode

#degree 1-4+
m1 = np.poly1d(np.polyfit(TSx, fbky, 1))
m2 = np.poly1d(np.polyfit(TSx, fbky, 2))
m3 = np.poly1d(np.polyfit(TSx, fbky, 3))
m4 = np.poly1d(np.polyfit(TSx, fbky, 4))
m5 = np.poly1d(np.polyfit(TSx, fbky, 5)) #should be max 5 put higher to test

polyline = np.linspace(1, 40, 100)
plt.scatter(TSx, fbky)

plt.plot(polyline, m1(polyline), color='orange')
plt.plot(polyline, m2(polyline), color='red')
plt.plot(polyline, m3(polyline), color='purple')
plt.plot(polyline, m4(polyline), color='blue')
plt.plot(polyline, m5(polyline), color='green')


#plt.draw()
plt.show(block = False)

#print equation term values
print('y1 = ')
print(m1)

# Calculate adjusted R values
adjR(TSx, fbky, 1)
adjR(TSx, fbky, 2)
adjR(TSx, fbky, 3)
adjR(TSx, fbky, 4)
adjR(TSx, fbky, 5)
#print('Done 1')
#print('Done 2')

params, params_covariance = optimize.curve_fit(test_func, TSx, fbky, p0=[2, 2])
print(params)

plt.figure(figsize=(6, 4))
plt.scatter(TSx, fbky, label='Data')
plt.plot(TSx, test_func(TSx, params[0], params[1]), label='Fitted function')
plt.legend(loc='best')
plt.show()


# f1, f2 = plt.figure(), plt.figure()
# af1 = f1.add_subplot(111)
# af2 = f2.add_subplot(111)
# af1.plot(TSx)
# af2.plot(fbky)
# plt.draw()
# print 'continue computing'
# plt.show(block = False)
# print ('Test ploting 1 done')

plt.show() # call at end to ensure windows dont close

#print('Done 3')

