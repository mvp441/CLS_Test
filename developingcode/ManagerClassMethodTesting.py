import os.path

from lib.FileManager import FileManager
from lib.config import config
from lib.DataFrameManager import dataFrameManager
from lib.DataStore import data

File = FileManager()


path1 = '/home/parmarm/Documents/CLS_Test/Data/tune-data/'
path2 = '/home/parmarm/Documents/CLS_Test/PV_Data/Trip_1_data/'

files = File.load_folder(path2, 'csv')

dataFrames = File.data.getAllDataFrames()

for frame in dataFrames:
    dataFrameManager.selectDataFrame(frame)
dataFrameManager.fillNa("median")

print('test')
