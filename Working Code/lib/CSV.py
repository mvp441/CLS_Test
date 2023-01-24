import pandas as pd
from tabulate import tabulate

class CSVList:
    def __init__(self, csv_files):
        self.csv_files = csv_files
        self.dataframe = pd.DataFrame()
        self.read_csvs()


    def read_csvs(self):
        for csv in self.csv_files:
            self.__add_csv_to_dataframe(csv)

    def __add_csv_to_dataframe(self, csv):
        data_frame = pd.read_csv(csv);
        data_frame["Timestamp"] = data_frame["Timestamp"].apply(pd.to_datetime)

        if len(self.dataframe.columns.to_list()) == 0:
            self.dataframe = data_frame
        else:
            self.dataframe = pd.merge(self.dataframe, data_frame, how="outer", on=['Timestamp'])
    def sort_by_column(self, columns):
        self.dataframe.sort_values(columns)

    def add_csv(self, csv):
        self.csv_files.append(csv)
        self.__add_csv_to_dataframe(csv)


    def get_column_names(self):
        return self.dataframe.columns.to_list()

    def interpolate_data(self, method='polynomial', order=None):
        self.dataframe = self.dataframe.interpolate(method='polynomial', order=1)
        self.dataframe = self.dataframe.fillna(0)

    def get_column_values(self, column):
        return self.dataframe.loc[:, column]

    def output_dataframe_to_console(self):
        print(tabulate(self.dataframe[1:50], headers='keys', tablefmt='rst'))




