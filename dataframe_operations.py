import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show, output_file

"""A class which has only one scope: open the .csv file and set-up to arguments in order to sort data"""


class DataSorting:
    def __init__(self):
        self.PATH = "D:\\PROGRAMARE\\PORTOFOLIO\\PandasDataFrame\\input_data\\players_fifa23.csv"
        self.df = pd.read_csv(self.PATH)
        self.rank1 = 30
        self.rank2 = 15


"""A class which allows user to perform different operations on the DataFrame  """


class DataOperations(DataSorting):
    def __init__(self):
        super(DataOperations, self).__init__()

    # Brief info of the DataFrame
    def dataframe_info(self):
        df_head = self.df.head()
        df_description = self.df.describe()
        print(df_head)
        print(df_description)

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

    # Find and shows a specific value from a column (user input)
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

    # Adds new columns and sort values from different columns (user input)
    def add_new_columns_and_sort(self):
        try:
            ui_col_loc = int(input("On which position you want to add the column? :"))
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

    # Filter the data from a column  based on min and max values(user input)
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

    # Make new column to sum up the values from different columns(user input)
    def sum_up_columns(self):
        try:
            sum_col_lst = []
            ui_col_loc = int(input("On which position you want to add the column? :"))
            col_to_add = str(input("Name of the column where you want to store results:"))
            ui_content = ""
            self.df.insert(ui_col_loc, col_to_add, ui_content, False)

            print("How many columns do you want to sum?:")
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

    def visualize_data(self):
        try:
            x_col = input("Enter X column name:")
            x = self.df[x_col]
            y_col = input("Enter Y column name:")
            y = self.df[y_col]
            p = figure(title="Example title", x_axis_label=x_col, y_axis_label=y_col)
            p.circle(x, y, line_width=2)
            output_file("Test.html")
            show(p)
        except ValueError:
            print("Invalid input, please try again!")


do = DataOperations()
ds = DataSorting()
