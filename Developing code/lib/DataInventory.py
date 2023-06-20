import Singleton
import CsvManager, JsonManager
import copy
import pandas as pd

# https://satoricyber.com/glossary/data-inventory
# https://satoricyber.com/data-management/what-is-a-data-inventory-and-why-is-it-important/?l=l-middle&f=gu-understanding-the-fundamentals-of-a-data-dictionary
'''While a Data Catalog is the whole system, which incorporates different informational tools, including the data, Data Inventory is the actual collection of data. It is an important function of the Data Catalog, but it is not the same as the data catalog.'''


# object containing all the data information which is accessed and operated on by the manager classes
#@Singleton ?
class DataInventory:
    # make a module instead of a class (or else make it a singleton?) consisting of lists of data dictionaries
    # or make a singleton class object comprised of lists and instantiated in catalog module
    def __init__(self):
        self.data_inventory = {
            'dictionary_of_file_names': {
                'list_of_csv': [],
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_all': []
            },
            'dictionary_of_dataframes': {
                'list_of_csv': [],  # self.list_of_csv_dataframes = []
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_original': [],
                'list_of_current': []
            },
            'dictionary_of_dictionaries': {
                'list_of_csv': [],
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_all': []
            },
            'correlation_data': {
                'list_of_files': None,
                'list_of_dataframes': None,
                'input_dataframe': pd.DataFrame,
                'correlation_matrix': pd.DataFrame,  # self.correlation_matrix = pd.DataFrame
                'correlation_pairs': []
            }
        }

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

        self.correlation_pairs_list = []

        # json.dumps(dictionary) saves dic to file

# file manager class adds data to object from files using file type manager classes
# dataframe manager class access object to modify dataframes

# use pickle to store object https://www.askpython.com/python/examples/save-data-in-python