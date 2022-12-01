


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rename_column:
    def setupUi(self, df_rename_column):
        df_rename_column.setObjectName("df_operations_window")
        df_rename_column.resize(421, 293)
        self.label = QtWidgets.QLabel(df_rename_column)
        self.label.setGeometry(QtCore.QRect(120, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_old_name = QtWidgets.QLineEdit(df_rename_column)
        self.ui_old_name.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.ui_old_name.setObjectName("ui_column_name")
        self.apply_btn = QtWidgets.QPushButton(df_rename_column)
        self.apply_btn.setGeometry(QtCore.QRect(160, 210, 111, 28))
        self.apply_btn.setObjectName("show_results_btn")
        self.label_2 = QtWidgets.QLabel(df_rename_column)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ui_new_name = QtWidgets.QLineEdit(df_rename_column)
        self.ui_new_name.setGeometry(QtCore.QRect(160, 160, 113, 22))
        self.ui_new_name.setObjectName("ui_column_name_2")

        self.retranslateUi(df_rename_column)
        QtCore.QMetaObject.connectSlotsByName(df_rename_column)

    def retranslateUi(self, df_operations_row_window):
        _translate = QtCore.QCoreApplication.translate
        df_operations_row_window.setWindowTitle(_translate("df_operations_window", "Rename column"))
        self.label.setText(_translate("df_operations_window", "Enter old name"))
        self.apply_btn.setText(_translate("df_operations_window", "Apply"))
        self.label_2.setText(_translate("df_operations_window", "Enter new name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rename_col = QtWidgets.QDialog()
    ui = Ui_rename_column()
    ui.setupUi(rename_col)
    rename_col.show()
    sys.exit(app.exec_())
