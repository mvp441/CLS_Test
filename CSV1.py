# Prints all data in csv file unseparated
import csv
file = open("SR1_BCaL_8h.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()