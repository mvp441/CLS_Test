import dframe as dframe
import pandas as pd
from lmfit.models import LorentzianModel

#dframe = pd.read_csv('peak.csv')

df = pd.read_csv("SR1_BCaL_8h.csv")
df.dropna()

dfminiNA = df.iloc[1:20, 0:2]
dfminiNA = dfminiNA.dropna()
TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]

# seperate df into mini of each variable to plot

dfmNAcs = dfminiNA.cumsum() #calculate the cumulative summation

model = LorentzianModel()
params = model.guess(fbky, TSx)

result = model.fit(fbky, params, TSx)

print(result.fit_report())

result.plot_fit()

