from copy import copy, deepcopy
import datetime
from tabulate import tabulate
from DataStore import data_store
import pandas as pd

class DataFrameManager:
    def __init__(self):
        self.selectedDataFrames = {}

    def copy(self, dataFrame):
        return copy(dataFrame)

    def deep_copy(self, dataFrame):
        return deepcopy(dataFrame)

    def select(self, dataFile, deep=True, modified=False):
        self.selectedDataFrames[dataFile.id] = dataFile.get_dataframe_copy(modified, deep)

    def select_all(self, dataFiles, deep=False, modified=False):
        for dataFile in dataFiles.values():
            self.select(dataFile, deep, modified)

    def save_selected(self):
        for key, value in self.selectedDataFrames.items():
            dataFrame = data_store.get_by_id(key)
            dataFrame.update_data_frame(value, 'saved')

    def unselect_all(self):
        self.selectedDataFrames = {}

    def unselect(self, dataFile):
        del self.selectedDataFrames[dataFile.id]

    def get_selected(self):
        return self.selectedDataFrames.values()

    def get_selected_by_id(self, id):
        return self.selectedDataFrames[id]
    
    def apply_to_selected(self, method):
        for dataFrame in self.selectedDataFrames.values():
            print('Running method: ' + str(method) + ' on dataframe: ' + str(dataFrame))
            method(dataFrame)


    def convert_timestamp_to_datetime(self, dataFrame):
        dataFrame['Timestamp'].apply(pd.to_datetime)

    def prepare_csv_df(self, dataFrame):
        self.modify(method='convert_ts', modified=False)
        self.modify(method='convert_ti', modified=True)


    def modify(self, method='polynomial', order=1):
        # check modification method
        if method == 'drop':
            # modify
            self.drop_na_values()
        elif method in ['mean', 'median', 'mode', 'backfill', 'bfill', 'ffill', 'pad']:
            self.fill_na_values(method)
        elif method == 'convert_ts':
            self.apply_to_selected(self.convert_timestamp_to_datetime)
        elif method == 'convert_ti':
            self.apply_to_selected(lambda df: self.convert_time_interval(df, column='PCT1402-01:timeInterval:fbk'))
        else:
            self.interpolate_data(method, order)
        
        self.save_selected()

        # eventually save all versions into a list of dictionaries containing the modified dataframe and modification history
        
    def sort_by_column(self, columns):
        self.apply_to_selected(lambda df: df.sort_values(columns))

    def get_column_names(self):
        column_names = self.apply_to_selected(lambda df: df.columns.to_list())
        return column_names
    
    def get_column_values(self, column):
        column_values = self.apply_to_selected(lambda df: df[column].to_list())
        return column_values
    
    def output_dataframe_to_console(self, dataframe):
        print(tabulate(dataframe, headers='keys', tablefmt='rst'))

    def print_columns(self, dataframe, column_list=None):
        if column_list is None:
            column_list = dataframe.columns.to_list()
        for column in column_list:
            print(dataframe[column])
            print('\n')
    
    def get_list_description(self, dataframe): 
        dataframe_description = list()
        dataframe_description.append(dataframe.describe())
        for column in dataframe:
            dataframe_description.append(dataframe[column].describe())
        return dataframe_description
    
    def get_dictionary_description(self, dataframe):
        dataframe_description = {}
        for column in dataframe:
            dataframe_description[column] = dataframe[column].describe()
        return dataframe_description
    '''    
    

   

    def construct_master_dataframe(self, modified=True):
        # check current status of master dataframe
        if len(self.master_dataframe.columns.to_list()) == 0:
            self.master_dataframe = dataFrame
        else:
            # 4. Assigning Keys to the Concatenated DataFrame Indexes to distinguish each individual dataframe from list within master
            # https://www.digitalocean.com/community/tutorials/pandas-concat-examples
            if modified:
                self.list_of_file_dataframes.remove(self.list_of_file_dataframes[len(self.list_of_file_dataframes) - 1])
                self.master_dataframe = pd.concat(self.list_of_file_dataframes, ignore_index=True, sort=False)
                self.list_of_file_dataframes.append(self.master_dataframe)
            else:
                self.master_dataframe = pd.concat(self.list_of_original_dataframes, ignore_index=True, sort=False)
        self.master_dataframe.sort_values('Timestamp', inplace=True)
        self.list_of_file_dataframes.append(self.master_dataframe)
        


    
    

   

   

    # def remove_columns(self, columns_to_remove):
    # NEED TO DO NEXT BEFORE CORRELATION

    

   

  


    # def calculate_percent_change(self):
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html
        '''
    
    def convert_time_interval(self, dataFrame, column='PCT1402-01:timeInterval:fbk'):  # set default to all time intervals?
    # problem not converting any currently for master (probably because when/if called for master no column is given)
        for i in range(len(dataFrame.loc[:, column])):
            if str(dataFrame.loc[i, column]) != 'nan':
                offset_time = datetime.datetime(1900, 1, 1)
                if 'min' in dataFrame.loc[i, column]:
                    if 'sec' in dataFrame.loc[i, column]:
                        input_time = pd.to_datetime(dataFrame.loc[i, column].strip(), format='%M min %S sec')
                        delta = input_time - offset_time
                        dataFrame.loc[i, column] = delta.total_seconds()
                    else:
                        input_time = pd.to_datetime(dataFrame.loc[i, column].strip(), format='%M min')
                        delta = input_time - offset_time
                        dataFrame.loc[i, column] = delta.total_seconds()
                else:
                    input_time = pd.to_datetime(dataFrame.loc[i, column].strip(), format='%S sec')
                    delta = input_time - offset_time
                    dataFrame.loc[i, column] = delta.total_seconds()
            else:
                float(dataFrame.loc[i, column])
        dataFrame[column] = dataFrame[column].astype(float)
    
    def calculate_mean(self, dataFrame, columns=None):  # keep columns=none?
        df_mean = dataFrame.mean(axis=0, skipna=True)
        return df_mean

    def calculate_median(self, dataFrame, columns=None):
        df_median = dataFrame.median(axis=0, skipna=True)
        return df_median

    def calculate_mode(self, dataFrame, columns=None):
        df_mode = dataFrame.mode(axis=0, skipna=True)
        return df_mode

    def convert_time_interval(self, dataFrame, column='PCT1402-01:timeInterval:fbk'):  # set default to all time intervals?
        # problem not converting any currently for master (probably because when/if called for master no column is given)
        if not column in dataFrame.columns:
            return
        
        for i in range(len(dataFrame.loc[:, column])):
            if str(dataFrame.loc[i, column]) != 'nan':
                offset_time = datetime.datetime(1900, 1, 1)
                if 'min' in dataFrame.loc[i, column]:
                    if 'sec' in dataFrame.loc[i, column]:
                        input_time = pd.to_datetime(dataFrame.loc[i, column].strip(), format='%M min %S sec')
                        delta = input_time - offset_time
                        dataFrame.loc[i, column] = delta.total_seconds()
                    else:
                        input_time = pd.to_datetime(dataFrame.loc[i, column].strip(), format='%M min')
                        delta = input_time - offset_time
                        dataFrame.loc[i, column] = delta.total_seconds()
                else:
                    input_time = pd.to_datetime(dataFrame.loc[i, column].strip(), format='%S sec')
                    delta = input_time - offset_time
                    dataFrame.loc[i, column] = delta.total_seconds()
            else:
                float(dataFrame.loc[i, column])
        dataFrame[column] = dataFrame[column].astype(float)
        return dataFrame

    def drop_na_values(self, dataframe, axis=0):
            dataframe.dropna(axis=axis, inplace=True)

    def fill_column_values(self, dataFrame, fillValues):
        for column in dataFrame.columns[1:]:
            fill_value = fillValues[column]
            dataFrame.fillna(fill_value, axis="rows", inplace=True)

    def fill_na_values(self, method="pad"):
        selectedDataFrames = self.selectedDataFrames.values()
        if type(method) == int or type(method) == float:
            for dataframe in selectedDataFrames:
                dataframe.fillna(method, axis='rows',
                                      inplace=True)  # Has been initially tested and is working at the moment
        elif method in ['mean', 'median', 'mode']:
            if method == 'mean':
                for dataframe in selectedDataFrames:
                    fill_values = dataframe.mean(axis=0, skipna=True)
                    self.fill_column_values(dataframe, fill_values)
            if method == 'median':  # Has been initially tested and is working at the moment
                for dataframe in selectedDataFrames:
                    fill_values = dataframe.median(axis=0, skipna=True)
                    self.fill_column_values(dataframe, fill_values)
            elif method == 'mode':
                for dataframe in selectedDataFrames:
                    fill_values = dataframe.mode(axis=0, skipna=True)
                    self.fill_column_values(dataframe, fill_values)
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

    def interpolate_data(self, dataFrame, method='polynomial', order=1):
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

    def calculate_correlation(self, dataframe, check_list=None):
        position = 0
        if check_list is None:
            for column in dataframe.columns:
                check_list[position] = column
        print('done checklist')
        # for PV in check_list:

    def calculate_correlation_matrix(self, dataframe):
        self.prepare_dataframe_for_correlating()
        self.correlation_matrix = dataframe.corr()  # calculates the pair-wise correlation values between all the columns within a dataframe
    
    def prepare_dataframe_for_correlating(self, dataframe):
        # need to convert time values before interpolating (possibly when dataframe is created?)
        self.convert_timestamp_to_datetime(dataframe)
        self.convert_time_interval(dataframe)  # ?
        # should interpolate data first so fewer na values
        self.interpolate_data(dataframe)
        # should remove na values remaining after interpolation to not throw off correlation calculation
        self.drop_na_values(dataframe)  # or fill_na
        # switch all function calls to modify ones - should be able to comment out everything above and uncomment the two lines below
        # self.modify_dataframe(method='interpolate', order=2)
        # self.modify_dataframe(method='drop')
        # drop all columns with a std of 0
        column_stds = dataframe.std()
        for i in range(len(column_stds)):
            if column_stds[i] == 0:
                dataframe = dataframe.drop(dataframe.columns[[i + 1]], axis=1)
'''
   
    # def select_dataframe_column(self, dataframe='master_dataframe', column=None):

    def set_dataframe_as_master(self):
        dataFrame = copy.deepcopy(self.master_dataframe)
        
            # JUST STARTING TO WRITE


   

    # check time conversion and na fills and columns
    
            '''

dataframe_manager = DataFrameManager()
