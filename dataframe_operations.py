import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show, output_file
from web_api.connect_api import ConnectToApi, WeatherApi
from tkinter import Tk
from tkinter.filedialog import askopenfilename

"""A class which has only one scope: open the .csv file and set-up to parameters in order to sort data"""


class DataInput:
    def __init__(self):
        Tk().withdraw()
        filename = askopenfilename()
        self.PATH = filename
        self.df = pd.read_csv(self.PATH)
        self.rank1 = 30
        self.rank2 = 15


"""A class which will perform different actions on a dataframe generated by a web api-csv file-work in progress 
here... """


class DataOperations(DataInput):
    def __init__(self):
        super(DataOperations, self).__init__()

    # GENERAL INFO ABOUT THE DATAFRAME

    # Brief info on the DataFrame
    def dataframe_info(self):
        df_head = self.df.head()
        df_description = self.df.describe()
        print(df_head)
        print(df_description)

    # SEARCH AND GENERAL  OPERATIONS ON THE DATAFRAME

    # Finds and shows the values from a specific column (user input)
    def find_column_values(self):
        try:
            ui_col1 = input("Enter column name:")
            df_col = self.df[ui_col1]
            df_col_save = pd.DataFrame(df_col)
            print(df_col_save)
            return df_col_save
        except ValueError:
            print("Please enter a valid input")

    # Finds and shows a specific value from a column (user input)
    def find_row_values(self):
        try:
            search_column = input("Column name : ")
            row_search = input("Looking for ?  :")
            if row_search.isdigit():
                df_row = self.df.loc[self.df[search_column] == int(row_search)]
                df_row_save = pd.DataFrame(df_row)
                print(df_row_save)
            else:
                df_row = self.df.loc[self.df[search_column] == row_search]
                df_row_save = pd.DataFrame(df_row)
                print(df_row_save)
            return df_row_save
        except ValueError:
            print("Invalid Input, please try again! ")

    def rename_column(self):
        col_old_name = str(input("Old column name:"))
        col_new_name = str(input("New column name:"))
        dict_col = {col_old_name: col_new_name}
        temp = self.df.rename(columns=dict_col)
        df_renamed = pd.DataFrame(temp)
        print(df_renamed)
        return df_renamed

    # ANALYZE AND REFACTOR  THE  DATAFRAME

    # Adds new column with data from other columns based on a user choice criteria (user input)
    def add_new_column_and_sort(self):
        try:
            ui_col_loc = int(input("On which position you want to add the new column? :"))
            ui_new_col_name = str(input("Name of new column: "))
            ui_content = ""
            self.df.insert(ui_col_loc, ui_new_col_name, ui_content, False)

            old_column = input("In which column is the referring data?:")
            sort_value = int(input("Sort criteria ( must be a  number) :"))
            self.df.loc[self.df[old_column] >= sort_value, ui_new_col_name] = self.rank1
            self.df.loc[self.df[old_column] < sort_value, ui_new_col_name] = self.rank2
            print(self.df.head())
            return self.df
        except ValueError:
            print("Invalid input, please try again! ")

    # Filters the data from a column  based on min and max values(user input)
    def filter_data(self):
        try:
            col_name = input("Enter the column name :")
            min_len_df = self.df[col_name].min()
            max_len_df = self.df[col_name].max()

            print(f"Choose a min and max value between  {min_len_df} and {max_len_df}")
            ui_min_val = int(input("Minimum value:"))
            ui_max_val = int(input("Maximum value:"))
            df_len = self.df[(self.df[col_name] >= ui_min_val) & (self.df[col_name] <= ui_max_val)]

            show_df = pd.DataFrame(df_len)
            print(show_df)
            return show_df
        except ValueError:
            print("Invalid input, please try again!")

    # Makes new column to sum up the values from different columns(user input)
    def sum_up_columns(self):
        try:
            sum_col_lst = []
            ui_col_loc = int(input("On which position you want to add the  new column? :"))
            col_to_add = str(input("Name of the column where you want to store results:"))
            ui_content = ""
            self.df.insert(ui_col_loc, col_to_add, ui_content, False)

            print("How many columns do you want to sum ( max number is 3) ?:")
            ui_answer = int(input())
            match ui_answer:
                case 2:
                    col_1 = str(input("Enter name of column:"))
                    col_2 = str(input("Enter name of column:"))
                    sum_col_lst.append(col_1)
                    sum_col_lst.append(col_2)
                    df_col_added = self.df[col_to_add] = self.df[sum_col_lst].sum(axis=1)
                    df_sum = pd.DataFrame(df_col_added)
                    return df_sum
                case 3:
                    col_1 = str(input("Enter name of column:"))
                    col_2 = str(input("Enter name of column:"))
                    col_3 = str(input("Enter name of column:"))
                    sum_col_lst.append(col_1)
                    sum_col_lst.append(col_2)
                    sum_col_lst.append(col_3)
                    df_col_added = self.df[col_to_add] = self.df[sum_col_lst].sum(axis=1)
                    df_sum = pd.DataFrame(df_col_added)
                    return df_sum
        except ValueError:
            print("Invalid input, please try again!")

        # Split columns where values from it are a list

    def split_column_data(self):
        col_name = str(input("Enter column name to be split:"))
        separator = str(input("Separated by ? : "))
        temp = self.df[col_name].str.split(separator, expand=True)
        df_split = pd.DataFrame(temp)
        print(type(df_split))
        print(df_split)
        return df_split

    # Select a range of columns from DF( e.g. from column 0 to column 10)
    def select_range_of_columns(self):
        name_first_col = str(input("Enter first column name:"))
        name_last_col = str(input("Enter last column name:"))
        temp = self.df.loc[:, name_first_col:name_last_col]
        df_selected = pd.DataFrame(temp)
        return df_selected

    def replace_all_values_in_row(self):
        num_row = int(input("Which row you want all the values to be  replaced? : "))
        new_value = input("Enter the new value :")
        temp = self.df.loc[num_row] = new_value
        df_replaced_row = pd.DataFrame(temp)
        return df_replaced_row

    def transpose_df(self):
        temp = self.df.transpose()
        df_transposed = pd.DataFrame(temp)
        return df_transposed

    # CONVERT THE VALUES FROM A COLUMN
    def str_to_float(self):
        col_to_float = str(input("Enter the column name you want the values to be converted to a float"))
        temp = self.df[col_to_float] = self.df[col_to_float].astype(float)
        df_col_float = pd.DataFrame(temp)
        return df_col_float

    def str_to_int(self):

        col_to_int = str(input("Enter the column name you want the values to be converted to an int"))
        temp = self.df[col_to_int] = self.df[col_to_int].astype(int)
        df_col_int = pd.DataFrame(temp)
        return df_col_int

    def int_to_float(self):
        col_to_float = str(input("Enter the column name you want the values to be converted to a float"))
        temp = self.df[col_to_float] = self.df[col_to_float].astype(float)
        df_col_float = pd.DataFrame(temp)
        return df_col_float

    def float_to_int(self):
        col_to_int = str(input("Enter the column name you want the values to be converted to an int"))
        temp = self.df[col_to_int] = self.df[col_to_int].astype(int)
        df_col_int = pd.DataFrame(temp)
        return df_col_int

        # GRAPHICAL VISUALIZATION OF THE DATAFRAME

    def visualize_data(self):
        try:
            x_col = input("Enter X column name:")
            x = self.df[x_col]
            y_col = input("Enter Y column name:")
            y = self.df[y_col]
            p = figure(title="Temperature for 2022-11-03", x_axis_label=x_col, y_axis_label=y_col)
            p.scatter(x, y, line_width=2)
            output_file("Test.html")
            show(p)
        except ValueError:
            print("Invalid input, please try again!")


do = DataOperations()
ds = DataInput()
weather_api = WeatherApi()
connect = ConnectToApi()
