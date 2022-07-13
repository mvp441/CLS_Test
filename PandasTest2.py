import pandas as pd
df = pd.read_csv("SR1_BCaL_8h.csv")
#print(df.columns)
#print(df)

dfmini = df.iloc[1:20,0:4]
print("dfmini \n")
print(dfmini)

Timestamp = dfmini.iloc[:, [0]]
fbk = dfmini.iloc[:, [1]]
mAChange = dfmini.iloc[:, [2]]
timeConstant = dfmini.iloc[:, [3]]

print("columns with N/A \n", fbk, "\n", mAChange, "\n", timeConstant)

fbk = fbk.dropna()
mAChange = mAChange.dropna()
timeConstant = timeConstant.dropna()
print("columns without N/A \n", fbk, "\n", mAChange, "\n", timeConstant)

# print("\n n=5 sample")
# print(fbk.sample(n=5))
# print(mAChange.sample(n=5))
# print(timeConstant.sample(n=5))

# print("\n first 5 position values")
# print(fbk.loc[0:4])
# print(mAChange.loc[0:4])
# print(timeConstant.loc[0:4])


# go through column headers
# save each column title in array
# convert to string?
# loop through column titles
# separate dataframe into individual columns
# remove na values
# perform statical analysis