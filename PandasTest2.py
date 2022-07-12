import pandas as pd
df = pd.read_csv("SR1_BCaL_8h.csv")
#print(df.columns)
print(df)
dfmini = df.iloc[1:10,[1]]
print(dfmini)
Timestamp = df.iloc[:, [0]]
fbk = df.iloc[:, [1]]
mAChange = df.iloc[:, [2]]
timeConstant = df.iloc[:, [3]]
fbk = fbk.dropna()
mAChange = mAChange.dropna()
timeConstant = timeConstant.dropna()
print(fbk.sample(n=10))
print(mAChange.sample(n=10))
print(timeConstant.sample(n=10))
#print(fbk.loc[1:5])
#print(mAChange.loc[1:5])
print(timeConstant.loc[0])


# go through column headers
# save each column title in array
# convert to string?
# loop through column titles
# separate dataframe into individual columns
# remove na values
# perform statical analysis