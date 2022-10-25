import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('TkAgg')

def MultiFigPlot():
    f1, f2 = plt.figure(), plt.figure()
    af1 = f1.add_subplot(111)
    af2 = f2.add_subplot(111)
    af1.plot([1,2,3])
    af2.plot([4,5,6])
    plt.draw()
    print 'continue computing'
    plt.show(block = False)

def MultiMatFig():
    # https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    plt.figure(1)  # the first figure
    plt.subplot(211)  # the first subplot in the first figure
    plt.plot([1, 2, 3])
#    pyplot.title('Check 1')
#    pyplot.suptitle('Check 2')
    plt.subplot(212)  # the second subplot in the first figure
    plt.plot([4, 5, 6])
    plt.figure(2)  # a second figure
    plt.plot([4, 5, 6])  # creates a subplot() by default
    plt.figure(1)  # figure 1 current; subplot(212) still current
    plt.subplot(211)  # make subplot(211) in figure1 current
    plt.title('Easy as 1, 2, 3')  # subplot 211 title

df = pd.read_csv("SR1_BCaL_8h.csv")  # read in csv file containing data
dfminiNA = df.iloc[1:20, 0:2]  # take small data set containing only Timestamp and fbk values
dfminiNA = dfminiNA.dropna()  # remove Timestamps with NA fbk values
# separate into individual variables
TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]
dfmNAcs = dfminiNA.cumsum()  # calculate the cumulative summation

plt.close("all")  # close all open plots
# first plot
plt.figure(1)

df.plot()  # plot using pandas method
plt.show(block = False)  # show plot but don't pause for input
# second plot
dfminiNA.plot() #to show only fbk curve
# dfminiNA.iloc[1].plot.bar()
#dfminiNA.plot(x="Timestamp", y="fbk")
plt.axline(0, color="k")
plt.show()  # show all plots and wait
