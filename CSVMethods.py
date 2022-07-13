import csv

# Function 1
# Prints all data in csv file unseparated
file = open("SR1_BCaL_8h.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()

# Function 2
# Prints all data in csv file one line at a time on separate lines
with open('SR1_BCaL_8h.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        print(row)

# Function 3
# Prints out all data in CSV file on separate lines with title attached to each value
import csv
with open("SR1_BCaL_8h.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

# Function 4
# Dialect helps group together many specific formatting patters
csv.register_dialect('myDialect',
                     delimiter=',',
                     skipinitialspace=False,
                     quoting=csv.QUOTE_NONE)
with open('SR1_BCaL_8h.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)

# Function 5
# Sniffer used to deduce the dialect (format) of the CSV file
with open('SR1_BCaL_8h.csv', 'r') as csvfile:
    sample = csvfile.read(64)
    has_header = csv.Sniffer().has_header(sample)
    print(has_header)
    deduced_dialect = csv.Sniffer().sniff(sample)
with open('SR1_BCaL_8h.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, deduced_dialect)
    for row in reader:
        print(row)

# Function 6 - Separate
file = open("SR1_BCaL_8h.csv")
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




