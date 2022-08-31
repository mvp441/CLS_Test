import pandas as pd
df = pd.read_csv("SR1_BCaL_8h.csv")
#print(df.columns)
#print(df)

dfminiNA = df.iloc[1:20,0:4]
print("\n dfmini with N/A \n", dfminiNA.iloc[:,1:4])

Timestamp = dfminiNA.iloc[:, [0]]
fbkNA = dfminiNA.iloc[:, [1]]
mAChangeNA = dfminiNA.iloc[:, [2]]
timeConstantNA = dfminiNA.iloc[:, [3]]

print("\n descricption with N/A", "\n", dfminiNA.describe())
#print("\n descricption with N/A", "\n", dfminiNA.describe(), "\n", fbkNA.describe(), "\n", mAChangeNA.describe(), "\n", timeConstantNA.describe())
# print("columns with N/A \n", fbkNA, "\n", mAChangeNA, "\n", timeConstantNA)

fbk = fbkNA.dropna()
mAChange = mAChangeNA.dropna()
timeConstant = timeConstantNA.dropna()

print("\n descricption N/A dropped", "\n", fbk.describe())#, "\n", mAChange.describe(), "\n", timeConstant.describe())
# print("columns without N/A \n", fbk, "\n", mAChange, "\n", timeConstant)

fbk0 = fbkNA.fillna(0)
mAChange0 = mAChangeNA.fillna(0)
timeConstant0 = timeConstantNA.fillna(0)
#print("\n descricption N/A 0", "\n", fbk0.describe())#, "\n", mAChange0.describe(), "\n", timeConstant0.describe()) #changes values too much

fbkpad = fbkNA.fillna(method="pad")
mAChangepad = mAChangeNA.fillna(method="pad")
timeConstantpad = timeConstantNA.fillna(method="pad")
print("\n descricption N/A padded", "\n", fbkpad.describe())#, "\n", mAChangepad.describe(), "\n", timeConstantpad.describe())

# print("\n n=5 sample")
# print(fbkNA.sample(n=5))
# print(mAChange.sample(n=5))
# print(timeConstantNA.sample(n=5))

# print("\n first 5 position values")
# print(fbkNA.loc[0:4])
# print(mAChange.loc[0:4])
# print(timeConstantNA.loc[0:4])


# go through column headers
# save each column title in array
# convert to string?
# loop through column titles
# separate dataframe into individual columns
# remove na values
# perform statical analysis

# store description and stats over time in variable
# continue to compare current values against previous stored ones
# trigger when current values deviates by larger than allowed margin
    # set trigger value limits





