

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_filter_col_data(object):
    def setupUi(self, filter_data):
        filter_data.setObjectName("add_new_column")
        filter_data.resize(780, 438)
        self.label = QtWidgets.QLabel(filter_data)
        self.label.setGeometry(QtCore.QRect(180, 50, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_col_name = QtWidgets.QLineEdit(filter_data)
        self.ui_col_name.setGeometry(QtCore.QRect(420, 100, 201, 31))
        self.ui_col_name.setObjectName("ui_col_position")
        self.label_2 = QtWidgets.QLabel(filter_data)
        self.label_2.setGeometry(QtCore.QRect(180, 100, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(filter_data)
        self.label_4.setGeometry(QtCore.QRect(180, 160, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ui_min_value = QtWidgets.QLineEdit(filter_data)
        self.ui_min_value.setGeometry(QtCore.QRect(420, 160, 201, 31))
        self.ui_min_value.setObjectName("ui_new_col_name")
        self.label_5 = QtWidgets.QLabel(filter_data)
        self.label_5.setGeometry(QtCore.QRect(180, 220, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ui_max_value = QtWidgets.QLineEdit(filter_data)
        self.ui_max_value.setGeometry(QtCore.QRect(420, 210, 201, 31))
        self.ui_max_value.setObjectName("ui_data_fill")

        self.filter_btn = QtWidgets.QPushButton(filter_data)
        self.filter_btn.setGeometry(QtCore.QRect(420, 270, 201, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.filter_btn.setFont(font)
        self.filter_btn.setObjectName("add_col_btn")

        self.retranslateUi(filter_data)
        QtCore.QMetaObject.connectSlotsByName(filter_data)

    def retranslateUi(self, filter_column_data):
        _translate = QtCore.QCoreApplication.translate
        filter_column_data.setWindowTitle(_translate("add_new_column", "Filter Column"))
        self.label.setText(_translate("add_new_column", "Filter column data based on a min and max value  "))
        self.label_2.setText(_translate("add_new_column", "Enter column name"))
        self.label_4.setText(_translate("add_new_column", "Enter minimum value"))
        self.label_5.setText(_translate("add_new_column", "Enter maximum value"))
        self.filter_btn.setText(_translate("add_new_column", "Filter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filter_col = QtWidgets.QDialog()
    ui = Ui_filter_col_data()
    ui.setupUi(filter_col)
    filter_col.show()
    sys.exit(app.exec_())
