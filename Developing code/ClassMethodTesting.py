from lib import CSV, JSON

'''Possibly consider making entire file a class for testing with each FiletypeManager as it's own instance and turning functions into helper ones'''

#def test_csv_to_df(csv_file):

#def test_add_csv_to_dictionary(csv_file):

#def test_load_csv_file(csv_file):

def test_add_csv(csv_data, csv_file):
    csv_data.add_csv(csv_file)
    #print(csv_list.print_columns())

def test_output_csv_list(csv_data):
    csv_data.output_csv_list()

#def test_construct_master_dataframe(csv_data):

def test_select_dataframe(csv_data, dataframe_name):
    csv_data.select_dataframe(dataframe_name)

def test_modify_dataframe(csv_data, method='polynomial', order=1):
    csv_data.modify_dataframe(dataframe=csv_data.list_of_csv_dataframes[1], method=method, order=order)

#def test_set_dataframe_as_master(csv_lsit, dataframe='master_dataframe')
    #csv_list.set_dataframe_as_master(dataframe)

def test_get_column_names(csv_data):
    column_names = csv_data.get_column_names()
    print(column_names)

def test_get_column_values(csv_data):
    column_names = csv_data.get_column_names()
    print(csv_data.get_column_values(column_names[0]))

def test_output_dataframe_to_console(csv_data):
    csv_data.output_dataframe_to_console()

def test_print_columns(csv_data):
    csv_data.print_columns()

def test_get_list_descriptions(csv_data):
    desc = csv_data.get_list_description()
    print(desc)

def test_get_dictionary_descriptions(csv_data):
    desc = csv_data.get_dictionary_description()
    print(desc)

def test_convert_time_interval(csv_data, column):
    csv_data.convert_time_interval(column)
    #print time interval data type before and after conversion

#def test_remove_columns(csv_data, columns):

#def test_removing_files(csv_data, file_name):

def test_drop_na_values(csv_data):
    csv_data.drop_na_values()
    csv_data.output_dataframe_to_console()

def test_fill_na_values(csv_data, fill):
    csv_data.fill_na_values(fill)
    csv_data.output_dataframe_to_console()

def test_interpolate_data(csv_data, method, order=None):
    csv_data.interpolate_data(method, order)
    csv_data.output_dataframe_to_console()

def test_calculate_correlation_matrix(csv_data):
    csv_data.calculate_correlation_matrix()
    csv_data.output_correlation_matrix()

def test_output_correlation_matrix(csv_data):
    csv_data.output_correlation_matrix()

def test_plot_correlation_matrix(csv_data):
    csv_data.plot_correlation_matrix()

#Present
#Pandas3: plotting
#

def file_setup():
    csv_1 = "../PV Data/Trip 1 data/gLYHVdm+.csv"
    csv_2 = '../PV Data/Trip 1 data/tdL5QoZo.csv'
    csv_data = CSV.CsvManger([csv_1])
    test_add_csv(csv_data, csv_2)
    return csv_data

def correlation_setup(csv_data):
    #csv_data.select_dataframe('../PV Data/Trip 1 data/tdL5QoZo.csv')  # might not need
    csv_data.select_dataframe()
    csv_data.convert_time_interval('PCT1402-01:timeInterval:fbk')
    csv_data.calculate_correlation_matrix()
    csv_data.output_correlation_matrix()

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
    test_dictionary_with_file_data = json_manager.json_to_dictionary(json_manager.list_of_file_names[0])
    test_json_dictionary_list = json_manager.jsons_to_dictionary_list()
    test_select_dictionary = json_manager.select_dictionary(test_filename_list[0])
    test_add_dictionary_description = json_manager.add_dictionary_description(test_filename_list[0], "Test description 1")
    test_add_dictionary_description = json_manager.add_experiment_number(test_filename_list[0], 2)
    test_add_to_dictionary1 = json_manager.add_to_dictionary(test_filename_list[0], "experiment", 3)
    test_add_to_dictionary2 = json_manager.add_to_dictionary(test_filename_list[0], "description", "Test decription 2")
    print('finished test of loading json data into dictionary')

def currently_testing(csv_data, csv_file=None):
    # test re-adding the same files
    # test_add_csv(csv_list, csv_file)  # adding same file twice shouldn't add data

    test_modify_dataframe(csv_data)

    correlation_setup(csv_data)
    test_plot_correlation_matrix(csv_data)

    # test adding other file types
    # test_load_data_to_dictionary
    # test_load_data_to_dataframe()
    test_modify_dataframe(csv_data)
    # test_remove_columns(csv_data, columns)
    # test_removing_files(csv_data, file_name)

    print('done testing')

def tested_working(csv_data):
    # test_csv_to_df(csv_file)
    # test_add_csv_to_dictionary(csv_file)
    # test_read_csv_file(csv_file)
    # test_add_csv(csv_file)
    # test_construct_master_dataframe(csv_list)
    test_output_csv_list(csv_data)
    test_get_column_names(csv_data)
    test_get_column_values(csv_data)
    test_output_dataframe_to_console(csv_data)
    test_print_columns(csv_data)
    test_get_list_descriptions(csv_data)
    test_get_dictionary_descriptions(csv_data)
    test_drop_na_values(csv_data)
    test_fill_na_values(csv_data, 'pad')  # test with  float, mean, median, mode, backfill, bfill, ffill, and pad - works with 5
    test_interpolate_data(csv_data, 'linear')  # works with linear and polynomial 1, but not 5, try orders 2-4 still



csv_data = file_setup()
currently_testing(csv_data)
test_load_data_to_dictionary()
#tested_working(csv_data)

