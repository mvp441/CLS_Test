import csv
csv.register_dialect('myDialect',
                     delimiter=',',
                     skipinitialspace=False,
                     quoting=csv.QUOTE_NONE)
with open('SR1_BCaL_8h.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)