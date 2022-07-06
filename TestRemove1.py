import csv
print('Test 1')
data1 = []
print(type(data1))
print('Test 2')
data2 = {}
print(type(data2))

with open("SR1_BCaL_8h.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))
        data2 = dict(row)

        data1.append(dict(row))

print('Test 1')
print(row)
print('Test 3')
print(data1[1])
print('Test 4')
print(type(data2))
print('Done')
