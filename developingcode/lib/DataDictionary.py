# dataframe methods
import DataFile
import pandas as pd
import copy

class DataDictionary:
    def __init__(self, filelist):
        self.data_dictionary = {
                    'file_name': None,
                    'alias': None,
                    'description': None,
                    'file_type': None,
                    'list_position': None,
                    'list_of_column_names': None,
                    'original_dataframe': None,
                    'modified_dataframe': None,
                    'modification_history': []
                    # size?
                }

        #dictionary helper functions

    ''' 
    def add_dictionary_information(self):
        # possibly remove the following two lines for non experiment use or make optional
        self.dictionary['experiment'] = None  # add
        self.dictionary['description'] = None  # to identify and distinguish files
        self.json_to_dataframe(self.dictionary['file_name'])
        # self.dictionary['original_data'] = copy.deepcopy(self.get_json_data())

    def add_dictionary_description(self, filename, description):  # should not need if add works
        self.select_dictionary(filename)
        self.dictionary['description'] = description

    def add_experiment_number(self, filename, experiment_number):  # should not need if add works
        self.select_dictionary(filename)
        self.dictionary['experiment'] = experiment_number

    def add_to_dictionary(self, filename, key, value):
        self.select_dictionary(filename)
        self.dictionary[key] = value'''
