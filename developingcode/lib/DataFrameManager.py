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

    '''    
    def convert_csv_timestamp(self):
        self.dataframe['Timestamp'] = self.dataframe['Timestamp'].apply(pd.to_datetime)

    def prepare_csv_df(self):
        self.modify_dataframe(method='convert_ts', modified=False)
        self.modify_dataframe(method='convert_ti', modified=True)

    # def add_txt(self, txt):
    # copy from experiment.py file or make TxtManager class file?

    # def add_json(self, json):
    # copy from JsonManager class file?

    # Read Multiple CSV Files from a Folder
    # https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/
    # def add_CSV_files_from_folder(self, path=None):

    # def add_txt_files_from_folder(self, path=None):
    # def add_json_files_from_folder(self, path=None):
    # def add_files_from_folder(self, path=None):

    def construct_master_dataframe(self, modified=True):
        # check current status of master dataframe
        if len(self.master_dataframe.columns.to_list()) == 0:
            self.master_dataframe = self.dataframe
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
        
    def sort_by_column(self, columns):
        self.dataframe.sort_values(columns)

    def get_column_names(self):
        return self.dataframe.columns.to_list()

    def get_column_values(self, column):
        return self.dataframe.loc[:, column]

    def output_dataframe_to_console(self):
        # https://pypi.org/project/tabulate/ use -o to save in file
        print(tabulate(self.dataframe, headers='keys', tablefmt='rst'))

    def print_columns(self, column_list=None):
        if column_list is None:
            column_list = self.dataframe.columns
        for column in column_list:
            print(self.dataframe[column])
            print('\n')

    # def remove_columns(self, columns_to_remove):
    # NEED TO DO NEXT BEFORE CORRELATION

    def get_list_description(self):
        dataframe_description = list()
        dataframe_description.append(self.dataframe.describe())
        for column in self.dataframe:
            dataframe_description.append(self.dataframe[column].describe())
        return dataframe_description

    def get_dictionary_description(self):
        dataframe_description = {}
        for column in self.dataframe:
            dataframe_description[column] = self.dataframe[column].describe()
        return dataframe_description

    def convert_time_interval(self, column='PCT1402-01:timeInterval:fbk'):  # set default to all time intervals?
        # problem not converting any currently for master (probably because when/if called for master no column is given)
        for i in range(len(self.dataframe.loc[:, column])):
            if str(self.dataframe.loc[i, column]) != 'nan':
                offset_time = datetime.datetime(1900, 1, 1)
                if 'min' in self.dataframe.loc[i, column]:
                    if 'sec' in self.dataframe.loc[i, column]:
                        input_time = pd.to_datetime(self.dataframe.loc[i, column].strip(), format='%M min %S sec')
                        delta = input_time - offset_time
                        self.dataframe.loc[i, column] = delta.total_seconds()
                    else:
                        input_time = pd.to_datetime(self.dataframe.loc[i, column].strip(), format='%M min')
                        delta = input_time - offset_time
                        self.dataframe.loc[i, column] = delta.total_seconds()
                else:
                    input_time = pd.to_datetime(self.dataframe.loc[i, column].strip(), format='%S sec')
                    delta = input_time - offset_time
                    self.dataframe.loc[i, column] = delta.total_seconds()
            else:
                float(self.dataframe.loc[i, column])
        self.dataframe[column] = self.dataframe[column].astype(float)

    def calculate_mean(self, columns=None):  # keep columns=none?
        df_mean = self.dataframe.mean(axis=0, skipna=True)
        return df_mean

    def calculate_median(self, columns=None):
        df_median = self.dataframe.median(axis=0, skipna=True)
        return df_median

    def calculate_mode(self, columns=None):
        df_mode = self.dataframe.mode(axis=0, skipna=True)
        return df_mode

    # def calculate_percent_change(self):
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html
        '''

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

'''
   def modify_dataframe(self, dataframe=None, dataframe_name=None, modified=False, method='polynomial', order=1):
        dataframe_name = self.dataframe_file_name  # check if correct
        # check if dataframe to modify was specified
        # select dataframe to modify
        if dataframe is None:
            self.select_dataframe(dataframe_name, modified)
        else:
            self.dataframe = dataframe
            self.get_dataframe_file_name()  # doesn't work if list position isn't set from selecting incorrectly
        # get file dataframe is associated with
        self.select_file_dictionary(dataframe_name)
        # check modification method
        if method == 'drop':
            # modify
            self.drop_na_values()
        elif method in ['mean', 'median', 'mode', 'backfill', 'bfill', 'ffill', 'pad']:
            self.fill_na_values(method)
        elif method == 'convert_ts':
            self.convert_csv_timestamp()
        elif method == 'convert_ti':
            self.convert_time_interval()
        else:
            self.interpolate_data(method, order)
        # save modified dataframe
        self.file_dictionary['modified_dataframe'] = copy.deepcopy(self.dataframe)  # might need to deep copy
        # replace dataframe in list
        self.list_of_file_dataframes[self.dataframe_list_position] = self.dataframe
        # test modifying the dataframe after and seeing if both change
        self.file_dictionary['modification_history'].append(method)

        # eventually save all versions into a list of dictionaries containing the modified dataframe and modification history
        
    # def select_dataframe_column(self, dataframe='master_dataframe', column=None):

    def set_dataframe_as_master(self):
        self.dataframe = copy.deepcopy(self.master_dataframe)
        
            # JUST STARTING TO WRITE
    def prepare_dataframe_for_correlating(self):
        # need to convert time values before interpolating (possibly when dataframe is created?)
        self.convert_csv_timestamp()
        self.convert_time_interval()  # ?
        # should interpolate data first so fewer na values
        self.interpolate_data()
        # should remove na values remaining after interpolation to not throw off correlation calculation
        self.drop_na_values()  # or fill_na
        # switch all function calls to modify ones - should be able to comment out everything above and uncomment the two lines below
        # self.modify_dataframe(method='interpolate', order=2)
        # self.modify_dataframe(method='drop')
        # drop all columns with a std of 0
        column_stds = self.dataframe.std()
        for i in range(len(column_stds)):
            if column_stds[i] == 0:
                self.dataframe = self.dataframe.drop(self.dataframe.columns[[i + 1]], axis=1)

    # HAS NOT BEEN CHECKED YET
    def calculate_correlation(self, check_list=None):
        position = 0
        if check_list is None:
            for column in self.dataframe.columns:
                check_list[position] = column
        print('done checklist')
        # for PV in check_list:

    # check time conversion and na fills and columns
    def calculate_correlation_matrix(self):
        # need to convert time values before interpolating (possibly when dataframe is created?)
        self.convert_csv_timestamp()
        # self.convert_time_interval()
        # should interpolate data first so fewer na values
        self.interpolate_data()
        # should remove na values remaining after interpolation so as to not throw off correlation calculation
        self.drop_na_values()
        # drop all columns with a std of 0
        column_stds = self.dataframe.std()
        for i in range(len(column_stds)):
            if column_stds[i] == 0:
                self.dataframe = self.dataframe.drop(self.dataframe.columns[[i + 1]],
                                                     axis=1)  # +! to account for no timestamp std
        # self.prepare_dataframe_for_correlating()
        self.correlation_matrix = self.dataframe.corr()  # calculates the pair-wise correlation values between all the columns within a dataframe
            '''

dataFrameManager = DataFrameManager()
