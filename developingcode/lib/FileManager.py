import os.path
import copy
import pandas as pd
import DataFile
from JsonManager import JsonManager
import CsvManager
from config import config
from DataStore import data
from glob import glob
from DataDictionary import DataDictionary

# https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
# https://pypi.org/project/singleton-decorator/?fbclid=IwAR0vUAXsSFI6G1el2EgjEQip7tdG3V29rnkCc0QhW6W8zNcBjoasu-zbZ6U

# has functions for importing files into datastore
class FileManager:
    def __init__(self):
        self.data = data
        # self.data_catalog = {
        #     'csv_data': {
        #         'file_names': DataStore.data.data_inventory['dictionary_of_file_names']['list_of_csv'],
        #         'dataframes': DataStore.data.data_inventory['dictionary_of_dataframes']['list_of_csv'],
        #         'dictionaries': DataStore.data.data_inventory['dictionary_of_dictionaries']['list_of_csv']
        #     },
        #     'json_data': {
        #         'file_names': DataStore.data.data_inventory['dictionary_of_file_names']['list_of_json'],
        #         'dataframes': DataStore.data.data_inventory['dictionary_of_dataframes']['list_of_json'],
        #         'dictionaries': DataStore.data.data_inventory['dictionary_of_dictionaries']['list_of_json']
        #     },
        #     'txt_data': {
        #         'file_names': DataStore.data.data_inventory['dictionary_of_file_names']['list_of_txt'],
        #         'dataframes': DataStore.data.data_inventory['dictionary_of_dataframes']['list_of_txt'],
        #         'dictionaries': DataStore.data.data_inventory['dictionary_of_dictionaries']['list_of_txt']
        #     },
        #     'all_data': {
        #         'file_names': DataStore.data.data_inventory['dictionary_of_file_names']['list_of_all'],
        #         'original_dataframes': DataStore.data.data_inventory['dictionary_of_dataframes']['list_of_original'],
        #         'current_dataframes': DataStore.data.data_inventory['dictionary_of_dataframes']['list_of_current'],
        #         'dictionaries': DataStore.data.data_inventory['dictionary_of_dictionaries']['list_of_all']
        #     },
        #     'current_file': {
        #         'file_name': None,
        #         'dataframe': pd.DataFrame,
        #         'dictionary': DataDictionary,
        #         'list_position': {
        #             'file_name': None,
        #             'dataframe': None,
        #             'dictionary': None
        #         }
        #     },
        #     'current_data': {
        #         'data': {
        #             'file_names': [],
        #             'dataframes': [],
        #             'dictionaries': []
        #         },
        #         'positions': {
        #             'file_names': [],
        #             'dataframes': [],
        #             'dictionaries': []
        #         }
        #     },
        #     'master_data': {
        #         'file_names': [],
        #         'original_dataframe': pd.DataFrame,
        #         'current_dataframe': pd.DataFrame,
        #         'dictionary': DataDictionary
        #     },
        #     'correlation_data': {
        #         'file_names': DataStore.data.data_inventory['correlation_data']['list_of_files'],
        #         'dataframes': DataStore.data.data_inventory['correlation_data']['list_of_dataframes'],
        #         'dictionary': DataDictionary
        #     }
        # }

    # Read Multiple CSV Files from a Folder
    # https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/

    # Add files
    # def add_file(self):

    # input file name(s) to add
    # add file names to list
    # go through list
    #   check file type
    #   save in according places for type
    #   create dictionary entry for each file
    #       store file name
    #       convert file to dataframe
    #       save original dataframe in dictionary
    #   store dictionary entry in list
    # create master dataframe from list00

    # file type detection
    # https://stackoverflow.com/questions/54698130/determine-if-a-file-is-more-likely-json-or-csv
    # just check extension and split into lists of file names by each type

    # add check for if file has already been added

    def parse_path(self, path):
        file_name, file_extension = os.path.splitext(path)
        return [file_name, file_extension]

    def read_file(self, path):
        file_name, file_extension = self.parse_path(path)
        if file_extension.lower() == '.json':
            # Read with JSON Manager
            JSON = JsonManager()
            dict = JSON.json_to_dictionary(path)
            JSON.json_to_dataframe(path)
            dataFrame = JSON.dataframe

            # Create the datafile
            dataFile = self.data.add_file(file_name)
            dataFile.type = config['FILE_TYPES']['json']
            dataFile.name = os.path.basename(file_name)
            dataFile.addDataFrame(dataFrame)
            
            return dataFile
        elif file_extension.lower() == 'csv':
            csvManager = CsvManager(path)
            csvManager.load_csv_file()
            print(csvManager)
            # Read with CSV Manager
        # elif file_extension.lower() == 'txt':
        #     print('')

    def load_filenames_from_folder(self, folder_location='/home/parmarm/Documents/CLS_Test/Data/tune-data', file_name='/*.json'):
        self.list_of_file_names = glob(folder_location + file_name)

    def load_folder(self, folderPath, extension):
        files = []
        fileNames = glob(folderPath + "*." + extension)
        for path in fileNames:
            files.append(self.read_file(os.path.abspath(path)))
        return files

    '''
    # def add_txt(self, txt):
    # copy from experiment.py file or make TxtManager class file?

    # def add_json(self, json):
    # copy from JsonManager class file?

    # Read Multiple CSV Files from a Folder
    # https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/
    # def add_CSV_files_from_folder(self, path=None):

    # def add_txt_files_from_folder(self, path=None):
    # def add_json_files_from_folder(self, path=None):
    # def add_files_from_folder(self, path=None):
    
    def load_csv_file(self):
        for csv in self.list_of_csv_file_names:
            self.add_csv_to_dictionary(csv)  # new - check if it should just be add_csv function
            # self.__add_csv_to_dataframe(csv)  # old

    # modify to add in multiple csv files at a time instead of modifying this function create which adds all in the list
    def add_csv(self, csv):
        self.list_of_all_file_names.append(
            csv)  # should be in but add again because initialized since missing type check
        self.list_of_csv_file_names.append(csv)
        self.add_csv_to_dictionary(csv)
        # self.csv_files.append(csv)
        # self.__add_csv_to_dataframe(csv)

    def add_csv_to_dictionary(self, csv):
        # https://www.educative.io/answers/how-to-create-a-dictionary-of-data-frames-in-python
        self.dataframe_file_name = csv
        self.csv_to_df(csv)
        if len(self.list_of_file_dictionaries) > 1:
            self.dataframe_list_position = len(self.list_of_file_dictionaries) - 1
        else:
            self.dataframe_list_position = len(self.list_of_file_dictionaries)
        self.convert_csv_timestamp()
        dataframe_info = {
            'file_name': csv,
            'file_type': 'csv',
            'list_position': self.dataframe_list_position,
            'list_of_column_names': self.get_column_names(),
            'original_dataframe': self.dataframe,
            'modified_dataframe': None,
            'modification_history': []
        }
        # self.__add_csv_to_dataframe(csv)  # old
        # if master is at the end of list remove it before adding new one
        if self.list_of_file_dictionaries is not None:
            if len(self.list_of_file_dictionaries) > 1:
                self.list_of_file_dictionaries.remove(
                    self.list_of_file_dictionaries[len(self.list_of_file_dictionaries) - 1])
        self.list_of_file_dictionaries.append(dataframe_info)
        # self.prepare_csv_df()  # not sure if this will work as intended need to test still
        self.construct_master_dictionary(modified=False)

    def csv_to_df(self, csv):
        self.dataframe = pd.read_csv(csv)
        self.list_of_original_dataframes.append(self.dataframe)
        self.list_of_csv_dataframes.append(self.dataframe)
        # if master is at the end of list remove it before adding new one
        if self.list_of_file_dataframes is not None:
            if len(self.list_of_file_dataframes) > 1:
                self.list_of_file_dataframes.remove(self.list_of_file_dataframes[len(self.list_of_file_dataframes) - 1])
        self.list_of_file_dataframes.append(self.dataframe)
        # self.construct_master_dictionary(modified=False)  moved to csv to dict function 
        
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
        self.dataframe_dictionary_list.append(self.dictionary)
    
    def jsons_to_dictionary_list(self):
        self.list_of_json_dictionaries = []
        key_list_list = []
        for i in range(len(self.list_of_file_names)):
            self.json_to_dictionary(self.list_of_file_names[i])
            self.list_of_json_dictionaries.append(self.dictionary)
            i = + 1
    
    # Construct master dataframe from list of modified (or original if no modified) dataframes
    def construct_master_dictionary(self, modified=True):
        self.construct_master_dataframe(modified)
        if not modified:
            self.master_dictionary['original_dataframe'] = self.master_dataframe
        else:
            self.master_dictionary['modified_dataframe'] = self.master_dataframe
        self.master_dictionary['list_position'] = len(self.list_of_file_dictionaries) - 1
        self.master_dictionary['list_of_column_names'] = self.master_dataframe.columns.to_list()
        self.list_of_file_dictionaries.append(self.master_dictionary)

    def get_dataframe_file_name(self):
        if self.dataframe_list_position == len(self.list_of_file_dictionaries):
            self.dataframe_file_name = 'master'
        else:
            self.dataframe_file_name = self.list_of_file_dictionaries[self.dataframe_list_position]['file_name']

    def select_file_dictionary(self, file_name='master', list_position=0):
        file_found = False
        self.file_list_position = list_position
        while file_found is not True:
            if file_name == 'master':
                file_found = True
                self.file_dictionary = copy.copy(self.master_dictionary)
            elif self.list_of_file_dictionaries[self.file_list_position]['file_name'] == file_name:
                file_found = True
                self.file_dictionary = copy.copy(self.list_of_file_dictionaries[self.file_list_position])
            else:
                self.file_list_position += 1

    # def select_multiple_files(self, list_of_filenames):
    
    def select_dictionary(self, filename):
        dictionary_found = 0
        dictionary_checking = 0
        while dictionary_found != 1:
            if self.list_of_json_dictionaries[dictionary_checking]['file_name'] == filename:
                dictionary_found = 1
                self.dictionary = self.list_of_json_dictionaries[dictionary_checking]
            dictionary_checking += 1    
        
    def select_dataframe(self, dataframe_name=None, modified=True, list_position=0):
        if dataframe_name is None:
            dataframe_name = self.dataframe_file_name
        self.unselect_dataframe()
        self.dataframe_list_position = list_position
        dataframe_found = False
        while dataframe_found is not True:
            if dataframe_name is not 'master':
                if self.list_of_file_dictionaries[self.dataframe_list_position]['file_name'] == dataframe_name:
                    dataframe_found = True
                    if modified and self.list_of_file_dictionaries[self.dataframe_list_position][
                        'modified_dataframe'] is not None:
                        self.dataframe = copy.copy(self.list_of_file_dictionaries[self.dataframe_list_position][
                                                       'modified_dataframe'])  # maybe deep copy to save versions later
                    else:
                        self.dataframe = copy.deepcopy(
                            self.list_of_file_dictionaries[self.dataframe_list_position]['original_dataframe'])
                    self.dataframe_file_name = dataframe_name
                if self.dataframe_list_position + 1 < len(self.list_of_file_dictionaries):
                    self.dataframe_list_position += 1
                else:
                    dataframe_name = 'master'
            else:
                dataframe_found = True
                if modified and self.master_dictionary['modified_dataframe'] is not None:
                    self.dataframe = copy.copy(self.master_dictionary['modified_dataframe'])
                else:
                    self.dataframe = copy.deepcopy(self.master_dictionary['original_dataframe'])
                self.dataframe_file_name = 'master'
        self.select_file_dictionary(list_position=self.dataframe_list_position)

    def unselect_dataframe(self):
        if self.dataframe is not None:
            # possibly save current file before so that can reload it after if different
            self.get_dataframe_file_name()
            self.select_file_dictionary(self.dataframe_file_name)
            self.file_dictionary['modified_dataframe'] = copy.deepcopy(self.dataframe)
            self.dataframe = pd.DataFrame

    def output_csv_list(self):
        for csv in range(len(self.list_of_csv_file_names)):
            print(self.list_of_csv_file_names[csv])
        # test print(self.csv_files)?
        
    def clean_up_correlation_matrix(self):
        print('clean up corr_mat')

    def output_correlation_matrix(self):
        print(tabulate(self.correlation_matrix, headers='keys', tablefmt='rst'))
        
    def plot_correlation_matrix(self):
        plt.figure()
        heat_map = sns.heatmap(self.correlation_matrix, annot=True, cmap='Spectral')  # heat_map = that?
        plt.show()
        print('done plotting')
            '''

    # def add_file()
    # if csv:
    # use CsvManager to add file to data store
    # csv_data.add_csv  # need to fix return so datastore object in file manager changes

# csv = os.path.basename('/home/parmarm/Documents/CLS_Test/PV_Data/Trip_1_data/gLYHVdm+.csv')
# fileManager.read_file(csv)
