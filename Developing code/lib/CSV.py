import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from tabulate import tabulate

class CSVList:
    def __init__(self, csv_files):
        self.csv_files = csv_files
        self.dataframe = pd.DataFrame()
        self.read_csv()

    def read_csv(self):
        for csv in self.csv_files:
            self.__add_csv_to_dataframe(csv)

    def __add_csv_to_dataframe(self, csv):
        data_frame = pd.read_csv(csv)
        data_frame["Timestamp"] = data_frame["Timestamp"].apply(pd.to_datetime)
        if len(self.dataframe.columns.to_list()) == 0:
            self.dataframe = data_frame
        else:
            self.dataframe = pd.merge(self.dataframe, data_frame, how="outer", on=['Timestamp'])

    # modify to add in multiple csv files at a time
    def add_csv(self, csv):
        # check if one or more csv files passed in
        # if more than one file loop through all
        # add each one as follows still
        self.csv_files.append(csv)
        self.__add_csv_to_dataframe(csv)

    #def add_txt(self, tct):
        #copy from experiment.py file

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

    #def calculate_mean(self, columns=None):

    #def calculate_median(self, columns=None):

    #def calculate_mode(self, columns=None):

    def drop_na_values(self):
        self.dataframe.dropna(axis='rows', inplace=True)

    # HAVE NOT CURRENTLY PASSED WORKING TEST
    def fill_na_values(self, method):
        print(type(method))
        if type(method) == int or type(method) == float:
            self.dataframe.fillna(method, axis='rows', inplace=True)
        elif method in ['mean', 'median', 'mode']:
            if method == 'median':
                df_median = self.dataframe.median(axis=0, skipna=True)
            for column in self.dataframe.columns[1:]:
                #method_function = getattr(self.dataframe.columns[column], method)
                fill_value = df_median[column]
                #fill_value = method_function()
                # fill_value = self.dataframe.columns[column].method  # Check if method after . is string
                self.dataframe[column].fillna(fill_value, axis='rows', inplace=True)
        else:
            # Test with backfill, bfill, ffill, and pad
            self.dataframe.fillna(method=method)    # Check if dataframe needs to equal this

    # HAS NOT BEEN CHECKED YET
    def interpolate_data(self, method='polynomial', order=None):
        self.dataframe = self.dataframe.interpolate(method='polynomial', order=1)
        self.dataframe = self.dataframe.fillna(0)

    #JUST STARTING TO WRITE
    def calculate_correlation(self, check_list=None):
        position = 0
        if check_list is None:
            for column in self.dataframe.columns:
                check_list[position] = column
        #for PV in check_list:

    def calculate_correlation_matrix(self):
        return self.dataframe.corr() #calculates the pair-wise correlation values between all the columns within a dataframe

    def output_correlation_matrix(self):
        correlation_matrix = self.calculate_correlation_matrix()
        for PV in correlation_matrix:
            print(PV)


    #include plotting helper functions? Or fill in DataPlotter class?
    






