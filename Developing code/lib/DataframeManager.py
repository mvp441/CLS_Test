# dataframe methods
import DataDictionary
import pandas as pd
import copy

class DataframeManager:
    def __init__(self, filelist):
        # old object variables
        self.list_of_all_file_names = copy.deepcopy(
            filelist)  # possibly switch deep copies once type check is set up
        self.list_of_csv_file_names = copy.deepcopy(filelist)
        # create dictionaries of lists as mentioned considering below
        self.data_dictionary = {
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
            'current_data': {
                'file_names': [],
                'dataframes': [],
                'dictionaries': []
            },
            'dictionary_of_file_names': {
                'current': None,
                'list_of_csv': [],
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_all': []
            },
            'dictionary_of_dataframes': {
                'current': None,
                'list_of_csv': [],
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_all': []
            },
            'dictionary_of_dictionaries': {
                'current': None,
                'list_of_csv': [],
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_all': []
            }
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
    #def df_method(self):