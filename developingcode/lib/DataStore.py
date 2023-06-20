from DataFile import DataFile
class DataStore:
    def __init__(self):
        self.data = {}
        self.dataFrames = {}

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