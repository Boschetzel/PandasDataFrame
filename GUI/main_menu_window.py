from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd

from GUI.show_column_data import Ui_df_operations_window
from GUI.show_row_data import Ui_df_operations_window_rows
from GUI.rename_column import Ui_rename_column
from GUI.delete_column import Ui_df_delete_col
from GUI.add_new_column import Ui_add_new_column
from GUI.filter_col_data import Ui_filter_col_data
from df_model import PandasModel


class Ui_MainWindow:
    def __init__(self):

        self.df = None
        self.dict_col = {}

    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow")
        MainWindow1.resize(1172, 838)
        self.central_widget = QtWidgets.QWidget(MainWindow1)
        self.central_widget.setObjectName("centralwidget")

        self.main_window_tableView = QtWidgets.QTableView(self.central_widget)
        self.main_window_tableView.setGeometry(QtCore.QRect(190, 120, 771, 501))
        self.main_window_tableView.setObjectName("main_window_tableView")

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(490, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

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
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")

        MainWindow1.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow1)
        self.actionSave.setObjectName("actionSave")
        self.actionShow_column_data = QtWidgets.QAction(MainWindow1)
        self.actionShow_column_data.setObjectName("actionShow_column_data")
        self.actionShow_row_data = QtWidgets.QAction(MainWindow1)
        self.actionShow_row_data.setObjectName("actionShow_row_data")
        self.actionRename_column = QtWidgets.QAction(MainWindow1)
        self.actionRename_column.setObjectName("actionRename_column")
        self.actionDelete_colum = QtWidgets.QAction(MainWindow1)
        self.actionDelete_colum.setObjectName("actionDelete_colum")
        self.actionSearch = QtWidgets.QAction(MainWindow1)
        self.actionSearch.setObjectName("actionSearch")
        self.actionRename_column_2 = QtWidgets.QAction(MainWindow1)
        self.actionRename_column_2.setObjectName("actionRename_column_2")
        self.actionDelete_column = QtWidgets.QAction(MainWindow1)
        self.actionDelete_column.setObjectName("actionDelete_column")
        self.actionSearch_Weather_Info = QtWidgets.QAction(MainWindow1)
        self.actionSearch_Weather_Info.setObjectName("actionSearch_Weather_Info")
        self.actionFilter_data = QtWidgets.QAction(MainWindow1)
        self.actionFilter_data.setObjectName("actionFilter_data")
        self.actionSum_columns = QtWidgets.QAction(MainWindow1)
        self.actionSum_columns.setObjectName("actionSum_columns")
        self.actionSelect_multiple_columns = QtWidgets.QAction(MainWindow1)
        self.actionSelect_multiple_columns.setObjectName("actionSelect_multiple_columns")
        self.actionReplace_values_in_row = QtWidgets.QAction(MainWindow1)
        self.actionReplace_values_in_row.setObjectName("actionReplace_values_in_row")
        self.actionTranspose_DF = QtWidgets.QAction(MainWindow1)
        self.actionTranspose_DF.setObjectName("actionTranspose_DF")
        self.actionShow_Data_Head = QtWidgets.QAction(MainWindow1)
        self.actionShow_Data_Head.setObjectName("actionShow_Data_Head")
        self.actionConvert_Str_to_Float = QtWidgets.QAction(MainWindow1)
        self.actionConvert_Str_to_Float.setObjectName("actionConvert_Str_to_Float")
        self.actionConvert_Str_to_Int = QtWidgets.QAction(MainWindow1)
        self.actionConvert_Str_to_Int.setObjectName("actionConvert_Str_to_Int")
        self.actionAdd_new_column = QtWidgets.QAction(MainWindow1)
        self.actionAdd_new_column.setObjectName("actionAdd_new_column")
        self.actionFilter_data_2 = QtWidgets.QAction(MainWindow1)
        self.actionFilter_data_2.setObjectName("actionFilter_data_2")
        self.actionSum_up_columns = QtWidgets.QAction(MainWindow1)
        self.actionSum_up_columns.setObjectName("actionSum_up_columns")
        self.actionSplit_column_data = QtWidgets.QAction(MainWindow1)
        self.actionSplit_column_data.setObjectName("actionSplit_column_data")
        self.actionSelect_multiple_columns_2 = QtWidgets.QAction(MainWindow1)
        self.actionSelect_multiple_columns_2.setObjectName("actionSelect_multiple_columns_2")
        self.actionReplace_all_values_in_row = QtWidgets.QAction(MainWindow1)
        self.actionReplace_all_values_in_row.setObjectName("actionReplace_all_values_in_row")
        self.actionMatPlotLib = QtWidgets.QAction(MainWindow1)
        self.actionMatPlotLib.setObjectName("actionMatPlotLib")
        self.actionBokeh = QtWidgets.QAction(MainWindow1)
        self.actionBokeh.setObjectName("actionBokeh")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
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
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDataFrame.menuAction())
        self.menubar.addAction(self.menuData_Analysis.menuAction())
        self.menubar.addAction(self.menuVisualize_data.menuAction())
        self.menubar.addAction(self.menuWeatherApp.menuAction())

        # MENU OPTIONS TRIGGER
        self.actionOpen.triggered.connect(lambda: self.open_df())
        self.actionShow_column_data.triggered.connect(self.show_column_data_window)
        self.actionShow_row_data.triggered.connect(self.show_row_data_window)
        self.actionRename_column_2.triggered.connect(self.show_rename_window)
        self.actionShow_Data_Head.triggered.connect(self.show_df_head)
        self.actionDelete_column.triggered.connect(self.show_delete_col_view)
        self.actionAdd_new_column.triggered.connect(self.show_add_new_column)
        self.actionFilter_data_2.triggered.connect(self.show_filter_col_window)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    # FILE MENU :
    # OPEN
    # SAVE
    @staticmethod
    def get_csv_filename():
        filename, _ = QFileDialog.getOpenFileName()
        return filename

    def convert_csv_to_df(self):
        csv_filename = self.get_csv_filename()
        reader = pd.read_csv(csv_filename)
        df = pd.DataFrame(reader)
        self.df = df
        return df

    def pandas_model(self):
        df = self.convert_csv_to_df()
        model = PandasModel(df)
        return model

    def open_df(self):
        self.main_window_tableView.setModel(self.pandas_model())

    # DATA OPERATIONS MENU :
    # SHOW DATA HEAD
    # SHOW COLUMN DATA
    # SHOW ROW DATA
    # RENAME COLUMN
    # DELETE COLUMN
    def show_column_data_window(self):
        self.df_operations_window = QtWidgets.QDialog()
        self.ui = Ui_df_operations_window()
        self.ui.setupUi(self.df_operations_window)
        self.df_operations_window.show()
        self.ui.show_results_btn.clicked.connect(self.show_column_data_values)

    def show_column_data_values(self):
        col_name = self.ui.ui_column_name.text()
        df_col = self.df[col_name]
        df_col1 = pd.DataFrame(df_col)
        model = PandasModel(df_col1)
        self.main_window_tableView.setModel(model)
        return model

    def show_row_data_window(self):
        self.df_operations_rows_wnd = QtWidgets.QDialog()
        self.ui_row = Ui_df_operations_window_rows()
        self.ui_row.setupUi(self.df_operations_rows_wnd)
        self.df_operations_rows_wnd.show()
        self.ui_row.show_results_btn.clicked.connect(self.show_row_data_values)

    def show_row_data_values(self):
        search_column = self.ui_row.ui_column_name.text()
        row_search = self.ui_row.ui_row_name.text()
        if row_search.isdigit():
            df_row = self.df.loc[self.df[search_column] == int(row_search)]
            df_row_save = pd.DataFrame(df_row)
            model = PandasModel(df_row_save)
            self.main_window_tableView.setModel(model)
        else:
            df_row = self.df.loc[self.df[search_column] == row_search]
            df_row_save = pd.DataFrame(df_row)
            model = PandasModel(df_row_save)
            self.main_window_tableView.setModel(model)
        return model

    def show_rename_window(self):
        self.rename_col = QtWidgets.QDialog()
        self.ui_rename = Ui_rename_column()
        self.ui_rename.setupUi(self.rename_col)
        self.rename_col.show()
        self.ui_rename.apply_btn.clicked.connect(self.rename_column)

    def rename_column(self):
        self.dict_col = {}
        col_old_name = self.ui_rename.ui_old_name.text()
        col_new_name = self.ui_rename.ui_new_name.text()
        self.dict_col[col_old_name] = col_new_name
        temp = self.df.rename(columns=self.dict_col, inplace=False)
        new_df = pd.DataFrame(temp)
        model = PandasModel(new_df)
        self.main_window_tableView.setModel(model)

    def show_df_head(self):
        df = self.df.head()
        df_head = pd.DataFrame(df)
        model = PandasModel(df_head)
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

    def show_add_new_column(self):
        self.add_new_column = QtWidgets.QDialog()
        self.ui_add_col = Ui_add_new_column()
        self.ui_add_col.setupUi(self.add_new_column)
        self.add_new_column.show()
        self.ui_add_col.add_col_btn.clicked.connect(self.add_column)

    def add_column(self):
        ui_col_loc = int(self.ui_add_col.ui_col_position.text())
        ui_new_col_name = self.ui_add_col.ui_new_col_name.text()
        ui_content = self.ui_add_col.ui_data_fill.text()
        self.df.insert(ui_col_loc, ui_new_col_name, ui_content)
        df = pd.DataFrame(self.df)
        model = PandasModel(df)
        self.main_window_tableView.setModel(model)
        # self.df[ui_new_col_name] = pd.DataFrame([ui_content for _ in range(len(self.df.index))])

    def show_filter_col_window(self):
        self.filter_col = QtWidgets.QDialog()
        self.ui_filter = Ui_filter_col_data()
        self.ui_filter.setupUi(self.filter_col)
        self.filter_col.show()
        self.ui_filter.filter_btn.clicked.connect(self.filter_col_data)

    def filter_col_data(self):
        df = self.df.fillna(0)
        self.df = df
        col_name = self.ui_filter.ui_col_name.text()
        ui_min_val = int(self.ui_filter.ui_min_value.text())
        ui_max_val = int(self.ui_filter.ui_max_value.text())
        self.df[col_name] = self.df[col_name].astype(float)
        temp3 = self.df[(self.df[col_name] >= ui_min_val) & (self.df[col_name] <= ui_max_val)]
        df = pd.DataFrame(temp3)
        model = PandasModel(df)
        self.main_window_tableView.setModel(model)
        # TODO - fix nan values for Covid Dataset ( check type of values from CSV)

    def show_sum_up_column_window(self):
        pass

    def sum_columns(self):
        pass

















    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label.setText(_translate("MainWindow", "DataFrame "))

        self.menuFile.setTitle(_translate("MainWindow", "File"))

        self.menuDataFrame.setTitle(_translate("MainWindow", "DataFrameOperations"))

        self.menuWeatherApp.setTitle(_translate("MainWindow", "WeatherApp"))

        self.menuData_Analysis.setTitle(_translate("MainWindow", "Data Analysis"))

        self.menuVisualize_data.setTitle(_translate("MainWindow", "Visualize data"))

        self.actionOpen.setText(_translate("MainWindow", "Open CSV file"))

        self.actionSave.setText(_translate("MainWindow", "Save CSV file"))

        self.actionShow_column_data.setText(_translate("MainWindow", "Show column data"))

        self.actionShow_row_data.setText(_translate("MainWindow", "Show row data"))

        self.actionRename_column.setText(_translate("MainWindow", "Rename column"))

        self.actionDelete_colum.setText(_translate("MainWindow", "Delete colum"))

        self.actionSearch.setText(_translate("MainWindow", "Search "))

        self.actionRename_column_2.setText(_translate("MainWindow", "Rename column"))

        self.actionDelete_column.setText(_translate("MainWindow", "Delete column"))

        self.actionSearch_Weather_Info.setText(_translate("MainWindow", "Search Weather Info"))

        self.actionFilter_data.setText(_translate("MainWindow", "Filter data"))

        self.actionSum_columns.setText(_translate("MainWindow", "Sum columns"))

        self.actionSelect_multiple_columns.setText(_translate("MainWindow", "Select multiple columns"))

        self.actionReplace_values_in_row.setText(_translate("MainWindow", "Replace values in row"))

        self.actionTranspose_DF.setText(_translate("MainWindow", "Transpose DF"))

        self.actionShow_Data_Head.setText(_translate("MainWindow", "Show Data Head"))

        self.actionConvert_Str_to_Float.setText(_translate("MainWindow", "Convert Str to Float"))

        self.actionConvert_Str_to_Int.setText(_translate("MainWindow", "Convert Str to Int"))

        self.actionAdd_new_column.setText(_translate("MainWindow", "Add new column"))

        self.actionFilter_data_2.setText(_translate("MainWindow", "Filter data"))

        self.actionSum_up_columns.setText(_translate("MainWindow", "Sum up columns"))

        self.actionSplit_column_data.setText(_translate("MainWindow", "Split column data"))

        self.actionSelect_multiple_columns_2.setText(_translate("MainWindow", "Select multiple columns"))

        self.actionReplace_all_values_in_row.setText(_translate("MainWindow", "Replace all values in row"))

        self.actionMatPlotLib.setText(_translate("MainWindow", "MatPlotLib"))

        self.actionBokeh.setText(_translate("MainWindow", "Bokeh"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
