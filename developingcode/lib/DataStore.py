from DataFile import DataFile
import pandas as pd

class DataStore:
    def __init__(self):
        self.data = {}
        self.selected_dataframes = {}

    def add_file(self, fileName):
        self.data[fileName] = DataFile()
        return self.data[fileName]

    def get_file_data(self, fileName):
        return self.data[fileName]

    def get_data_by_file_type(self, fileType):
        dataValues = self.data.values()
        returnData = []
        for value in dataValues:
            if value.type.lower() == fileType.lower():
                returnData.append(value)
        return returnData

    def get_data_frames_by_file_type(self, fileType):
        data_files = self.get_data_by_file_type(fileType)
        data_frames = []
        for file in data_files:
            data_frames.append(file.getDataFrames())
        return data_frames

    def get_all_data_frames(self):
        data_files = self.data.values()  # might need to get data.keys() instead
        data_frames = []
        for file in data_files:
            data_frames.append(file.getDataFrames())
        return data_frames

    def add_file_name_to_inventory(self, file_name, file_extension):
        if file_extension.lower() == '.csv':
            self.data_inventory['dictionary_of_file_names']['list_of_csv'].append(file_name)
        elif file_extension.lower() == '.json':
            self.data_inventory['dictionary_of_file_names']['list_of_json'].append(file_name)
        elif file_extension.lower() == '.txt':
            self.data_inventory['dictionary_of_file_names']['list_of_txt'].append(file_name)
        self.data_inventory['dictionary_of_file_names']['list_of_all'].append(file_name)

    def get_file_names(self, type=None):
        fileNames = []
        for file in self.data.values():
            if type is None:
                fileNames.append(file.name)
                continue

            if type is not None and file is not None and type.lower() == file.type.lower():
                fileNames.append(file.name)
        return fileNames



    def to_dict(self):
        dict = {
            'file_names_by_type': {},
            'dataframes_by_type': {}
        }
        dict['file_names_by_type']['csv'] = self.get_file_names('csv')
        dict['file_names_by_type']['json'] = self.get_file_names('json')
        dict['file_names_by_type']['txt'] = self.get_file_names('txt')
        dict['file_names_by_type']['all'] = self.get_file_names()

        dict['dataframes_by_type']['json'] = self.get_data_frames_by_file_type('json')
        dict['dataframes_by_type']['csv'] = self.get_data_frames_by_file_type('csv')
        dict['dataframes_by_type']['txt'] = self.get_data_frames_by_file_type('txt')
                # raise Exception(self.data.values())

        # dict['dataframes_by_type']['all'] = self.get_all_data_frames()
        return dict

    # def add_dataframe_to_inventory(self,):


data = DataStore()
