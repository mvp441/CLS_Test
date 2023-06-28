from lib.FileManager import FileManager
from lib.DataFrameManager import df_manager
from lib.config import config

from lib.DataStore import data

import os

File = FileManager()

workingDirectory = os.getcwd()


jsonsFolder = workingDirectory + '/Data/tune-data/'
csvFolder = workingDirectory + '/PV_Data/Trip_1_data/'

File.load_folder(jsonsFolder, 'json')

data_dictionary = data.to_dict()
print("Hello")
raise Exception("Hello")