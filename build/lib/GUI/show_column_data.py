


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_df_operations_window:
    def setupUi(self, df_operations_window):
        df_operations_window.setObjectName("df_operations_window")
        df_operations_window.resize(421, 209)
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
        self.show_results_btn.setGeometry(QtCore.QRect(160, 110, 111, 28))
        self.show_results_btn.setObjectName("show_results_btn")


        self.retranslateUi(df_operations_window)
        QtCore.QMetaObject.connectSlotsByName(df_operations_window)




    def retranslateUi(self, df_operations_window):
        _translate = QtCore.QCoreApplication.translate
        df_operations_window.setWindowTitle(_translate("df_operations_window", "Show column data"))
        self.label.setText(_translate("df_operations_window", "Enter the column name"))
        self.show_results_btn.setText(_translate("df_operations_window", "Show results"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    df_operations_window = QtWidgets.QDialog()
    ui = Ui_df_operations_window()
    ui.setupUi(df_operations_window)
    df_operations_window.show()
    sys.exit(app.exec_())
