import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('TkAgg')

def PandaPlot1():
    df = pd.read_csv("SR1_BCaL_8h.csv")  # read in csv file containing data
    dfminiNA = df.iloc[1:20, 0:2]  # take small data set containing only Timestamp and fbk values
    dfminiNA = dfminiNA.dropna()  # remove Timestamps with NA fbk values
    # separate into individual variables
    TSx = dfminiNA.iloc[:, 0]
    fbky = dfminiNA.iloc[:, 1]
    dfmNAcs = dfminiNA.cumsum()  # calculate the cumulative summation

    plt.close("all")  # close all open plots
    # first plot
    df.plot()  # plot using pandas method
    plt.show(block = False)  # show plot but don't pause for input
    # second plot
    dfminiNA.plot()  # to show only fbk curve
    plt.show()  # show all plots and wait

PandaPlot1()
