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
        self.fileName = ""
        self.description = ""
        self.dataFrames = {}  # doesn't work as a dictionary must be a list
        self.fileType = ""
        self.history = []
        self.id = uuid.uuid4()
        self.dictionary = {}
        #self.data_dictionary = DataDictionary.DataDictionary()

    def setAlias(self, alias):
        self.alias = alias

    def setDescription(self, description):
        self.description = description

    def generateUniqueId(self):
        return uuid.uuid4()

    def addDataFrame(self, dataFrame):  # ? how do I fix this so it's how I had it instead
        dataFrameId = self.generateUniqueId()
        self.dataFrames[dataFrameId] = dataFrame  # dataFrameId needs to be a string
        return dataFrameId

    def updateDataFrame(self, id, dataFrame, reason):
        self.dataFrames[id].update(dataFrame)
        self.dataFrames[id]['modified'] = True
        self.history.append({
            'dataFrameId': id,
            'reason': reason
        })

    def getDataFrameCopy(self, modified=False, deep=False):
        selectedDataFrame = self.getDataFrame(modified)
        if deep:
            selectedDataFrame = deepcopy(selectedDataFrame)
        else:
            selectedDataFrame = copy(selectedDataFrame)
        return selectedDataFrame

    def getDataFrames(self):
        dataFrames = []
        for dataFrame in self.dataFrames:
            dataFrames.append(dataFrame)
        return dataFrames

    def isModified(self, dataFrame):
        return dataFrame.modified

    def getDataFrame(self, modified=False):
        return filter(self.isModified, self.dataFrames)  # ? is modified requires a dataframe input??



