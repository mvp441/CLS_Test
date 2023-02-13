from lib import CSV

def test_csv_add(csv_list, csv_2):
    csv_list.add_csv(csv_2)
    print(csv_list.print_columns())


def test_get_column_names(csv_list):
    column_names = csv_list.get_column_names()
    print(column_names)

def test_get_column_values(csv_list):
    column_names = csv_list.get_column_names()
    print(csv_list.get_column_values(column_names[0]))

def test_output_dataframe_to_console(csv_list):
    csv_list.output_dataframe_to_console()

def test_print_columns(csv_list):
    csv_list.print_columns()

def test_get_list_descriptions(csv_list):
    desc = csv_list.get_list_description()
    print(desc)

def test_get_dictionary_descriptions(csv_list):
    desc = csv_list.get_dictionary_description()
    print(desc)

#Present
#Pandas3: plotting
#

def currently_testing(csv_1, csv_2):
    csv_list = CSV.CSVList([csv_1])



def tested_working(csv_1, csv_2):
    csv_list = CSV.CSVList([csv_1])
    test_csv_add(csv_list, csv_2)
    test_get_column_names(csv_list)
    test_get_column_values(csv_list)
    test_output_dataframe_to_console(csv_list)
    test_print_columns(csv_list)
    test_get_list_descriptions(csv_list)
    test_get_dictionary_descriptions(csv_list)


csv_1 = "../PV Data/Trip 1 data/gLYHVdm+.csv"
csv_2 = '../PV Data/Trip 1 data/tdL5QoZo.csv'

currently_testing(csv_1, csv_2)
#tested_working(csv_1, csv_2)

