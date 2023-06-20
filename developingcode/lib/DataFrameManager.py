from copy import copy, deepcopy
class DataFrameManager:
    def __init__(self):
        self.selectedDataFrames = {}

    def copy(self, dataFrame):
        return copy(dataFrame)

    def deepCopy(self, dataFrame):
        return deepcopy(dataFrame)

    def selectDataFrame(self, dataFile, deep=False, modified=False):
        self.selectedDataFrames[dataFile.id] = dataFile.getDataFrameCopy(modified, deep)

    def unselectDataFrame(self, dataFile):
        del self.selectedDataFrames[dataFile.id]

    def getSelected(self):
        return self.selectedDataFrames.values()

    def dropNa(self, axis=0):
        for dataFrame in self.selectedDataFrames:
            dataFrame.dropna(axis=axis, inplace=True)

    def fillColumnValues(self, dataFrame, fillValues):
        for column in dataFrame.columns[1:]:
            fill_value = fillValues[column]
            dataFrame.fillna(fill_value, axis="rows", inplace=True)

    def fillNa(self, method="pad"):
        selectedDataFrames = self.selectedDataFrames.values()
        if type(method) == int or type(method) == float:
            for dataframe in selectedDataFrames:
                dataframe.fillna(method, axis='rows',
                                      inplace=True)  # Has been initially tested and is working at the moment
        elif method in ['mean', 'median', 'mode']:
            if method == 'mean':
                for dataframe in selectedDataFrames:
                    fill_values = dataframe.mean(axis=0, skipna=True)
                    self.fillColumnValues(dataframe, fill_values)
            if method == 'median':  # Has been initially tested and is working at the moment
                for dataframe in selectedDataFrames:
                    fill_values = dataframe.median(axis=0, skipna=True)
                    self.fillColumnValues(dataframe, fill_values)
            elif method == 'mode':
                for dataframe in selectedDataFrames:
                    fill_values = dataframe.mode(axis=0, skipna=True)
                    self.fillColumnValues(dataframe, fill_values)
        elif method in ['backfill', 'bfill', 'ffill', 'pad']:
            if method == 'backfill':
                for dataframe in selectedDataFrames:
                    dataframe.fillna(method='backfill', inplace=True)
            if method == 'bfill':
                for dataframe in selectedDataFrames:
                    dataframe.fillna(method='bfill', inplace=True)
            if method == 'ffill':
                for dataFrame in selectedDataFrames:
                    dataframe.fillna(method='ffill', inplace=True)
            if method == 'pad':  # Has been initially tested and is working at the moment
                for dataFrame in selectedDataFrames:
                    dataframe.fillna(method='pad', inplace=True)

    def interpolateData(self, method='polynomial', order=1):
        selectedDataFrames = self.selectedDataFrames.values()
        if order is None:
            if method == 'linear':
                # check if method == method and calling like poly 1 works
                for dataframe in selectedDataFrames:
                    dataframe.interpolate(method='linear', inplace=True)
        elif method == 'polynomial':
            # typecheck order is int
            for dataframe in selectedDataFrames:
                if str(order) == '1':  # can remove int check
                    dataframe.interpolate(method=method, order=order, inplace=True)
                elif str(order) == '2':
                    dataframe.interpolate(method='polynomial', order=2, inplace=True)
                elif str(order) == '3':
                    dataframe.interpolate(method='polynomial', order=3, inplace=True)
                elif str(order) == '4':
                    dataframe.interpolate(method='polynomial', order=4, inplace=True)
                elif str(order) == '5':
                    dataframe.interpolate(method='polynomial', order=5, inplace=True)


dataFrameManager = DataFrameManager()