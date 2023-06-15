import CsvManager, JsonManager
import copy
import pandas as pd

class DataStorage:
    def __init__(self, filelist):
        self.list_of_all_file_names = copy.deepcopy(filelist)  # possibly switch deep copies once type check is set up
        self.list_of_csv_file_names = copy.deepcopy(filelist)
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
            "file_name": "master",
            "list_position": 0,  # Maybe initialize to None
            "list_of_column_names": [],
            "original_dataframe": self.master_dataframe,
            "modified_dataframe": None,
            "modification_history": []
        }
        self.correlation_matrix = pd.DataFrame
        self.correlation_pairs_list = []
