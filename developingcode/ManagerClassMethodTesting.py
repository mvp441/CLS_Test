import os.path

from lib.FileManager import FileManager
from lib.config import config
from lib.DataFrameManager import df_manager
from developingcode.lib.DataStore import data_store

File = FileManager()

path1 = '/home/parmarm/Documents/CLS_Test/Data/tune-data/'
path2 = '/home/parmarm/Documents/CLS_Test/PV_Data/Trip_1_data/'

files = File.load_folder(path1, 'json')

dataFrames = File.data.get_all_data_frames()

for frame in dataFrames:
    df_manager.select(frame)
df_manager.fill_na_values("median")

print('test')
