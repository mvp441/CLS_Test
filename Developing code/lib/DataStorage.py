import CsvManager, JsonManager
import copy
import pandas as pd

# object containing all the data information which is accessed and operated on by the manager classes
class DataStorage:
    # make a module instead of a class or else make it a singleton?
    def __init__(self, filelist):
        # old object variables
        self.list_of_all_file_names = copy.deepcopy(filelist)  # possibly switch deep copies once type check is set up
        self.list_of_csv_file_names = copy.deepcopy(filelist)
        # create dictionaries of lists as mentioned considering below
        self.dictionary_of_file_names = {
            'current': None,
            'list_of_csv': [],
            'list_of_json': [],
            'list_of_txt': [],
            'list_of_all': []
        }
        self.dictionary_of_dataframes = {
            'current': None,
            'list_of_csv': [],
            'list_of_json': [],
            'list_of_txt': [],
            'list_of_all': []
        }
        self.dictionary_of_dictionaries = {
            'current': None,
            'list_of_csv': [],
            'list_of_json': [],
            'list_of_txt': [],
            'list_of_all': []
        }
        self.data = {
            'files': {
                'data': {
                    'example': 102.44
                },
                'filetype': 'Json'
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
        #consider making a dictionary of lists for each thing:
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

