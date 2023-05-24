from lib import CSV

def test_csv_add(csv_list, csv_2):
    csv_list.add_csv(csv_2)
    print(csv_list.print_columns())

def test_output_csv_list(csv_list):
    csv_list.output_csv_list()

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

def test_drop_na_values(csv_list):
    csv_list.drop_na_values()
    csv_list.output_dataframe_to_console()

def test_fill_na_values(csv_list, fill):
    csv_list.fill_na_values(fill)
    csv_list.output_dataframe_to_console()

def test_interpolate_data(csv_list):
    csv_list.interpolate_data()
    csv_list.output_datafram_to_console()

def test_calculate_correlation_matrix(csv_list):
    correlation_matrix = csv_list.calculate_correlation_matrix()
    print(correlation_matrix)

def test_output_correlation_matrix(csv_list):
    csv_list.output_correlation_matrix()

#Present
#Pandas3: plotting
#

def currently_testing(csv_1, csv_2):
    csv_list = CSV.CSVList([csv_1])
    test_csv_add(csv_list, csv_2)

    #test_interpolate_data(csv_list)
    #test_calculate_correlation_matrix(csv_list)
    #test_output_correlation_matrix(csv_list)

    print('done testing')

def tested_working(csv_1, csv_2):
    csv_list = CSV.CSVList([csv_1])
    test_csv_add(csv_list, csv_2)
    test_output_csv_list(csv_list)
    test_get_column_names(csv_list)
    test_get_column_values(csv_list)
    test_output_dataframe_to_console(csv_list)
    test_print_columns(csv_list)
    test_get_list_descriptions(csv_list)
    test_get_dictionary_descriptions(csv_list)
    test_drop_na_values(csv_list)
    test_fill_na_values(csv_list, 'pad') # test with  float, mean, median, mode, backfill, bfill, ffill, and pad - works with 5

csv_1 = "../PV Data/Trip 1 data/gLYHVdm+.csv"
csv_2 = '../PV Data/Trip 1 data/tdL5QoZo.csv'

currently_testing(csv_1, csv_2)
#tested_working(csv_1, csv_2)

