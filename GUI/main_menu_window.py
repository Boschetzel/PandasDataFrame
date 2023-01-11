# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'username_taken.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd

from GUI.show_column_data import Ui_df_operations_window
from GUI.show_row_data import Ui_df_operations_window_rows
from GUI.rename_column import Ui_rename_column
from GUI.delete_column import Ui_df_delete_col
from GUI.add_new_column import Ui_add_new_column
from GUI.filter_col_data import Ui_filter_col_data
from GUI.sum_columns import Ui_sum_columns
from GUI.split_col_data import Ui_split_col_data
from GUI.select_multiple_col import Ui_df_select_multiple_col
from GUI.add_new_row import Ui_df_add_new_rows
from GUI.plot_mat import Ui_graph_matplotlib
from GUI.plot_bokeh import Ui_graph_bokeh
from GUI.weather import Ui_weather_info_selenium
from GUI.ml_supevised_gui import Ui_ml_operations

from df_model import PandasModel

import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.io import show, output_file

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

"""This Class contains all the functionalities of the PandasDataFrame Project:
# FILE MENU :
    # OPEN
# DATA OPERATIONS MENU :
    # SHOW DATA HEAD
    # SHOW COLUMN DATA
    # SHOW ROW DATA
    # RENAME COLUMN
    # DELETE COLUMN 
# DATA ANALYSIS MENU :
    # ADD NEW COLUMN
    # FILTER COLUMN
    # SUM UP COLUMNS
    # SPLIT COLUMNS
    # SELECT MULTIPLE COLUMNS 
# DATA VISUALIZATION MENU
    # MATPLOTLIB
    # BOKEH 
# WEATHER INFO MENU
    # THIS WORKS ONLY FOR ROMANIAN CITIES (IF YOU NEED OTHER COUNTRIES YOU MUST CHANGE THE PATH)     
    """


