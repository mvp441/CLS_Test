import pandas as pd
from matplotlib import pyplot as plt
from lib import CsvManager

# import csv data file
csv_list = CSV.CsvManger(["../PV Data/Trip 1 data/gLYHVdm+.csv"])
# add csv files together
csv_list.add_csv('../PV Data/Trip 1 data/tdL5QoZo.csv')
    # csv_list.add_csv("../PV Data/Trip 1 data/gLYHVdm+.csv")
# copy column names into list - class attribute

# get column names function
csv_list.get_column_names()

csv_list.sort_by_column("Timestamp")
# fill in missing data
csv_list.interpolate_data()


# plot all data and correlation
csv_list.output_dataframe_to_console()

# calculate correlation between PV1 and remaining PVs

# sort list by PV correlation factor

# display data









