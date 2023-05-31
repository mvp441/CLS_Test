import glob
import copy
import pandas as pd
from pandas._libs.algos import backfill

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from tabulate import tabulate


# ADD CATCH STATEMENTS TO ALL IF ELSE STATEMENTS

# create list of dictionaries of files
# each dictionary has a file_name, raw_data, and data_frame
# [{file_name: 'example.ext', dataframe: {}]



class CSVList:
    def __init__(self, csv_files):
        self.list_of_file_names = copy.deepcopy(csv_files)  # possibly switch deep copies once type check is set up
        self.csv_files = copy.deepcopy(csv_files)
        self.list_of_csv_dataframes = []
        self.dataframe = pd.DataFrame()  # Working dataframe
        self.dataframe_list = []  # List of dataframes
        self.dataframe_dictionary_list = []  # List of dictionary of dataframes
        self.original_master_dataframe = pd.DataFrame()  # Concatenated all original Dataframes
        self.master_dataframe = pd.DataFrame()  # Concatenated all Dataframes
        #self.original_data = {}  # create dictionary to store original data in before fill or editing

        self.read_csv_file()
        #self.add_csv()


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

    def read_csv_file(self):
        for csv in self.csv_files:
            self.add_csv_to_dictionary(csv)  # new
            #self.__add_csv_to_dataframe(csv)  # old

    def csv_to_df(self, csv):
        data_frame = pd.read_csv(csv)
        data_frame["Timestamp"] = data_frame["Timestamp"].apply(pd.to_datetime)
        self.list_of_csv_dataframes.append(data_frame)
        self.dataframe_list.append(data_frame)
        self.construct_master_dataframe(data_frame)
        return data_frame

    def add_csv_to_dictionary(self, csv):
    # https://www.educative.io/answers/how-to-create-a-dictionary-of-data-frames-in-python
        dataframe_info = {
            "file_name": csv,
            "file_type": "csv",
            "original_dataframe": self.csv_to_df(csv),
            "modified_dataframe": None
        }
        #self.__add_csv_to_dataframe(csv)  # old
        self.dataframe_dictionary_list.append(dataframe_info)

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

    # modify to add in multiple csv files at a time
    # instead of modifying this function create which adds all in the list
    def add_csv(self, csv):
        # check if one or more csv files passed in
        # if more than one file loop through all
        # add each one as follows still
        self.list_of_file_names.append(csv)  # should be in but add again because initalized since missing type check
        self.csv_files.append(csv)
        self.add_csv_to_dictionary(csv)
        #self.csv_files.append(csv)
        #self.__add_csv_to_dataframe(csv)



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


    # Construct master dataframe from list of modified (or original if no modified) dataframes
    def construct_master_dataframe(self, data_frame):
        if len(self.original_master_dataframe.columns.to_list()) == 0:
            self.original_master_dataframe = data_frame
        else:
            # 4. Assigning Keys to the Concatenated DataFrame Indexes
            # https://www.digitalocean.com/community/tutorials/pandas-concat-examples
            self.original_master_dataframe = pd.concat(self.dataframe_list, ignore_index=True, sort=False)

    def select_dataframe(self, data_frame='master_dataframe'):
        print('something')
        #self.dataframe = self.

    def set_dataframe_as_master(self):
        self.dataframe = copy.deepcopy(self.master_dataframe)

    def output_csv_list(self):
        for csv in range(len(self.csv_files)):
            print(self.csv_files[csv])

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
        if order == None:
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
        return self.dataframe.corr() #calculates the pair-wise correlation values between all the columns within a dataframe

    def output_correlation_matrix(self):
        correlation_matrix = self.calculate_correlation_matrix()
        for PV in correlation_matrix:
            print(PV)


    #include plotting helper functions? Or filvcl in DataPlotter class?
    






