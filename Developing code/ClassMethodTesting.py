from lib import CSV

csv_list = CSV.CSVList(["../PV Data/Trip 1 data/gLYHVdm+.csv"])
csv_list.add_csv('../PV Data/Trip 1 data/tdL5QoZo.csv')
print(csv_list.print_columns())
