import json
from glob import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_filenames_from_folder(folder_location='/home/parmarm/Documents/CLS_Test/Data/tune-data', file_name='/getTbTBPMData_2023-05-07*.json'):
    filename_list = glob(folder_location + file_name)
    return filename_list

def json_to_dictionary(file_name):
    json_file = open(file_name)
    dictionary_with_file_data = json.load(json_file)
    for key_outer in dictionary_with_file_data:
        data = dictionary_with_file_data[key_outer]
        for key_inner in data:
            value = data[key_inner]
    key = dictionary_with_file_data.keys()[0]
    key_list = dictionary_with_file_data[key].keys()
    dictionary_with_file_data["key_list"] = key_list
    # key_list.sort() shouldn't be necessary at this point
    dictionary_with_file_data["file_name"] = file_name
    return dictionary_with_file_data, key_list

def add_dictionary_information(dictionary_with_file_data):
    dictionary_with_file_data["experiment"] = None # add
    dictionary_with_file_data["description"] = None # to identify and distinguish files
    dataframe_with_file_info, dataframe_with_changing_data = json_to_dataframe(dictionary_with_file_data["file_name"])
    dictionary_with_file_data["dataframe_with_file_info"] = dataframe_with_file_info
    dictionary_with_file_data["changing_data"] = dataframe_with_changing_data

def jsons_to_dictionary_list(filename_list):
    list_of_json_dictionaries = []
    key_list_list = []
    for i in range(len(filename_list)):
        dictionary_with_file_data, key_list = json_to_dictionary(filename_list[i])
        list_of_json_dictionaries.append(dictionary_with_file_data)
        key_list_list.append(key_list)
        i =+ 1
    return list_of_json_dictionaries, key_list

def select_dictionary(list_of_json_dictionaries, filename):
    dictionary_found = 0
    dictionary_checking = 0
    while dictionary_found != 1:
        if list_of_json_dictionaries[dictionary_checking]['file_name'] == filename:
            dictionary_found = 1
            dictionary = list_of_json_dictionaries[dictionary_checking]
        dictionary_checking += 1
    return dictionary

def add_dictionary_description(list_of_json_dictionaries, filename, description): # should not need if add works
    dictionary = select_dictionary(list_of_json_dictionaries, filename)
    dictionary["description"] = description

def add_experiment_number(list_of_json_dictionaries, filename, experiment_number): # should not need if add works
    dictionary = select_dictionary(list_of_json_dictionaries, filename)
    dictionary["experiment"] = experiment_number

def add_to_dictionary(list_of_json_dictionaries, filename, key, value):
    dictionary = select_dictionary(list_of_json_dictionaries, filename)
    dictionary[key] = value

def test_load_data_to_dictionary():
    print('starting test of loading json data into dictionary')
    test_filename_list = load_filenames_from_folder()
    test_dictionary_with_file_data = json_to_dictionary(test_filename_list[0])
    test_json_dictionary_list = jsons_to_dictionary_list(test_filename_list)
    test_select_dictionary = select_dictionary(test_json_dictionary_list, test_filename_list[0])
    test_add_dictionary_description = add_dictionary_description(test_json_dictionary_list, test_filename_list[0], "Test description 1")
    test_add_dictionary_description = add_experiment_number(test_json_dictionary_list, test_filename_list[0], 2)
    test_add_to_dictionary1 = add_to_dictionary(test_json_dictionary_list, test_filename_list[0], "experiment", 3)
    test_add_to_dictionary2 = add_to_dictionary(test_json_dictionary_list, test_filename_list[0], "description", "Test decription 2")
    print('finished test of loading json data into dictionary')


def json_to_dataframe(json_file):
    # Need to make second dataframe of just json data (anything in a list)
    # add second dataframe to dictionary entry
    dataframe_with_file_info = pd.read_json(json_file)
    dataframe_with_changing_data = pd.DataFrame  # Create second dataframe of changing variables
    dataframe_columns = dataframe_with_file_info.columns.to_list()
    for i in dataframe_columns:  # loop through all variales in dataframe
        if dataframe_with_file_info[i] is type(list):  # check if variable has a single value or is a list of values
            column_with_changing_data = dataframe_with_file_info.iloc[i] # if a list add to second dataframe
            # Use dataframe_with_file_info.iloc[#] to get entire row or .loc['column/variable_name']
            #dataframe_with_changing_data append column
    return dataframe_with_file_info, dataframe_with_changing_data

def jsons_to_dataframe_list(filename_list):
    list_of_json_dataframes = []
    for i in range(len(filename_list)):
        dataframe_with_file_data = json_to_dataframe(filename_list[i])
        list_of_json_dataframes.append(dataframe_with_file_data)
        i =+ 1
    return list_of_json_dataframes

def test_load_data_to_dataframe():
    print('Starting conversion of json to df')
    test_filename_list = load_filenames_from_folder()
    test_dataframe_with_file_data = json_to_dataframe(test_filename_list[0])
    test_json_dataframe_list = jsons_to_dataframe_list(test_filename_list)
    print('Finished conversion of json to df')

"""

def open_files(filename_list, output_type='dictionary'):
    if output_type == 'dictionary':
        return dictionary_with_file_data
    elif output_type == 'dataframe':
        return dataframe_with_file_data

def select_file(filename):
    return file_data

def select_variable_data(variable):
    return variable_data

def single_plot(dictionary with plot specifications): 

def plot(list of dictionaries with plot specifications):

def calculate_FFT(filename):
    return file_FFT

"""

#test_load_data_to_dictionary()
test_load_data_to_dataframe()
