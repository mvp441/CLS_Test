import csv
print('Test 1: initial data1 type')
data1 = []
print(type(data1))
print('Test 2: initial data2 type')
data2 = {}
print(type(data2))

with open("../PV Data/SR1_BCaL_8h.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
#        print(dict(row))
        data2 = dict(row)
        data1.append(dict(row))

print('Test 3: row type')
print(row)

print('Test 4: final data1 type')
print(type(data1))
print(data1[1])

print('Test 5: final data2 type')
print(type(data2))
print(data2)

print('Done')
