import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.close("all")

df = pd.read_csv("SR1_BCaL_8h.csv")
dfminiNA = df.iloc[1:20, 0:4]
dfmNAcs = dfminiNA.cumsum()
plt.figure()
plt.show()
dfmNAcs.plot()

