import glob
import copy
import pandas as pd
import functools
import matplotlib.pyplot as plt
import time
from epics import caget, PV
import datetime
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from tabulate import tabulate


# ADD CATCH STATEMENTS TO ALL IF ELSE STATEMENTS

# create list of dictionaries of files
# each dictionary has a file_name, raw_data, and data_frame
# [{file_name: 'example.ext', dataframe: {}]



class CSVList:  # Rename to DataManager
    def __init__(self, csv_files):
        self.list_of_file_names = copy.deepcopy(csv_files)  # possibly switch deep copies once type check is set up
        self.csv_files = copy.deepcopy(csv_files)
        self.list_of_csv_dataframes = []
        self.dataframe = pd.DataFrame()  # Working dataframe
        self.dataframe_file_name = None
        self.list_of_file_dataframes = []  # List of current dataframes from each file
        self.dataframe_list_position = 0
        self.file_dictionary = {} # Currently selected file
        self.list_of_file_dictionaries = []  # List of dictionaries for each file
        self.file_list_position = 0
        self.list_of_original_dataframes = []
        self.original_master_dataframe = pd.DataFrame()  # Concatenated all original Dataframes
        self.master_dataframe = pd.DataFrame()  # Concatenated all Dataframes
        self.master_dataframe_dictionary = {
            "file_name": "master_dataframe",
            "original_dataframe": self.original_master_dataframe,
            "modified_dataframe": self.master_dataframe,
            "modification_history": None
        }
        #self.original_data = {}  # create dictionary to store original data in before fill or editing
        self.correlation_matrix = pd.DataFrame
        self.correlation_pairs_list = []

        self.load_csv_file()
        #self.add_csv()


    def __add_csv_to_dataframe(self, csv):  # original function used before reformating
        # change to convert csv to dataframe and store in dictionary
        data_frame = pd.read_csv(csv)
        #self.dataframe_list.append(data_frame)
        #self.original_data[csv] = data_frame
        data_frame["Timestamp"] = data_frame["Timestamp"].apply(pd.to_datetime)
        if len(self.dataframe.columns.to_list()) == 0:
            self.dataframe = data_frame
        else:
            self.dataframe = pd.merge(self.dataframe, data_frame, how="outer", on=['Timestamp'])  # USES MERGE INSTEAD OF CONCAT

    # Read Multiple CSV Files from a Folder
    # https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/

    #Add files
    #def add_file(self):


    # input file name(s) to add
    # add file names to list
    # go through list
    #   check file type
    #   save in according places for type
    #   create dictionary entry for each file
    #       store file name
    #       convert file to dataframe
    #       save original dataframe in dictionary
    #   store dictionary entry in list
    # create master dataframe from list


    # file type detection
    # https://stackoverflow.com/questions/54698130/determine-if-a-file-is-more-likely-json-or-csv

    # add check for if file has already been added

    def load_csv_file(self):
        for csv in self.csv_files:
            self.add_csv_to_dictionary(csv)  # new
            # self.__add_csv_to_dataframe(csv)  # old

    # modify to add in multiple csv files at a time
    # instead of modifying this function create which adds all in the list
    def add_csv(self, csv):
        # check if one or more csv files passed in
        # if more than one file loop through all
        # add each one as follows still
        self.list_of_file_names.append(csv)  # should be in but add again because initalized since missing type check
        self.csv_files.append(csv)
        self.add_csv_to_dictionary(csv)
        # self.csv_files.append(csv)
        # self.__add_csv_to_dataframe(csv)

    def add_csv_to_dictionary(self, csv):
        # https://www.educative.io/answers/how-to-create-a-dictionary-of-data-frames-in-python
        dataframe_info = {
            "file_name": csv,
            "file_type": "csv",
            # add and check "list_of_column_names": self.get_column_names(),
            "original_dataframe": self.csv_to_df(csv),
            "modified_dataframe": None,
            "modification_history": None
        }
        #self.__add_csv_to_dataframe(csv)  # old
        self.list_of_file_dictionaries.append(dataframe_info)

    def csv_to_df(self, csv):
        data_frame = pd.read_csv(csv)
        data_frame["Timestamp"] = data_frame["Timestamp"].apply(pd.to_datetime)
        self.list_of_original_dataframes.append(data_frame)
        self.list_of_csv_dataframes.append(data_frame)
        self.list_of_file_dataframes.append(data_frame)
        self.construct_master_dataframe_dictionary()
        return data_frame


    #def add_txt(self, txt):
    #copy from experiment.py file

    #def add_json(self, json):
    #copy from ecperiment sample_read_json_file

    # Read Multiple CSV Files from a Folder
    # https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/
    #def add_CSV_files_from_folder(self, path=None):

    #def add_txt_files_from_folder(self, path=None):
    #def add_json_files_from_folder(self, path=None):
    #def add_files_from_folder(self, path=None):


    def construct_original_master_dataframe(self):
        if len(self.original_master_dataframe.columns.to_list()) == 0:
            self.original_master_dataframe = self.dataframe
        else:
            # 4. Assigning Keys to the Concatenated DataFrame Indexes to distinguish each individual dataframe from list within master
            # https://www.digitalocean.com/community/tutorials/pandas-concat-examples
            self.original_master_dataframe = pd.concat(self.list_of_original_dataframes, ignore_index=True, sort=False)

    def construct_modified_master_dataframe(self):
        if len(self.master_dataframe.columns.to_list()) == 0:
            self.master_dataframe = self.dataframe
        else:
            # 4. Assigning Keys to the Concatenated DataFrame Indexes to distinguish each individual dataframe from list within master
            # https://www.digitalocean.com/community/tutorials/pandas-concat-examples
            self.master_dataframe = pd.concat(self.list_of_file_dataframes, ignore_index=True, sort=False)

    # Construct master dataframe from list of modified (or original if no modified) dataframes
    def construct_master_dataframe_dictionary(self):
        self.construct_original_master_dataframe()
        self.construct_modified_master_dataframe()
        self.master_dataframe_dictionary["original_dataframe"] = self.original_master_dataframe
        self.master_dataframe_dictionary["modified_dataframe"] = self.master_dataframe

    def select_file_dictionary(self, file_name):
        file_found = False
        while file_found is not True:
            if self.list_of_file_dictionaries[self.file_list_position]['file_name'] == file_name:
                file_found = True
                self.file_dictionary = self.list_of_file_dictionaries[self.file_list_position]
            else:
                self.file_list_position += 1

    def select_dataframe(self, dataframe_name='master_dataframe', original=False):
        dataframe_found = False
        while dataframe_found is not True:
            if self.list_of_file_dictionaries[self.dataframe_list_position]['file_name'] == dataframe_name:
                dataframe_found = True
                if original != True and self.list_of_file_dictionaries[self.dataframe_list_position]['modified_dataframe'] is not None:
                    self.dataframe = self.list_of_file_dictionaries[self.dataframe_list_position]['modified_dataframe'] # maybe deep copy to save versions later
                else:
                    self.dataframe = copy.deepcopy(self.list_of_file_dictionaries[self.dataframe_list_position]['original_dataframe'])
                self.dataframe_file_name = dataframe_name
            else:
                self.dataframe_list_position += 1

    def unselect_dataframe(self):
        if self.dataframe is not None:
            #possibly save current file before so that can reload it after if different
            self.select_file_dictionary()

    def modify_dataframe(self, dataframe=None, dataframe_name='master_dataframe', version='modified', method=None):
        #set dataframe version
        if version == 'modified':
            original = False
        else:
            original = True
        #select dataframe to modify if n
        if dataframe is None:
            self.select_dataframe(dataframe_name, original)
        else:

        #eventually save all versions into a list of dictionaries containing the modified dataframe and modification history



    #def select_dataframe_column(self, dataframe='master_dataframe', column=None):
    #return dataframe_column

    def set_dataframe_as_master(self):
        self.dataframe = copy.deepcopy(self.master_dataframe)

    def output_csv_list(self):
        for csv in range(len(self.csv_files)):
            print(self.csv_files[csv])
        #test print(self.csv_files)?

    def sort_by_column(self, columns):
        self.dataframe.sort_values(columns)

    def get_column_names(self):
        return self.dataframe.columns.to_list()

    def get_column_values(self, column):
        return self.dataframe.loc[:, column]

    def output_dataframe_to_console(self):
        print(tabulate(self.dataframe[1:50], headers='keys', tablefmt='rst'))

    def print_columns(self, column_list=None):
        if column_list is None:
            column_list = self.dataframe.columns
        for column in column_list:
            print(self.dataframe[column])
            print('\n')


    #def remove_columns(self, columns_to_remove):
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

    def convert_time_interval(self, column=None):
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

    def drop_na_values(self):
        self.dataframe.dropna(axis='rows', inplace=True)

    # NOT ALL HAVE CURRENTLY PASSED WORKING TEST
    def fill_na_values(self, method='pad'):
        if type(method) == int or type(method) == float:
            self.dataframe.fillna(method, axis='rows', inplace=True)  # Has been initially tested and is working at the moment
        elif method in ['mean', 'median', 'mode']:
            if method == 'mean':
                column_fill_values = self.calculate_mean()
            if method == 'median':  # Has been initially tested and is working at the moment
                column_fill_values = self.calculate_median()
            elif method == 'mode':
                column_fill_values = self.calculate_mode()
            for column in self.dataframe.columns[1:]:
                fill_value = column_fill_values[column]
                self.dataframe[column].fillna(fill_value, axis='rows', inplace=True)
        elif method in ['backfill', 'bfill', 'ffill', 'pad']:
            if method == 'backfill':
                self.dataframe.fillna(method='backfill', inplace=True)
            if method == 'bfill':
                self.dataframe.fillna(method='bfill', inplace=True)
            if method == 'ffill':
                self.dataframe.fillna(method='ffill', inplace=True)
            if method == 'pad':  # Has been initially tested and is working at the moment
                self.dataframe.fillna(method='pad', inplace=True)
        # Add catch statement/check default


    def interpolate_data(self, method='polynomial', order=5):  # Check default works without options
        # Could try using match case instead of if-else statements
        # https://learnpython.com/blog/python-match-case-statement/
        # Check method is a valid option
        if order is None:
            if method == 'linear':
                self.dataframe.interpolate(method='linear', inplace=True)
        elif method == 'polynomial':
            # typecheck order is int
            if str(order) == '1':
                self.dataframe.interpolate(method='polynomial', order=1, inplace=True)
            elif str(order) == '2':
                self.dataframe.interpolate(method='polynomial', order=2, inplace=True)
            elif str(order) == '3':
                self.dataframe.interpolate(method='polynomial', order=3, inplace=True)
            elif str(order) == '4':
                self.dataframe.interpolate(method='polynomial', order=4, inplace=True)
            elif str(order) == '5':
                self.dataframe.interpolate(method='polynomial', order=5, inplace=True)
            # add catch for negative/fractional/higher orders entered

    # JUST STARTING TO WRITE
    # HAS NOT BEEN CHECKED YET
    def calculate_correlation(self, check_list=None):
        position = 0
        if check_list is None:
            for column in self.dataframe.columns:
                check_list[position] = column
        print('done checklist')
        #for PV in check_list:

    def calculate_correlation_matrix(self):
        # should interpolate data first so fewer na values
        self.interpolate_data()
        # should remove na values remaining after interpolation so as to not throw off correlation calculation
        self.drop_na_values()
        # drop all columns with a std of 0
        column_stds = self.dataframe.std()
        for i in range(len(column_stds)):
            if column_stds[i] == 0:
                self.dataframe = self.dataframe.drop(self.dataframe.columns[[i+1]], axis=1) # +! to account for no timestamp std
        self.correlation_matrix = self.dataframe.corr() #calculates the pair-wise correlation values between all the columns within a dataframe


    def output_correlation_matrix(self):
        for PV in self.correlation_matrix:
            print(PV)

    #add FFT function?

    #frequency map analysis experiment txt page 24

    #include plotting helper functions? Or filvcl in DataPlotter class?







