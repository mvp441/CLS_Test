import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_csv("SR1_BCaL_8h.csv")
df.dropna()

dfminiNA = df.iloc[1:20, 0:2]
dfminiNA = dfminiNA.dropna()
TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]

# seperate df into mini of each variable to plot

dfmNAcs = dfminiNA.cumsum()
plt.close("all")
plt.figure()
df.plot() #dfminiNA.plot() to show only fbk curve
plt.show()
#dfminiNA.iloc[1].plot.bar()
#dfmNAcs.plot(x="Timestamp", y="fbk")
#plt.axline(0,color="k")
