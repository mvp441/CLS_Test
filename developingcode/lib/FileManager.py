import os.path


import copy
import pandas as pd
import DataFile
from JsonManager import JsonManager
# from CsvManager import CsvManager
from config import config
from DataStore import data
from glob import glob
from TypeDataCatalog import TypeDataCatalog
from DataDictionary import DataDictionary

# https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
# https://pypi.org/project/singleton-decorator/?fbclid=IwAR0vUAXsSFI6G1el2EgjEQip7tdG3V29rnkCc0QhW6W8zNcBjoasu-zbZ6U

# file type managers are subclasses with shared parent variables
class FileManager:
    def __init__(self):
        self.data = data
        self.data_catalog = {
            'csv_data': TypeDataCatalog(),
            'json_data': TypeDataCatalog(),
            'txt_data': TypeDataCatalog(),
            'all_data': TypeDataCatalog(),
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
                'data': TypeDataCatalog(),
                'positions': TypeDataCatalog()
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
            #Read with JSON Manager
            JSON = JsonManager()
            dict = JSON.json_to_dictionary(path)
            JSON.json_to_dataframe(path)

            dataFrame = JSON.dataframe

            dataFile = self.data.addFile(file_name)
            dataFile.fileType = config['FILE_TYPES']['json']
            dataFile.fileName = os.path.basename(file_name)
            dataFile.description = 'My File Description'
            dataFile.addDataFrame(dataFrame)
            dataFile.setAlias("Example File Alias")
            return dataFile


        # elif file_extension.lower() == 'csv':
        #     csvManager = CsvManager(path)
        #     csvManager.load_csv_file()
        #     print(csvManager)
        #     # Read with CSV Manager
        # elif file_extension.lower() == 'txt':
        #     print('')

    def load_folder(self, folderPath, extension):
        files = []
        fileNames = glob(folderPath + "*." + extension)

        for path in fileNames:
            files.append(self.read_file(os.path.abspath(path)))
        return files


    # has functions for importing data into dataframes

    #def add_file()
        #if csv:
            #use CsvManager to add file to data store
            #csv_data.add_csv  # need to fix return so datastore object in file manager changes



# csv = os.path.basename('/home/parmarm/Documents/CLS_Test/PV Data/Trip 1 data/gLYHVdm+.csv')
# fileManager.read_file(csv)