class GuiMainWindow:
    def __init__(self):

        self.df = None
        self.dict_col = {}

    def setupUi(self, MainWindow1):
        # Main window object
        MainWindow1.setObjectName("MainWindow")
        MainWindow1.showMaximized()
        self.central_widget = QtWidgets.QWidget(MainWindow1)
        self.central_widget.setObjectName("centralwidget")

        # TableView Object
        self.main_window_tableView = QtWidgets.QTableView(self.central_widget)
        self.main_window_tableView.setGeometry(QtCore.QRect(190, 120, 1650, 800))
        self.main_window_tableView.setObjectName("main_window_tableView")

        # Title label
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(490, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # MENU BAR ITEMS
        MainWindow1.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDataFrame = QtWidgets.QMenu(self.menubar)
        self.menuDataFrame.setObjectName("menuDataFrame")
        self.menuWeatherApp = QtWidgets.QMenu(self.menubar)
        self.menuWeatherApp.setObjectName("menuWeatherApp")
        self.menuData_Analysis = QtWidgets.QMenu(self.menubar)
        self.menuData_Analysis.setObjectName("menuData_Analysis")
        self.menuVisualize_data = QtWidgets.QMenu(self.menubar)
        self.menuVisualize_data.setObjectName("menuVisualize_data")
        self.menuScikitLearn = QtWidgets.QMenu(self.menubar)
        self.menuScikitLearn.setObjectName("menuScikitLearn")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")

        # MENU BAR ACTION OBJECTS
        # Open CSV file
        MainWindow1.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow1)
        self.actionOpen.setObjectName("actionOpen")

        # Show data from a specific column
        self.actionShow_column_data = QtWidgets.QAction(MainWindow1)
        self.actionShow_column_data.setObjectName("actionShow_column_data")

        # Show data from a specific row
        self.actionShow_row_data = QtWidgets.QAction(MainWindow1)
        self.actionShow_row_data.setObjectName("actionShow_row_data")

        # Rename column
        self.actionRename_column_2 = QtWidgets.QAction(MainWindow1)
        self.actionRename_column_2.setObjectName("actionRename_column_2")

        # Delete column
        self.actionDelete_column = QtWidgets.QAction(MainWindow1)
        self.actionDelete_column.setObjectName("actionDelete_column")

        # Get weather info with Selenium
        self.actionSearch_Weather_Info = QtWidgets.QAction(MainWindow1)
        self.actionSearch_Weather_Info.setObjectName("actionSearch_Weather_Info")

        # Select multiple columns
        self.actionSelect_multiple_columns = QtWidgets.QAction(MainWindow1)
        self.actionSelect_multiple_columns.setObjectName("actionSelect_multiple_columns")

        # Replace values in a row
        self.actionReplace_values_in_row = QtWidgets.QAction(MainWindow1)
        self.actionReplace_values_in_row.setObjectName("actionReplace_values_in_row")

        # Show  DF Head
        self.actionShow_Data_Head = QtWidgets.QAction(MainWindow1)
        self.actionShow_Data_Head.setObjectName("actionShow_Data_Head")

        # Add new column
        self.actionAdd_new_column = QtWidgets.QAction(MainWindow1)
        self.actionAdd_new_column.setObjectName("actionAdd_new_column")

        # Filter data
        self.actionFilter_data_2 = QtWidgets.QAction(MainWindow1)
        self.actionFilter_data_2.setObjectName("actionFilter_data_2")

        # Sum up columns
        self.actionSum_up_columns = QtWidgets.QAction(MainWindow1)
        self.actionSum_up_columns.setObjectName("actionSum_up_columns")

        # Split column data based on a separator
        self.actionSplit_column_data = QtWidgets.QAction(MainWindow1)
        self.actionSplit_column_data.setObjectName("actionSplit_column_data")

        # Select multiple columns
        self.actionSelect_multiple_columns_2 = QtWidgets.QAction(MainWindow1)
        self.actionSelect_multiple_columns_2.setObjectName("actionSelect_multiple_columns_2")

        # Replace all values in a row
        self.actionReplace_all_values_in_row = QtWidgets.QAction(MainWindow1)
        self.actionReplace_all_values_in_row.setObjectName("actionReplace_all_values_in_row")

        # Matplotlib graphs
        self.actionMatPlotLib = QtWidgets.QAction(MainWindow1)
        self.actionMatPlotLib.setObjectName("actionMatPlotLib")

        # Bokeh graphs
        self.actionBokeh = QtWidgets.QAction(MainWindow1)
        self.actionBokeh.setObjectName("actionBokeh")

        # ScikitLearn
        self.actionScikitLearn = QtWidgets.QAction(MainWindow1)
        self.actionScikitLearn.setObjectName("actionScikitLearn")

        # MENU ACTIONS
        self.menuFile.addAction(self.actionOpen)
        self.menuDataFrame.addAction(self.actionShow_Data_Head)
        self.menuDataFrame.addAction(self.actionShow_column_data)
        self.menuDataFrame.addAction(self.actionShow_row_data)
        self.menuDataFrame.addAction(self.actionRename_column_2)
        self.menuDataFrame.addAction(self.actionDelete_column)
        self.menuWeatherApp.addAction(self.actionSearch_Weather_Info)
        self.menuData_Analysis.addAction(self.actionAdd_new_column)
        self.menuData_Analysis.addAction(self.actionFilter_data_2)
        self.menuData_Analysis.addAction(self.actionSum_up_columns)
        self.menuData_Analysis.addAction(self.actionSplit_column_data)
        self.menuData_Analysis.addAction(self.actionSelect_multiple_columns_2)
        self.menuData_Analysis.addAction(self.actionReplace_all_values_in_row)
        self.menuVisualize_data.addAction(self.actionMatPlotLib)
        self.menuVisualize_data.addAction(self.actionBokeh)
        self.menuScikitLearn.addAction(self.actionScikitLearn)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDataFrame.menuAction())
        self.menubar.addAction(self.menuData_Analysis.menuAction())
        self.menubar.addAction(self.menuVisualize_data.menuAction())
        self.menubar.addAction(self.menuWeatherApp.menuAction())
        self.menubar.addAction(self.menuScikitLearn.menuAction())

        # MENU TRIGGERS
        self.actionOpen.triggered.connect(lambda: self.open_df())
        self.actionShow_column_data.triggered.connect(self.show_column_data_window)
        self.actionShow_row_data.triggered.connect(self.show_row_data_window)
        self.actionRename_column_2.triggered.connect(self.show_rename_window)
        self.actionShow_Data_Head.triggered.connect(self.show_df_head)
        self.actionDelete_column.triggered.connect(self.show_delete_col_view)
        self.actionAdd_new_column.triggered.connect(self.show_add_new_column)
        self.actionFilter_data_2.triggered.connect(self.show_filter_col_window)
        self.actionSum_up_columns.triggered.connect(self.show_sum_up_column_window)
        self.actionSplit_column_data.triggered.connect(self.show_split_col_window)
        self.actionSelect_multiple_columns_2.triggered.connect(self.show_select_multiple_col_window)
        self.actionReplace_all_values_in_row.triggered.connect(self.show_add_new_row_window)
        self.actionMatPlotLib.triggered.connect(self.show_matplot_window)
        self.actionBokeh.triggered.connect(self.show_bokeh_plot_window)
        self.actionSearch_Weather_Info.triggered.connect(self.show_weather_info_window)
        self.actionScikitLearn.triggered.connect(self.show_scikit)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    # FILE MENU :
    # OPEN

    # Opens the file dialog and returns the *.csv filepath
    @staticmethod
    def get_csv_filename():
        filename, _ = QFileDialog.getOpenFileName()
        return filename

    # Converts the *.csv file to a Pandas DataFrame and returns the df
    def convert_csv_to_df(self):
        csv_filename = self.get_csv_filename()
        reader = pd.read_csv(csv_filename)
        df = pd.DataFrame(reader)
        self.df = df
        return df

    # Creates a pandas model fo the df and return the model
    def pandas_model(self):
        df = self.convert_csv_to_df()
        model = PandasModel(df)
        return model

    # Opens and show the df in the TableView
    def open_df(self):
        self.main_window_tableView.setModel(self.pandas_model())

    # Cleans the df from nan values (can be used by devs for further development of this project)
    def clean_nan_values(self):
        self.df.fillna(0)
        return self.df

    # Saves the df from the weather info into a *.csv file, I know is hardcoded:)
    def save_df(self):
        df_to_save = pd.DataFrame(self.df)
        df_to_save.to_csv("D:\\PROGRAMARE\\PORTOFOLIO\\PandasDataFrame\\output_data\\sample.csv")

    # DATA OPERATIONS MENU :
    # SHOW DATA HEAD
    # SHOW COLUMN DATA
    # SHOW ROW DATA
    # RENAME COLUMN
    # DELETE COLUMN

    # Method to show the pyQt5 window for displaying a column data
    def show_column_data_window(self):
        self.df_operations_window = QtWidgets.QDialog()
        self.ui = Ui_df_operations_window()
        self.ui.setupUi(self.df_operations_window)
        self.df_operations_window.show()
        self.ui.show_results_btn.clicked.connect(self.get_column_data_values)

    # Method to get the column data from df
    def get_column_data_values(self):
        # Gets the column name from user input
        col_name = self.ui.ui_column_name.text()

        # Rename the column
        df_col = self.df[col_name]

        # Update de df
        df_col1 = pd.DataFrame(df_col)

        # Make a pandas model
        model = PandasModel(df_col1)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)
        return model

    # Method to show the pyQt5 window for displaying a row data
    def show_row_data_window(self):
        self.df_operations_rows_wnd = QtWidgets.QDialog()
        self.ui_row = Ui_df_operations_window_rows()
        self.ui_row.setupUi(self.df_operations_rows_wnd)
        self.df_operations_rows_wnd.show()
        self.ui_row.show_results_btn.clicked.connect(self.get_row_data_values)

    # Method to get the row data from df
    def get_row_data_values(self):
        # Gets the column name from user input
        search_column = self.ui_row.ui_column_name.text()
        row_search = self.ui_row.ui_row_name.text()

        # Check if user input is digit or str
        if row_search.isdigit():
            # Gets the row data from the df(int)
            df_row = self.df.loc[self.df[search_column] == int(row_search)]

            # Update de df with the changes
            df_row_save = pd.DataFrame(df_row)

            # Make a pandas model
            model = PandasModel(df_row_save)

            # Display the updated df in the TableView
            self.main_window_tableView.setModel(model)
        else:
            # Gets the row data from the df(str)
            df_row = self.df.loc[self.df[search_column] == row_search]

            # Update de df with the changes
            df_row_save = pd.DataFrame(df_row)

            # Make a pandas model
            model = PandasModel(df_row_save)

            # Display the updated df in the TableView
            self.main_window_tableView.setModel(model)
        return model

    # Method to show the pyQt5 window to rename a column
    def show_rename_window(self):
        self.rename_col = QtWidgets.QDialog()
        self.ui_rename = Ui_rename_column()
        self.ui_rename.setupUi(self.rename_col)
        self.rename_col.show()
        self.ui_rename.apply_btn.clicked.connect(self.rename_column)

    # Method to rename a column
    def rename_column(self):
        # Creates an empty hash( dict)
        self.dict_col = {}

        # Gets the data from the user input(old col. name, new col name)
        col_old_name = self.ui_rename.ui_old_name.text()
        col_new_name = self.ui_rename.ui_new_name.text()

        # Renames the column
        self.dict_col[col_old_name] = col_new_name
        temp = self.df.rename(columns=self.dict_col, inplace=False)

        # Update de df with the changes
        new_df = pd.DataFrame(temp)

        # Make a pandas model
        model = PandasModel(new_df)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)

    # Method to display the df head in TableView
    def show_df_head(self):
        # Function to get the df head
        df = self.df.head()

        # Update de df with the changes
        df_head = pd.DataFrame(df)

        # Make a pandas model
        model = PandasModel(df_head)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)

    def show_delete_col_view(self):
        self.delete_col = QtWidgets.QDialog()
        self.ui_delete = Ui_df_delete_col()
        self.ui_delete.setupUi(self.delete_col)
        self.delete_col.show()
        self.ui_delete.delete_col_btn.clicked.connect(self.delete_column_data)

    def delete_column_data(self):
        column_to_delete = self.ui_delete.ui_column_name_delete.text()
        temp = self.df.drop(column_to_delete, axis=1, inplace=False)
        new_df = pd.DataFrame(temp)
        model = PandasModel(new_df)
        self.main_window_tableView.setModel(model)

    # DATA ANALYSIS MENU :
    # ADD NEW COLUMN
    # FILTER COLUMN
    # SUM UP COLUMNS
    # SPLIT COLUMNS
    # SELECT MULTIPLE COLUMNS

    # Method to show the pyQt5 window to add a new column
    def show_add_new_column(self):
        self.add_new_column = QtWidgets.QDialog()
        self.ui_add_col = Ui_add_new_column()
        self.ui_add_col.setupUi(self.add_new_column)
        self.add_new_column.show()
        self.ui_add_col.add_col_btn.clicked.connect(self.add_column)

    # Method to add a new column to the df
    def add_column(self):
        # Gets the data from the user input(position of new column, column name, fill data)
        ui_col_loc = int(self.ui_add_col.ui_col_position.text())
        ui_new_col_name = self.ui_add_col.ui_new_col_name.text()
        ui_content = self.ui_add_col.ui_data_fill.text()

        # Inserts the new column into the df
        self.df.insert(ui_col_loc, ui_new_col_name, ui_content)

        # Update de df with the changes
        df = pd.DataFrame(self.df)

        # Make a pandas model
        model = PandasModel(df)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)

        # Can be done like this also :
        # self.df[ui_new_col_name] = pd.DataFrame([ui_content for _ in range(len(self.df.index))])

    # Method to show the pyQt5 window to add a filter a column data
    def show_filter_col_window(self):
        self.filter_col = QtWidgets.QDialog()
        self.ui_filter = Ui_filter_col_data()
        self.ui_filter.setupUi(self.filter_col)
        self.filter_col.show()
        self.ui_filter.filter_btn.clicked.connect(self.filter_col_data)

    # Method to filter a column data based on a min, max value entered by user
    def filter_col_data(self):
        # Fill the nan with "0"
        df = self.df.fillna(0)
        self.df = df

        # Gets the user input(col. name, min val, max val)
        col_name = self.ui_filter.ui_col_name.text()
        ui_min_val = int(self.ui_filter.ui_min_value.text())
        ui_max_val = int(self.ui_filter.ui_max_value.text())

        # Filter the data based on the user input
        self.df[col_name] = self.df[col_name].astype(float)
        temp = self.df[(self.df[col_name] >= ui_min_val) & (self.df[col_name] <= ui_max_val)]

        # Update de df with the changes
        df = pd.DataFrame(temp)

        # Make a pandas model
        model = PandasModel(df)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)

    # Method to show the pyQt5 window to sum up columns
    def show_sum_up_column_window(self):
        self.sum_columns = QtWidgets.QDialog()
        self.ui_sum_col = Ui_sum_columns()
        self.ui_sum_col.setupUi(self.sum_columns)
        self.sum_columns.show()
        self.ui_sum_col.sum_col_btn.clicked.connect(self.sum_columns_up)

    # Method to sum up two columns
    def sum_columns_up(self):
        # Creates an empty list
        sum_col_lst = []

        # Fill nan values with "0"
        self.df.fillna(0)

        # Gets the user input(new column position and name, first col. to be added, second col. to be added)
        ui_col_loc = int(self.ui_sum_col.col_new_position.text())
        col_to_add = str(self.ui_sum_col.new_col_name.text())
        col_1 = str(self.ui_sum_col.first_col_to_sum.text())
        col_2 = str(self.ui_sum_col.second_col_to_sum.text())

        # Inserts new column
        self.df.insert(ui_col_loc, col_to_add, False)

        # Appends data to the list
        sum_col_lst.append(col_1)
        sum_col_lst.append(col_2)

        # Sum up the two columns
        df = self.df[col_to_add] = self.df[sum_col_lst].sum(axis=1)

        # Update de df with the changes
        df_new = pd.DataFrame(df)

        # Make a pandas model
        model = PandasModel(df_new)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)

    # Method to show the pyQt5 window to split column data based on a separator
    def show_split_col_window(self):
        self.df_split = QtWidgets.QDialog()
        self.ui_split = Ui_split_col_data()
        self.ui_split.setupUi(self.df_split)
        self.df_split.show()
        self.ui_split.split_btn.clicked.connect(self.split_col_and_expand)

    # Method to split data on a column based on a separator
    def split_col_and_expand(self):
        # Gets the user input(name of column, separator)
        col_name = str(self.ui_split.ui_column_name.text())
        separator = str(self.ui_split.ui_separator.text())

        # Splits the data
        temp = self.df[col_name].str.split(separator, expand=True)

        # Update de df with the changes
        df_split = pd.DataFrame(temp)

        # Make a pandas model
        model = PandasModel(df_split)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)

    # Method to show the pyQt5 window to select multiple columns
    def show_select_multiple_col_window(self):
        self.df_sel_columns = QtWidgets.QDialog()
        self.ui_select = Ui_df_select_multiple_col()
        self.ui_select.setupUi(self.df_sel_columns)
        self.df_sel_columns.show()
        self.ui_select.select_columns_btn.clicked.connect(self.select_multiple_col)

    # Method to select multiple columns
    def select_multiple_col(self):
        # Gets the user input(name of first column, name of last column)
        name_first_col = str(self.ui_select.ui_first_col_name.text())
        name_last_col = str(self.ui_select.ui_last_col_name.text())

        # Selects the range of columns
        temp = self.df.loc[:, name_first_col:name_last_col]

        # Update de df with the changes
        new_df = pd.DataFrame(temp)

        # Make a pandas model
        model = PandasModel(new_df)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)

    # Method to show the pyQt5 window to add new row
    def show_add_new_row_window(self):
        self.df_replace_values = QtWidgets.QDialog()
        self.ui_replace = Ui_df_add_new_rows()
        self.ui_replace.setupUi(self.df_replace_values)
        self.df_replace_values.show()
        self.ui_replace.replace_btn.clicked.connect(self.add_new_row)

    # Method to add new row
    def add_new_row(self):
        # Gets the user input(row name, value to fill row)
        num_row = self.ui_replace.ui_row_name.text()
        new_value = self.ui_replace.ui_fill_row_value.text()

        # Adds new row and values
        self.df.loc[num_row] = new_value

        # Make a pandas model
        model = PandasModel(self.df)

        # Display the updated df in the TableView
        self.main_window_tableView.setModel(model)

    # DATA VISUALIZATION MENU
    # MATPLOTLIB
    # BOKEH

    # MATPLOTLIB GRAPHS

    # Method to show the pyQt5 window to plot with Matplotlib
    def show_matplot_window(self):
        self.graph_matplotlib = QtWidgets.QDialog()
        self.ui_graph = Ui_graph_matplotlib()
        self.ui_graph.setupUi(self.graph_matplotlib)
        self.graph_matplotlib.show()
        self.ui_graph.simple_plot_btn.clicked.connect(self.plot_simple_graph)
        self.ui_graph.scatter_plot_btn.clicked.connect(self.plot_scatter_graph)
        self.ui_graph.bar_btn.clicked.connect(self.plot_bar_graph)
        self.ui_graph.stem_btn.clicked.connect(self.plot_stem_graph)
        self.ui_graph.step_btn.clicked.connect(self.plot_step_graph)

    # Method to plot data with Matplotlib(simple plot)
    def plot_simple_graph(self):
        plt.style.use('_mpl-gallery')
        # Gets the user input for the two columns to be represented
        x_col = self.ui_graph.ui_X_column.text()
        y_col = self.ui_graph.ui_Y_column.text()

        # Selects the data from columns
        x = self.df[x_col][1:]
        y = self.df[y_col][1:]

        # Plots the data
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)

        # Show the plot
        plt.show()

    # Method to plot data with Matplotlib(scatter plot)
    def plot_scatter_graph(self):
        plt.style.use('_mpl-gallery')
        # Gets the user input for the two columns to be represented
        x_col = self.ui_graph.ui_X_column.text()
        y_col = self.ui_graph.ui_Y_column.text()

        # Selects the data from columns
        x = self.df[x_col][1:]
        y = self.df[y_col][1:]

        # Plots the data
        fig, ax = plt.subplots()
        ax.scatter(x, y)

        # Show the plot
        plt.show()

    # Method to plot data with Matplotlib(bar plot)
    def plot_bar_graph(self):
        plt.style.use('_mpl-gallery')
        # Gets the user input for the two columns to be represented
        x_col = self.ui_graph.ui_X_column.text()
        y_col = self.ui_graph.ui_Y_column.text()

        # Selects the data from columns
        x = self.df[x_col][1:]
        y = self.df[y_col][1:]

        # Plots the data
        fig, ax = plt.subplots()
        ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

        # Show the plot
        plt.show()

    # Method to plot data with Matplotlib(stem plot)
    def plot_stem_graph(self):
        plt.style.use('_mpl-gallery')
        # Gets the user input for the two columns to be represented
        x_col = self.ui_graph.ui_X_column.text()
        y_col = self.ui_graph.ui_Y_column.text()

        # Selects the data from columns
        x = self.df[x_col][1:]
        y = self.df[y_col][1:]

        # Plots the data
        fig, ax = plt.subplots()
        ax.stem(x, y)

        # Show the plot
        plt.show()

    # Method to plot data with Matplotlib(step plot)
    def plot_step_graph(self):
        plt.style.use('_mpl-gallery')
        # Gets the user input for the two columns to be represented
        x_col = self.ui_graph.ui_X_column.text()
        y_col = self.ui_graph.ui_Y_column.text()

        # Selects the data from columns
        x = self.df[x_col][1:]
        y = self.df[y_col][1:]

        # Plots the data
        fig, ax = plt.subplots()
        ax.step(x, y, linewidth=2.5)

        # Show the plot
        plt.show()

    # BOKEH GRAPHS

    # Method to show the pyQt5 window to plot with Bokeh
    def show_bokeh_plot_window(self):
        self.graph_with_bokeh = QtWidgets.QDialog()
        self.ui_bokeh = Ui_graph_bokeh()
        self.ui_bokeh.setupUi(self.graph_with_bokeh)
        self.graph_with_bokeh.show()
        self.ui_bokeh.line_plot_btn.clicked.connect(self.plot_bokeh_line)
        self.ui_bokeh.scatter_plot_btn.clicked.connect(self.plot_bokeh_scatter)
        self.ui_bokeh.bar_btn.clicked.connect(self.plot_bokeh_bar)
        self.ui_bokeh.step_btn.clicked.connect(self.plot_bokeh_step)

    # Method to plot data with Matplotlib(scatter plot)
    def plot_bokeh_scatter(self):
        # Gets the user input for the two columns to be represented
        x_col = self.ui_bokeh.ui_X_column.text()
        x = self.df[x_col][1:]
        y_col = self.ui_bokeh.ui_Y_column.text()

        # Selects the data from columns
        y = self.df[y_col][1:]

        # Plots the data
        p = figure(title="Simple Scatter graph", x_axis_label=x_col, y_axis_label=y_col)
        p.scatter(x, y, line_width=2)

        # Saves the plot in a *.html format
        output_file("Scatter_graph.html")

        # Show the plot
        show(p)

    # Method to plot data with Matplotlib(line  plot)
    def plot_bokeh_line(self):
        # Gets the user input for the two columns to be represented
        x_col = self.ui_bokeh.ui_X_column.text()
        x = self.df[x_col][1:]
        y_col = self.ui_bokeh.ui_Y_column.text()

        # Selects the data from columns
        y = self.df[y_col][1:]

        # Plots the data
        p = figure(title="Simple Line graph", x_axis_label=x_col, y_axis_label=y_col)
        p.line(x, y, line_width=2)

        # Saves the plot in a *.html format
        output_file("Line_graph.html")

        # Show the plot
        show(p)

    # Method to plot data with Matplotlib(step  plot)
    def plot_bokeh_step(self):
        # Gets the user input for the two columns to be represented
        x_col = self.ui_bokeh.ui_X_column.text()
        x = self.df[x_col][1:]
        y_col = self.ui_bokeh.ui_Y_column.text()

        # Selects the data from columns
        y = self.df[y_col][1:]

        # Plots the data
        p = figure(title="Simple Step graph", x_axis_label=x_col, y_axis_label=y_col)
        p.step(x, y, line_width=2, mode="center")

        # Saves the plot in a *.html format
        output_file("Step_graph.html")

        # Show the plot
        show(p)

    # Method to plot data with Matplotlib(bar plot)
    def plot_bokeh_bar(self):
        # Gets the user input for the two columns to be represented
        x_col = self.ui_bokeh.ui_X_column.text()
        x = self.df[x_col][1:]
        y_col = self.ui_bokeh.ui_Y_column.text()

        # Selects the data from columns
        y = self.df[y_col][1:]

        # Plots the data
        p = figure(title="Simple Bar graph", x_axis_label=x_col, y_axis_label=y_col)
        p.vbar(x, top=y, width=0.5, bottom=0, color="firebrick")

        # Saves the plot in a *.html format
        output_file("Bar_graph.html")

        # Show the plot
        show(p)

    # WEATHER INFO MENU
    # THIS WORKS ONLY FOR ROMANIAN CITIES (IF YOU NEED OTHER COUNTRIES YOU MUST CHANGE THE PATH)

    # Method to show the pyQt5 window to search for weather info with Selenium
    def show_weather_info_window(self):
        self.weather_info_selenium = QtWidgets.QDialog()
        self.ui_weather = Ui_weather_info_selenium()
        self.ui_weather.setupUi(self.weather_info_selenium)
        self.weather_info_selenium.show()
        self.ui_weather.save_data_btn.clicked.connect(self.get_weather_info_from_web)

    # Method to get the weather info and save it into a *.csv file
    def get_weather_info_from_web(self):
        # Gets the user input(location)
        city = self.ui_weather.ui_location.text()

        # Set up webdriver
        driver = webdriver.Chrome()

        driver.maximize_window()

        # Gets the url path
        driver.get(f"https://www.accuweather.com/ro/search-locations?query={city}")

        # Creates an empty list to store results
        my_weather_list = []

        # Gets the element and click "Consent" pop-up window
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Consent')]")))

            driver.find_element(By.XPATH, "//p[contains(text(),'Consent')]").click()
        except ValueError:
            print("Something went wrong here ...")

        # Gets the element and click the "DAILY" link
        try:
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "DAILY")))

            driver.find_element(By.LINK_TEXT, "DAILY").click()

        except ValueError:
            print("Something went wrong here ...")

        # Gets the element and store the data into the list
        try:

            results = driver.find_elements(By.CLASS_NAME, "daily-forecast-card ")
            for result in results:
                day = result.find_element(By.XPATH, ".//span[@class='module-header dow date']").text
                date = result.find_element(By.XPATH, ".//span[@class='module-header sub date']").text
                high_temp = result.find_element(By.XPATH, ".//span[@class='high']").text
                low_temp = result.find_element(By.XPATH, ".//span[@class='low']").text
                print(day, date, high_temp, low_temp)  # this is for testing purposes

                # Makes a dict with the gathered results
                results_dict = {"City": city,
                                "Day ": day,
                                "Date": date,
                                "Temp.Max": high_temp,
                                "Low.Temp": low_temp}

                # Appends the data to the list
                my_weather_list.append(results_dict)
        finally:
            # Creates a df from the results
            df = pd.DataFrame(my_weather_list)
            new_df = pd.DataFrame(df)

            # Makes a pandas model
            model = PandasModel(new_df)

            # Display the results in the TableView
            self.main_window_tableView.setModel(model)

            # Close the driver
            driver.quit()

            # Save the results into a *.csv file
            new_df.to_csv("D:\\PROGRAMARE\\PORTOFOLIO\\PandasDataFrame\\output_data\\sample.csv")
            return new_df

    # WORKFLOW FOR SCIKIT LEARN - SUPERVISED LEARNING

    def show_scikit(self):
        self.ml_operations = QtWidgets.QDialog()
        self.ui_ml_op = Ui_ml_operations()
        self.ui_ml_op.setupUi(self.ml_operations)
        self.ml_operations.show()
        self.ui_ml_op.predict_btn.clicked.connect(self.make_predictions)

    def make_predictions(self):
        # 1 Get data and clean it (remove NaN, make numeric columns ...)

        # Fill NaN values with a user choice number
        value_for_nan = self.ui_ml_op.ui_nan_values.text()
        self.df.fillna(value_for_nan)
        print(value_for_nan)
        print(self.df)

        # Drop "String" column by user choice
        col_to_dop = self.ui_ml_op.ui_drop_col.text()
        if col_to_dop == "":
            pass
        else:
            self.df.drop(col_to_dop, axis=1)
            print(f"Column {col_to_dop} dropped")

        # Replace "," with an empty string in all DataFrame
        if self.ui_ml_op.checkBox_2.isChecked():
            self.df.replace(",", "", regex=True).astype(float)
            print("Replaced commas")
        else:
            print("Something went wrong replacing commas")

        # Convert "float" values to "int"
        if self.ui_ml_op.checkBox_4.isChecked():
            self.df.astype(int)
            print("Values converted to int")
        else:
            print("Something went from converting float to int")

        # 2 Set training data (X) - features
        features_col = self.ui_ml_op.ui_features_col.text()
        X = self.df.drop(features_col, axis=1)
        print("Set the training data  - X")

        # 3 Set test data (x) - label
        label_col = self.ui_ml_op.ui_label_col.text()
        y = self.df[label_col]
        print("Set the test data - y")

        # 4 Select the right model  for the problem (classification, Regression, etc)
        if self.ui_ml_op.random_clasifier_chk_box.isChecked():
            model = RandomForestClassifier(n_estimators=30)

        if self.ui_ml_op.random_regr_chk_box.isChecked():
            model = RandomForestRegressor()

        # 5 Fit the data to the model and predict results
        test_size_value = self.ui_ml_op.ui_test_size.text()
        test_size_value_float = float(test_size_value)
        print(test_size_value_float)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_value_float)
        model.fit(X_train, y_train)
        print("Data fit to model")

        # 6 Predict
        predictions = model.predict(X_test)

        # 7 Save prediction to *csv
        csv_filename = self.ui_ml_op.ui_csv_filename.text()
        df_pred = pd.DataFrame(predictions)
        df_pred.to_csv(f"{csv_filename}.csv")
        print("Predictions saved to csv")

        # 8 Evaluate the model (train data, test data) with metrics (accuracy_score, score)
        model_score = model.score(X_test, y_test)
        model_acc = accuracy_score(y_test, predictions)
        self.ui_ml_op.score_lbl.setText(f"The model score is {model_score}")
        self.ui_ml_op.accuracy_lbl.setText(f"The model accuracy is  is {model_acc}")

        # 9 Save the model with pickle
        pickle.dump(model, open("D:\PROGRAMARE\PORTOFOLIO\PandasDataFrame\output_data\model_1.pkl", "wb"))
        print("Model saved with pickle")

        pd_model = PandasModel(df_pred)
        self.main_window_tableView.setModel(pd_model)
        print("Reached here....done")

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label.setText(_translate("MainWindow", "Welcome to my Pandas Dataframe Project @BogdanMFometescu"))
        self.label.adjustSize()

        self.menuFile.setTitle(_translate("MainWindow", "File"))

        self.menuDataFrame.setTitle(_translate("MainWindow", "DataFrameOperations"))

        self.menuWeatherApp.setTitle(_translate("MainWindow", "WeatherApp"))

        self.menuData_Analysis.setTitle(_translate("MainWindow", "Data Analysis"))

        self.menuVisualize_data.setTitle(_translate("MainWindow", "Visualize data"))

        self.menuScikitLearn.setTitle(_translate("MainWindow", "ScikitLearn"))

        self.actionOpen.setText(_translate("MainWindow", "Open CSV file"))

        self.actionShow_column_data.setText(_translate("MainWindow", "Show column data"))

        self.actionShow_row_data.setText(_translate("MainWindow", "Show row data"))

        self.actionRename_column_2.setText(_translate("MainWindow", "Rename column"))

        self.actionDelete_column.setText(_translate("MainWindow", "Delete column"))

        self.actionSearch_Weather_Info.setText(_translate("MainWindow", "Search Weather Info"))

        self.actionSelect_multiple_columns.setText(_translate("MainWindow", "Select multiple columns"))

        self.actionReplace_values_in_row.setText(_translate("MainWindow", "Replace values in row"))

        self.actionShow_Data_Head.setText(_translate("MainWindow", "Show Data Head"))

        self.actionAdd_new_column.setText(_translate("MainWindow", "Add new column"))

        self.actionFilter_data_2.setText(_translate("MainWindow", "Filter data"))

        self.actionSum_up_columns.setText(_translate("MainWindow", "Sum up columns"))

        self.actionSplit_column_data.setText(_translate("MainWindow", "Split column data"))

        self.actionSelect_multiple_columns_2.setText(_translate("MainWindow", "Select multiple columns"))

        self.actionReplace_all_values_in_row.setText(_translate("MainWindow", "Add new row"))

        self.actionMatPlotLib.setText(_translate("MainWindow", "MatPlotLib"))

        self.actionBokeh.setText(_translate("MainWindow", "Bokeh"))

        self.actionScikitLearn.setText(_translate("MainWindow", "SupervisedLearning"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GuiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
