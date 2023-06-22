import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('TkAgg')

df = pd.read_csv("../PV_Data/SR1_BCaL_8h.csv")
df.dropna()

dfminiNA = df.iloc[1:20, 0:2]
dfminiNA = dfminiNA.dropna()
TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]

# separate df into mini of each variable to plot

dfmNAcs = dfminiNA.cumsum()  # calculate the cumulative summation

plt.close("all")  # close all open plots

# f1, f2 = plt.figure(), plt.figure()
# af1 = f1.add_subplot(111)
# af2 = f2.add_subplot(111)
# af1.plot([1,2,3])
# af2.plot(fbky)
# plt.draw()
# print 'continue computing'
# plt.show(block = False)
# print ('Test ploting 1 done')

#first plot
#plt.figure(1) #open plot figure
df.plot() #plot
plt.show(block = False)

#print('Test plot 2 done')

#plt.figure(2)
dfminiNA.plot() #to show only fbk curve
plt.show()
#dfminiNA.iloc[1].plot.bar()
#dfmNAcs.plot(x="Timestamp", y="fbk")
#plt.axline(0,color="k")