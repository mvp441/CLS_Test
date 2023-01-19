import numpy
import csv
import scipy.stats

file = open("../PV Data/SR1_BCaL_8h.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
TimeStamp = []
fbk = []
Change = []
TimeConstant = []
for row in csvreader:
    rows.append(row)
    TimeStamp.append(row[0])
    fbk.append(row[1])
    Change.append(row[2])
    TimeConstant.append(row[3])

print('initial Change length: ' + str(len(Change)))
print('initial fbkNA length: ' + str(len(fbk)))
print('initial TimeConstant length: ' + str(len(TimeConstant)) + '\n')

valueToBeRemoved = 'N/A'

Change = filter(lambda val: val != valueToBeRemoved, Change)

try:
    while True:
        fbk.remove(valueToBeRemoved)
except ValueError:
    pass

TimeConstant = [value for value in TimeConstant if value != valueToBeRemoved]

print('final Change length: ' + str(len(Change)))
print('final fbkNA length: ' + str(len(fbk)))
print('final TimeConstant length: ' + str(len(TimeConstant)) + '\n')

fbk = [float(x) for x in fbk]
Change = [float(x) for x in Change]

print('numpy corrcoef')
print(numpy.corrcoef(fbk, Change))
print('SciPy Pearsonr:' + str(scipy.stats.pearsonr(fbk, Change)))
print(scipy.stats.spearmanr(fbk, Change))
print(scipy.stats.kendalltau(fbk, Change))

file.close()
