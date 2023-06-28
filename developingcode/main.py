from lib.FileManager import FileManager
from lib.config import config

from lib.DataStore import data_store
from lib.DataFrameManager import dataframe_manager
import random
import os
workingDirectory = os.getcwd()
jsonsFolder = workingDirectory + '/Data/tune-data/'
csvFolder = workingDirectory + '/PV_Data/Trip_1_data/'


File = FileManager()
File.load_folder(csvFolder)
File.load_folder(jsonsFolder)

data_inventory = data_store.to_dict()

dataframe_manager.select_all(data_store.data)

for df in dataframe_manager.get_selected():
  data_store.master_data['all'].add_data_frame(df)

dataframe_manager.modify('conert_ts')
dataframe_manager.modify('convert_ti')
dataframe_manager.modify('mean')




# dataframe_manager.save_selected()



print("Hello")