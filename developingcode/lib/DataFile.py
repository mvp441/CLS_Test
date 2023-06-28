import uuid
from copy import copy, deepcopy
import DataDictionary
import pandas as pd

# https://satoricyber.com/glossary/data-dictionary
# https://satoricyber.com/data-management/understanding-the-fundamentals-of-a-data-dictionary/

# object containing all the data information for a single file stored in the data (catalog and) inventory?
class DataFile:
    # make a module instead of a class or else make it a singleton?
    def __init__(self):
        self.alias = ""
        self.name = ""
        self.description = ""
        self.dataFrames = []
        self.type = ""
        self.history = []
        self.id = str(uuid.uuid4())
        #self.data_dictionary = DataDictionary.DataDictionary()

    def set_alias(self, alias):
        self.alias = alias

    def set_description(self, description):
        self.description = description

    def generate_id(self):
        return str(uuid.uuid4())

    def add_data_frame(self, dataFrame, modified=False):  # ? how do I fix this so it's how I had it instead
        dataFrameId = self.generate_id()
        newDataFrame = {
            'id': dataFrameId,
            'dataFrame': dataFrame,
            'modified': modified,
            'history': []
        }

        self.dataFrames.append(newDataFrame)
        return newDataFrame        
    
    def update_data_frame(self, dataFrame, reason):
        current_dataframe = self.dataFrames[-1]
        
        if current_dataframe['modified'] is False:
            # Create the new modified dataframe
            newFrame = self.add_data_frame(dataFrame, True)
            newFrame['history'].append(reason)
        else:
            # Update the modified dataframe
            current_dataframe['dataFrame'] = dataFrame
            current_dataframe['history'].append(reason)
    


    def get_dataframe_copy(self, modified=False, deep=False):
        selectedDataFrame = self.get_data_frame(modified)
        if deep:
            selectedDataFrame = deepcopy(selectedDataFrame)
        else:
            selectedDataFrame = copy(selectedDataFrame)
        return selectedDataFrame


    
    def is_modified(self, dataframe):
        return dataframe['modified']
    
    def get_data_frame(self, modified=False):
        dataframes = filter(lambda df: df['modified'] is modified ,self.dataFrames)
        return list(dataframes)[-1]['dataFrame']

    def get_current_frame(self):
        modified = self.get_dataframe_copy(modified=True)
        if modified:
            return modified
        else:
            return self.get_dataframe_copy()


