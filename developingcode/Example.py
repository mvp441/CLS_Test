import os.path

from lib.FileManager import FileManager
from lib.config import config
from lib.DataFrameManager import dataFrameManager
from lib.DataStore import data

File = FileManager()


path = '/home/parmarm/Documents/CLS_Test/Data/tune-data/'

files = File.load_folder(path, 'json')

dataFrames = File.data.getAllDataFrames()

# for frame in dataFrames:
#     dataFrameManager.selectDataFrame(frame)
#
# dataFrameManager.fillNa("median")

print('test')
