from DataFile import DataFile
import pandas as pd

class DataStore:
    def __init__(self):
        #self.data = {}
        self.dataFrames = {}
        self.data= {
            'dictionary_of_file_names': {
                'list_of_csv': [],
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_all': []
            },
            'dictionary_of_dataframes': {
                'list_of_csv': [],  # self.list_of_csv_dataframes = []
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_original': [],
                'list_of_current': []
            },
            'dictionary_of_dictionaries': {
                'list_of_csv': [],
                'list_of_json': [],
                'list_of_txt': [],
                'list_of_all': []
            },
            'correlation_data': {
                'list_of_files': None,
                'list_of_dataframes': None,
                'input_dataframe': pd.DataFrame,
                'correlation_matrix': pd.DataFrame,  # self.correlation_matrix = pd.DataFrame
                'correlation_pairs': []
            }
        }

    def addFile(self, fileName):
        self.data[fileName] = DataFile()
        return self.data[fileName]

    def getFileData(self, fileName):
        return self.data[fileName]

    def getFilesByTpe(self, fileType):
        dataValues = self.data.values()
        returnData = []
        for value in dataValues:
            print(value.fileType)
            if value.fileType == fileType:
                returnData.append(value)
        return returnData

    def getAllDataFrames(self):
        dataFiles = self.data.values()
        dataFrames = []
        for file in dataFiles:
            dataFrames.append(file.getDataFrames())
        return dataFrames



data = DataStore()