# Prints all data in csv file one line at a time on separate lines
import csv
with open('../PV_Data/SR1_BCaL_8h.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        print(row)