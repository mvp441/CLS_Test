from lib import CSV

csv_list = CSV.CsvManger(["../PV Data/Trip 1 data/gLYHVdm+.csv"])
csv_list.add_csv('../PV Data/Trip 1 data/tdL5QoZo.csv')
#csv_list.output_dataframe_to_console()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# step 1 get the data in a usable format for determining correlations
# step 2 get a scatter plot correlation of PVs
# step 3 test with known correlated data
# step 4 loop over multiple PVs
#
# find which PVs correlate 
#
# step n use machine learning

# ask about phase section 6 and booster ring injection frequency
# ask operators about PVs they know are ocrrolated
# what value has a problem and which value do you adjust ot fix it
# what knob do you grab and what change do you see
# y axis read back PV1
# x axix read back of PV2

# send corroaltion of PVs plot

