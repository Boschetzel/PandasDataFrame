
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_weather_info_selenium(object):
    def setupUi(self, weather_info_selenium):
        weather_info_selenium.setObjectName("weather_info_selenium")
        weather_info_selenium.resize(693, 318)
        self.label = QtWidgets.QLabel(weather_info_selenium)
        self.label.setGeometry(QtCore.QRect(160, 40, 451, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_location = QtWidgets.QLineEdit(weather_info_selenium)
        self.ui_location.setGeometry(QtCore.QRect(320, 90, 211, 22))
        self.ui_location.setObjectName("ui_location")
        self.label_2 = QtWidgets.QLabel(weather_info_selenium)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.save_data_btn = QtWidgets.QPushButton(weather_info_selenium)
        self.save_data_btn.setGeometry(QtCore.QRect(370, 160, 93, 28))
        self.save_data_btn.setObjectName("save_data_btn")

        self.retranslateUi(weather_info_selenium)
        QtCore.QMetaObject.connectSlotsByName(weather_info_selenium)

    def retranslateUi(self, weather_info_selenium):
        _translate = QtCore.QCoreApplication.translate
        weather_info_selenium.setWindowTitle(_translate("weather_info_selenium", "Weather info"))
        self.label.setText(_translate("weather_info_selenium", "GET WEATHER INFO WITH SELENIUM"))
        self.label_2.setText(_translate("weather_info_selenium", "Enter location"))
        self.save_data_btn.setText(_translate("weather_info_selenium", "Show "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    weather_info_selenium = QtWidgets.QDialog()
    ui = Ui_weather_info_selenium()
    ui.setupUi(weather_info_selenium)
    weather_info_selenium.show()
    sys.exit(app.exec_())
