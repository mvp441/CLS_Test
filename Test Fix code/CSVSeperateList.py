import csv
file = open("../PV_Data/SR1_BCaL_8h.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
TimeStamp = []
fbk = []
Change = []
TimeConstant = []
remove = 'N/a'
for row in csvreader:
    rows.append(row)
    TimeStamp.append(row[0])
    fbk.append(row[1])
    Change.append(row[2])
    TimeConstant.append(row[3])
#print(TimeStamp)
print('just normal fbkNA')
print(fbk)
print('without N/A')
print(list(filter(lambda val: val != 'N/A', fbk)))
#file.close()
