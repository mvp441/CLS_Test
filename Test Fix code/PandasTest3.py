import pandas as pd

def print_data(df):
    for column in df:
        print(df[column])
        print('\n')

def get_list_desc(df):
    dfdesc = list()
    dfdesc.append(df.describe())
    for column in df:
        dfdesc.append(df[column].describe())
    return dfdesc

def get_dict_desc(df):
    dfdesc = {}
    for column in df:
        dfdesc[column] = df[column].describe()
    return dfdesc

def drop_NA(df):  # Won't work because of NA placement - need seperated columns which loses time
    dfnoNA = {}
    for column in df:
        dfnoNA[column] = df[column].dropna()
    return dfnoNA

df = pd.read_csv("../PV Data/SR1_BCaL_8h.csv")

print(df.columns)
print(df)

dfminiNA = df.iloc[1:20, 0:4]
print("dfmini with N/A")  #, dfminiNA.iloc[:,1:4])
print(dfminiNA.iloc[:,1:4])

Timestamp = dfminiNA.iloc[:, [0]]
fbkNA = dfminiNA.iloc[:, [1]]
mAChangeNA = dfminiNA.iloc[:, [2]]
timeConstantNA = dfminiNA.iloc[:, [3]]

dfminiNAdesc = dfminiNA.describe()
fbkNAdesc = fbkNA.describe()
mAChangeNAdesc = mAChangeNA.describe()
timeConstantNAdesc = timeConstantNA.describe()

NA_list_desc = get_list_desc(dfminiNA)
NA_dict_desc = get_dict_desc(dfminiNA)

print("columns with N/A")
print_data(dfminiNA)
print("description with N/A")
print_data(NA_dict_desc)

fbk = fbkNA.dropna()
mAChange = mAChangeNA.dropna()
timeConstant = timeConstantNA.dropna()
print("columns without N/A")  # , fbk, "\n", mAChange, "\n", timeConstant)
print(fbk)
print(mAChange)
print(timeConstant)
print("description N/A dropped")  # , "\n", fbk.describe())#, "\n", mAChange.describe(), "\n", timeConstant.describe())
print(fbk.describe())
print(mAChange.describe())
print(timeConstant.describe())

dfmini0 = dfminiNA.copy().fillna(0)
dfm0_dict_desc = get_dict_desc(dfmini0)
print("columns with N/A filled by 0")
print_data(dfmini0)
print("description N/A 0")
print_data(dfm0_dict_desc)

dfminipad = dfminiNA.copy().fillna(method='pad')
dfmpad_dict_desc = get_dict_desc(dfminipad)
print("columns fill N/A padded")
print_data(dfminipad)
print("description N/A padded")
print_data(dfmpad_dict_desc)

print("n=5 sample")
print(fbk.sample(n=5))
print(mAChange.sample(n=5))
print(timeConstant.sample(n=5))

print("position values before index 5")
print(fbk.loc[0:4])
print(mAChange.loc[0:4])
print(timeConstant.loc[0:4])


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





