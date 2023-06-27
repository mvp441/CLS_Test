from DataFile import DataFile
import pandas as pd
import singleton

class DataState:
    def __init__(self):
        self.data = {}
        self.selected_dataframes = {}

    def addFile(self, fileName):
        self.data[fileName] = DataFile()
        return self.data[fileName]

    def getFileData(self, fileName):
        return self.data[fileName]

    def getDataByFileType(self, fileType):
        dataValues = self.data.values()
        returnData = []
        for value in dataValues:
            print(value.fileType)
            if value.type == fileType:
                returnData.append(value)
        return returnData

    def getDataFramesByFileType(self, fileType):
        dataFiles = self.getDataByFileType(fileType)
        dataFrames = []
        for file in dataFiles:
            dataFiles.append(file.dataFrame)
        return dataFiles

    def getAllDataFrames(self):
        dataFiles = self.data.values()  # might need to get data.keys() instead
        dataFrames = []
        for file in dataFiles:
            dataFrames.append(file.getDataFrames())
        return dataFrames

    def add_file_name_to_inventory(self, file_name, file_extension):
        if file_extension.lower() == '.csv':
            self.data_inventory['dictionary_of_file_names']['list_of_csv'].append(file_name)
        elif file_extension.lower() == '.json':
            self.data_inventory['dictionary_of_file_names']['list_of_json'].append(file_name)
        elif file_extension.lower() == '.txt':
            self.data_inventory['dictionary_of_file_names']['list_of_txt'].append(file_name)
        self.data_inventory['dictionary_of_file_names']['list_of_all'].append(file_name)

    def getFileNames(self, type=None):
        fileNames = []
        for file in self.data.values():
            print(file.type.lower() == type.lower())
            if type is not None and type.lower() == file.type.lower():
                fileNames.append(file.name)
            elif type is None:
                fileNames.append(file.name)



    def toDictionary(self):
        dict = {
            'file_names_by_type': {}
        }
        dict['file_names_by_type']['csv'] = self.getFileNames('csv')
        dict['file_names_by_type']['json'] = self.getFileNames('json')
        dict['file_names_by_type']['txt'] = self.getFileNames('txt')
        dict['file_names_by_type']['all'] = self.getFileNames()

        return dict

    # def add_dataframe_to_inventory(self,):


data = DataState()
