import pandas as pd
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

    def add_csv(self, csv):
        self.csv_files.append(csv)
        self.__add_csv_to_dataframe(csv)

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

# HAVE NOT CURRENTLY PASSED WORKING TEST
    def drop_na_values(self):
        self.dataframe.dropna(axis='columns')
        #for column in self.dataframe:
        #    self.dataframe[column] = self.dataframe[column].dropna()

    def fill_na_values(self, method):
        print(type(method))
        if type(method) == int or type(method) == float:
            self.dataframe.fillna(method)
        elif method in ['mean', 'median', 'mode']:
            for column in self.dataframe.columns[1:]:
                method_function = getattr(self.dataframe.columns[column], method)
                fill_value = method_function()
                # fill_value = self.dataframe.columns[column].method  # Check if method after . is string
                self.dataframe[column] = self.dataframe[column].fillna(fill_value)
        else:
            # Test with backfill, bfill, ffill, and pad
            self.dataframe.fillna(method=method)    # Check if dataframe needs to equal this

    # HAS NOT BEEN CHECKED YET
    def interpolate_data(self, method='polynomial', order=None):
        self.dataframe = self.dataframe.interpolate(method='polynomial', order=1)
        self.dataframe = self.dataframe.fillna(0)

    #JUST STARTING TO WRITE
    # df.corr() calculates the pair-wise correlation values between all the columns within a dataframe
    def calculate_correlation(self, check_list=None):
        position = 0
        if check_list is None:
            for column in self.dataframe.columns:
                check_list[position] = column
        #for PV in check_list:









