import CsvManager, JsonManager
import copy
import pandas as pd


# https://satoricyber.com/glossary/data-dictionary
# https://satoricyber.com/data-management/understanding-the-fundamentals-of-a-data-dictionary/

# object containing all the data information for a single file stored in the data (catalog and) inventory?
class DataFile:
    # make a module instead of a class or else make it a singleton?
    def __init__(self):
        self.data = {
            'files': {
                'data': {
                    'example': 102.44
                },
                'filetype': 'Json'
            }
        }
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

