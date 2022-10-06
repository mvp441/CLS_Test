import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

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
plt.show() #display plot


#plt.figure(2)
dfminiNA.plot() #to show only fbk curve
plt.show()
#dfminiNA.iloc[1].plot.bar() #causes error
#dfmNAcs.plot(x="Timestamp", y="fbk") #causes error
#plt.axline(0,color="k") #causes error

print('Done1')
print('Done2')
print('Done3')

