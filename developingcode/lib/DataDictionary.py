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


