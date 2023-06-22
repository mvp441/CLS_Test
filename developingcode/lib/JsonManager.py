import json
from glob import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
from DataStore import data
import FileManager
from DataDictionary import DataDictionary

class JsonManager():
    def __init__(self):
        self.list_of_json_files = data.data_inventory['dictionary_of_file_names']['list_of_json']
        self.list_of_file_names = data.data_inventory['dictionary_of_file_names']['list_of_all']
        self.list_of_json_dictionaries = data.data_inventory['dictionary_of_dictionaries']['list_of_json']
        self.list_of_json_dataframes = data.data_inventory['dictionary_of_dataframes']['list_of_json']
        self.dictionary = {}
        self.dataframe = FileManager.file_manager.data_catalog['current_file']['dataframe']
        self.dataframe_list = data.data_inventory['dictionary_of_dataframes']['list_of_current']
        self.dataframe_dictionary_list = data.data_inventory['dictionary_of_dictionaries']['list_of_all']
        self.original_master_dataframe = FileManager.file_manager.data_catalog['master_data']['original_dataframe']
        self.master_dataframe = FileManager.file_manager.data_catalog['master_data']['current_dataframe']

    def load_filenames_from_folder(self, folder_location='/home/parmarm/Documents/CLS_Test/Data/tune-data',
                                    file_name='/*.json'):
        self.list_of_json_files = glob(folder_location + file_name)
        return self.list_of_json_files

    def json_to_dictionary(self, file_name):
        json_file = open(file_name)
        self.dictionary = json.load(json_file)
        for key_outer in self.dictionary:
            data = self.dictionary[key_outer]
            for key_inner in data:
                value = data[key_inner]
        key = self.dictionary.keys()[0]
        key_list = self.dictionary[key].keys()
        self.dictionary['key_list'] = key_list
        # key_list.sort() shouldn't be necessary at this point
        self.dictionary['file_name'] = file_name
        self.add_dictionary_information()
        self.list_of_json_dictionaries.append(self.dictionary)
        self.dataframe_dictionary_list.append(self.dictionary)
        #ds.data.data_inventory['dictionary_of_dictionaries']['list_of_json'].append(self.dictionary)
        return self.dictionary

    def add_dictionary_information(self):
        # possibly remove the following two lines for non experiment use or make optional
        self.dictionary['experiment'] = None  # add
        self.dictionary['description'] = None  # to identify and distinguish files
        self.json_to_dataframe(self.dictionary['file_name'])
        # self.dictionary['original_data'] = copy.deepcopy(self.get_json_data())
        return self.dictionary

    def jsons_to_dictionary_list(self):
        self.list_of_json_dictionaries = []
        key_list_list = []
        for i in range(len(self.list_of_json_files)):
            self.json_to_dictionary(self.list_of_json_files[i])
            self.list_of_json_dictionaries.append(self.dictionary)
        return self.list_of_json_dictionaries

    def select_dictionary(self, filename):
        dictionary_found = 0
        dictionary_checking = 0
        while dictionary_found != 1:
            if self.list_of_json_dictionaries[dictionary_checking]['file_name'] == filename:
                dictionary_found = 1
                self.dictionary = self.list_of_json_dictionaries[dictionary_checking]
            dictionary_checking += 1
        return self.dictionary, dictionary_checking

    def add_dictionary_description(self, filename, description):  # should not need if add works
        self.select_dictionary(filename)
        self.dictionary['description'] = description
        return self.dictionary

    def add_experiment_number(self, filename, experiment_number):  # should not need if add works
        self.select_dictionary(filename)
        self.dictionary['experiment'] = experiment_number
        return self.dictionary

    def add_to_dictionary(self, filename, key, value):
        self.select_dictionary(filename)
        self.dictionary[key] = value
        return self.dictionary

    def json_to_dataframe(self, json_file):
        # Need to make second dataframe of just json data (anything in a list)
        # add second dataframe to dictionary entry
        self.dataframe = pd.read_json(json_file)
        # self.dataframe = pd.DataFrame  # Create second dataframe of changing variables
        return self.dataframe

    def get_json_data(self):
        # possibly make a second function which deepcopies the dataframe and removes unnecessary columns
        dataframe_columns = self.dataframe.columns.to_list()
        for i in dataframe_columns:  # loop through all variales in dataframe
            if self.dataframe[i] is type(
                    list):  # check if variable has a single value or is a list of values
                column_with_changing_data = self.dataframe.iloc[i]  # if a list add to second dataframe
                # Use dataframe_with_file_info.iloc[#] to get entire row or .loc['column/variable_name']
                # dataframe_with_changing_data append column
        return column_with_changing_data

    def jsons_to_dataframe_list(self):
        list_of_json_dataframes = []
        for i in range(len(self.list_of_json_files)):
            dataframe_with_file_data = self.json_to_dataframe(self.list_of_json_files[i])
            self.list_of_json_dataframes.append(dataframe_with_file_data)
            i = + 1
        return list_of_json_dataframes

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
    # test_load_data_to_dictionary()
    #test_load_data_to_dataframe()



