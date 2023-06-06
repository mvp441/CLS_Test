from lib import CSV, JSON

#def test_csv_to_df(csv_file):

#def test_add_csv_to_dictionary(csv_file):

#def test_load_csv_file(csv_file):

def test_add_csv(csv_list, csv_2):
    csv_list.add_csv(csv_2)
    #print(csv_list.print_columns())

def test_output_csv_list(csv_list):
    csv_list.output_csv_list()

#def test_construct_master_dataframe(csv_list):

def test_select_dataframe(csv_list, dataframe_name):
    csv_list.select_dataframe(dataframe_name)

#def test_set_dataframe_as_master(csv_lsit, dataframe='master_dataframe')
    #csv_list.set_dataframe_as_master(dataframe)

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

#def test_remove_columns(csv_list, columns):

#def test_removing_files(csv_list, file_name):

def test_drop_na_values(csv_list):
    csv_list.drop_na_values()
    csv_list.output_dataframe_to_console()

def test_fill_na_values(csv_list, fill):
    csv_list.fill_na_values(fill)
    csv_list.output_dataframe_to_console()

def test_interpolate_data(csv_list, method, order=None):
    csv_list.interpolate_data(method, order)
    csv_list.output_dataframe_to_console()

def test_calculate_correlation_matrix(csv_list):
    csv_list.calculate_correlation_matrix()
    csv_list.output_correlation_matrix()

def test_output_correlation_matrix(csv_list):
    csv_list.output_correlation_matrix()

#Present
#Pandas3: plotting
#

def file_setup():
    csv_1 = "../PV Data/Trip 1 data/gLYHVdm+.csv"
    csv_2 = '../PV Data/Trip 1 data/tdL5QoZo.csv'
    csv_list = CSV.CSVList([csv_1])
    test_add_csv(csv_list, csv_2)
    return csv_list

def test_load_data_to_dataframe():
    print('Starting conversion of json to df')
    json_manager = JSON.JsonManager()
    test_filename_list = json_manager.load_filenames_from_folder()
    test_dataframe_with_file_data = json_manager.json_to_dataframe(test_filename_list[0])
    test_json_dataframe_list = json_manager.jsons_to_dataframe_list(test_filename_list)
    print('Finished conversion of json to df')

def test_load_data_to_dictionary():
    print('starting test of loading json data into dictionary')
    json_manager = JSON.JsonManager()
    test_filename_list = json_manager.load_filenames_from_folder()
    test_dictionary_with_file_data = json_manager.json_to_dictionary(test_filename_list[0])
    test_json_dictionary_list = json_manager.jsons_to_dictionary_list()
    test_select_dictionary = json_manager.select_dictionary(test_filename_list[0])
    test_add_dictionary_description = json_manager.add_dictionary_description(test_filename_list[0], "Test description 1")
    test_add_dictionary_description = json_manager.add_experiment_number(test_filename_list[0], 2)
    test_add_to_dictionary1 = json_manager.add_to_dictionary(test_filename_list[0], "experiment", 3)
    test_add_to_dictionary2 = json_manager.add_to_dictionary(test_filename_list[0], "description", "Test decription 2")
    print('finished test of loading json data into dictionary')

def currently_testing(csv_list, csv_file=None):
    # test re-adding the same files
    # test_add_csv(csv_list, csv_file)  # adding same file twice shouldn't add data

    test_select_dataframe(csv_list, '../PV Data/Trip 1 data/tdL5QoZo.csv')

    test_interpolate_data(csv_list, 'polynomial', 5)
    test_calculate_correlation_matrix(csv_list)
    test_output_correlation_matrix(csv_list)

    # test adding other file types
    # test_remove_columns(csv_list, columns)
    # test_removing_files(csv_list, file_name)

    print('done testing')

def tested_working(csv_list):
    # test_csv_to_df(csv_file)
    # test_add_csv_to_dictionary(csv_file)
    # test_read_csv_file(csv_file)
    # test_add_csv(csv_file)
    # test_construct_master_dataframe(csv_list)
    test_output_csv_list(csv_list)
    test_get_column_names(csv_list)
    test_get_column_values(csv_list)
    test_output_dataframe_to_console(csv_list)
    test_print_columns(csv_list)
    test_get_list_descriptions(csv_list)
    test_get_dictionary_descriptions(csv_list)
    test_drop_na_values(csv_list)
    test_fill_na_values(csv_list, 'pad')  # test with  float, mean, median, mode, backfill, bfill, ffill, and pad - works with 5
    test_interpolate_data(csv_list, 'linear')  # works with linear and polynomial 1 and 5, try orders 2-4 still



csv_list = file_setup()
currently_testing(csv_list)
#tested_working(csv_list)

