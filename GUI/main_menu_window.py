# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from df_model import PandasModel


class Ui_MainWindow(object):
    def __init__(self):
        self.actionBokeh = None
        self.actionMatPlotLib = None
        self.actionReplace_all_values_in_row = None
        self.actionSelect_multiple_columns_2 = None
        self.actionSplit_column_data = None
        self.actionSum_up_columns = None
        self.actionFilter_data_2 = None
        self.actionAdd_new_column = None
        self.actionConvert_Str_to_Int = None
        self.actionConvert_Str_to_Float = None
        self.actionShow_Data_Head = None
        self.actionTranspose_DF = None
        self.actionReplace_values_in_row = None
        self.actionSelect_multiple_columns = None
        self.actionSum_columns = None
        self.actionFilter_data = None
        self.actionSearch_Weather_Info = None
        self.actionDelete_column = None
        self.actionRename_column_2 = None
        self.actionSearch = None
        self.actionDelete_colum = None
        self.actionRename_column = None
        self.actionShow_row_data = None
        self.actionShow_column_data = None
        self.actionSave = None
        self.actionOpen = None
        self.statusbar = None
        self.menuVisualize_data = None
        self.menuData_Analysis = None
        self.menuWeatherApp = None
        self.menuDataFrame = None
        self.menuFile = None
        self.menubar = None
        self.label = None
        self.main_window_tableView = None
        self.central_widget = None

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

        self.actionOpen.triggered.connect(lambda: self.open_df())

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    @staticmethod
    def get_csv_filename():
        filename, _ = QFileDialog.getOpenFileName()
        return filename

    def convert_csv_to_df(self):
        csv_filename = self.get_csv_filename()
        reader = pd.read_csv(csv_filename)
        df = pd.DataFrame(reader)
        return df

    def pandas_model(self):
        df = self.convert_csv_to_df()
        model = PandasModel(df)
        return model

    def open_df(self):
        self.main_window_tableView.setModel(self.pandas_model())

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
