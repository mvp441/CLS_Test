from lib.FileManager import FileManager
from lib.DataFrameManager import dataFrameManager
from lib.config import config
from lib.DataState import data as dataState


File = FileManager()
jsonsFolder = '/home/parmarm/Documents/CLS_Test/Data/tune-data/'
csvFolder = '/home/parmarm/Documents/CLS_Test/PV_Data/Trip_1_data/'

files = File.load_folder(jsonsFolder, 'json')

data_dictionary = dataState.toDictionary()
print("Hello")