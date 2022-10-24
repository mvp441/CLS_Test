



df = pd.read_csv("SR1_BCaL_8h.csv")#, parse_dates=["Timestamp"])
data = df.values
df.dropna()



dfminiNA = df.iloc[1:100, 0:2]
dfminiNA = dfminiNA.dropna()
TSx = dfminiNA.iloc[:, 0]
fbky = dfminiNA.iloc[:, 1]



date1 = TSx.min
date2 = TSx.max
# datetime.resolution(date1, date2)

# td = date2 - date1

#start = TSx.iloc[0, 0]
#end = TSx.iloc[-1, 0]
#index = pd.date_range(start, end)
#print(index)


#TSx = TSx.astype('float64')
ax = []
ax = [i for i in range(len(fbky))]
#print(ax)
TSx = ax
# dfminiNA.astype('int32').dtypes



