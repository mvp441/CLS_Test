import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_csv("SR1_BCaL_8h.csv")
df.dropna()

dfminiNA = df.iloc[1:20, 0:2]
dfminiNA.dropna(axis='row')
TSx = dfminiNA.iloc[:, 0]
TSx = TSx.dropna()
fbky = dfminiNA.iloc[:, 1]
fbky = fbky.dropna()

dfmNAcs = dfminiNA.cumsum()
plt.close("all")
plt.figure()
dfminiNA.plot(x="Tsx", y="fbky")
plt.show()
#dfminiNA.iloc[1].plot.bar()
#dfmNAcs.plot(x="Timestamp", y="fbk")
#plt.axline(0,color="k")
