import pandas as pd
df = pd.read_csv("SR1_BCaL_8h.csv")
#print(df.columns)
fbk = df.iloc[:, [1]]
fbk = fbk.dropna()
print(fbk)


