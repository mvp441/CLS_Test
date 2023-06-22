# Prints out all data in CSV file on separate lines with title attached to each value
import csv
with open("../PV_Data/SR1_BCaL_8h.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

