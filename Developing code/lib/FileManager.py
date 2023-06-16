import CsvManager, JsonManager, DataStorage
import copy
import pandas as pd

# https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
# https://pypi.org/project/singleton-decorator/?fbclid=IwAR0vUAXsSFI6G1el2EgjEQip7tdG3V29rnkCc0QhW6W8zNcBjoasu-zbZ6U

# file type managers are subclasses with shared parent variables
class FileManager:
    def __init__(self):
        data_store = DataStorage
        csv_data = CsvManager
        json_data = JsonManager

    # has functions for importing data into dataframes

    #def add_file()
        #if csv:
            #use CsvManager to add file to data store
            #csv_data.add_csv  # need to fix return so datastore object in file manager changes


