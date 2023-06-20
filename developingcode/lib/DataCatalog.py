import CsvManager, JsonManager
import copy
import pandas as pd
import DataFile
import DataInventory

# https://satoricyber.com/data-management/data-catalog/
# https://satoricyber.com/glossary/data-catalog/?l=l-middle&f=what-is-a-data-inventory-and-why-is-it-important
'''Data Mapping is an essential function of a Data Catalog. It heavily relies on Data Inventory, but it is a function for searching and integrating different aspects of the Data Catalog. It is not the data itself or a particular element of the Data Catalog.'''

# object containing all the data information for a single file(type?) stored in the data catalog and inventory?

# make a singleton object called within each datamanager class that includes(imports) the data inventory?
# or make it a module with an instance of the inventory singleton class?
# or make it a singleton class same as the data inventory and call it in the file manager module? - PROBABLY THIS

class DataCatalog:
    # make a module instead of a class or else make it a singleton?
    def __init__(self, filelist):
        # map dictionary entries to corresponding data inventory object location
        self.data_catalog = {
            'csv_data': {
                'file_names': [],
                'dataframes': [],
                'dictionaries': []
            },
            'json_data': {
                'file_names': [],
                'dataframes': [],
                'dictionaries': []
            },
            'txt_data': {
                'file_names': [],
                'dataframes': [],
                'dictionaries': []
            },
            'all_data': {
                'file_names': [],
                'dataframes': [],
                'dictionaries': []
            },
            'current_file': {
                'file_name': None,
                'dataframe': pd.DataFrame,
                'dictionary': DataDictionary,
                'list_position': {
                    'file_name': None,
                    'dataframe': None,
                    'dictionary': None
                }
            },
            'current_data': {
                'list_of_file_names': [],
                'list_of_dataframes': [],
                'list_of_dictionaries': [],
                'list_positions': {
                    'file_names': [],
                    'dataframes': [],
                    'dictionaries': []
                }
            },
            'master_data': {
                'file_names': [],
                'dataframes': [],
                'dictionary': DataDictionary
            },
            'correlation_data': {
                'file_names': [],
                'dataframes': [],
                'dictionary': DataDictionary
            }
        }
        self.list_of_csv_dataframes = []
        # create dictionary for current dataframe with name and list positions
        self.dataframe = pd.DataFrame()  # Currently selected dataframe - maybe have this seperate or different for selecting and looking at a subset of all files
        self.dataframe_file_name = None  # Filename of currently selected dataframe
        self.list_of_file_dataframes = []  # List of current dataframes from each file
        self.dataframe_list_position = 0
        self.file_dictionary = {}  # Currently selected file
        self.list_of_file_dictionaries = []  # List of dictionaries for each file
        self.file_list_position = 0
        self.list_of_original_dataframes = []
        # consider making a dictionary of lists for each thing:
        # file types: csvs, json, txt (filenames, dataframes, and dictionaries),
        # filenames (each file type and all),
        # dataframes (current, master, original, modified, file type)
        self.master_dataframe = pd.DataFrame()  # Concatenated all Dataframes
        self.master_dictionary = {
            'file_name': 'master',
            'list_position': 0,  # Maybe initialize to None
            'list_of_column_names': [],
            'original_dataframe': self.master_dataframe,
            'modified_dataframe': None,
            'modification_history': []
        }
        self.correlation_matrix = pd.DataFrame
        self.correlation_pairs_list = []

        #json.dumps(dictionary) saves dic to file

# file manager class adds data to object from files using file type manager classes
# dataframe manager class access object to modify dataframes

    # use pickle to store object https://www.askpython.com/python/examples/save-data-in-python



