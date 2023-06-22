# Prints all data in csv file one line at a time on separate lines
# Sniffer used to deduce the dialect (format) of the CSV file
import csv
with open('../PV_Data/SR1_BCaL_8h.csv', 'r') as csvfile:
    sample = csvfile.read(64)
    has_header = csv.Sniffer().has_header(sample)
    print(has_header)

    deduced_dialect = csv.Sniffer().sniff(sample)

with open('../PV_Data/SR1_BCaL_8h.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, deduced_dialect)

    for row in reader:
        print(row)