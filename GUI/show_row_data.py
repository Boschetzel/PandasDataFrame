# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_row_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_df_operations_window(object):
    def setupUi(self, df_operations_window):
        df_operations_window.setObjectName("df_operations_window")
        df_operations_window.resize(421, 293)
        self.label = QtWidgets.QLabel(df_operations_window)
        self.label.setGeometry(QtCore.QRect(120, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_column_name = QtWidgets.QLineEdit(df_operations_window)
        self.ui_column_name.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.ui_column_name.setObjectName("ui_column_name")
        self.show_results_btn = QtWidgets.QPushButton(df_operations_window)
        self.show_results_btn.setGeometry(QtCore.QRect(160, 210, 111, 28))
        self.show_results_btn.setObjectName("show_results_btn")
        self.label_2 = QtWidgets.QLabel(df_operations_window)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ui_column_name_2 = QtWidgets.QLineEdit(df_operations_window)
        self.ui_column_name_2.setGeometry(QtCore.QRect(160, 160, 113, 22))
        self.ui_column_name_2.setObjectName("ui_column_name_2")

        self.retranslateUi(df_operations_window)
        QtCore.QMetaObject.connectSlotsByName(df_operations_window)

    def retranslateUi(self, df_operations_window):
        _translate = QtCore.QCoreApplication.translate
        df_operations_window.setWindowTitle(_translate("df_operations_window", "Dialog"))
        self.label.setText(_translate("df_operations_window", "Enter the column name"))
        self.show_results_btn.setText(_translate("df_operations_window", "Show results"))
        self.label_2.setText(_translate("df_operations_window", "What are you looking for?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    df_operations_window = QtWidgets.QDialog()
    ui = Ui_df_operations_window()
    ui.setupUi(df_operations_window)
    df_operations_window.show()
    sys.exit(app.exec_())
