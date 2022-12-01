

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Acc(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 168)
        self.acc_created_label = QtWidgets.QLabel(Form)
        self.acc_created_label.setGeometry(QtCore.QRect(170, 60, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.acc_created_label.setFont(font)
        self.acc_created_label.setObjectName("acc_created_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.acc_created_label.setText(_translate("Form", "Account created!"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Acc()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
