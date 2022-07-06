import csv
with open('SR1_BCaL_8h.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        print(row)