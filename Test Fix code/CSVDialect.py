# Prints all data in csv file one line at a time on separate lines
# Dialect helps group together many specific formatting patters
import csv
csv.register_dialect('myDialect',
                     delimiter=',',
                     skipinitialspace=False,
                     quoting=csv.QUOTE_NONE)
with open('../PV Data/SR1_BCaL_8h.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)