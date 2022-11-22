import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.account_created import Ui_Form


class ConnectDB:
    def __init__(self):
        self.db = sqlite3.connect("D:\\PROGRAMARE\\PORTOFOLIO\\PandasDataFrame\\test.sqlite")
        self.cursor = self.db.cursor()
        self.column_user = "User"
        self.column_pass = "Password"
        self.column_email = "Email"
        self.filename = "test"

    def create_table(self):
        try:
            table = f"CREATE TABLE IF NOT EXISTS {self.filename} ({self.column_user} TEXT ,{self.column_pass} TEXT ," \
                    f" {self.column_email} TEXT)"
            self.cursor.execute(table)
            self.db.commit()

        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            print("Exception class is: ", err.__class__)


class UiRegisterWindow(ConnectDB):
    def __init__(self):
        super(UiRegisterWindow, self).__init__()
        self.welcome_label = QtWidgets.QLabel(RegisterWindow)
        self.ui_username = QtWidgets.QLineEdit(RegisterWindow)
        self.username = QtWidgets.QLabel(RegisterWindow)
        self.password = QtWidgets.QLabel(RegisterWindow)
        self.email = QtWidgets.QLabel(RegisterWindow)
        self.ui_password = QtWidgets.QLineEdit(RegisterWindow)
        self.ui_email = QtWidgets.QLineEdit(RegisterWindow)
        self.registerBtn = QtWidgets.QPushButton(RegisterWindow)
        self.label_2 = QtWidgets.QLabel(RegisterWindow)
        self.loginBtn1 = QtWidgets.QPushButton(RegisterWindow)
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()

    def setup_ui(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(797, 499)
        self.welcome_label = QtWidgets.QLabel(RegisterWindow)
        self.welcome_label.setGeometry(QtCore.QRect(180, 80, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")

        self.ui_username = QtWidgets.QLineEdit(RegisterWindow)
        self.ui_username.setGeometry(QtCore.QRect(300, 180, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_username.setFont(font)
        self.ui_username.setObjectName("ui_username")

        self.username = QtWidgets.QLabel(RegisterWindow)
        self.username.setGeometry(QtCore.QRect(180, 180, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setObjectName("username")

        self.password = QtWidgets.QLabel(RegisterWindow)
        self.password.setGeometry(QtCore.QRect(180, 230, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")

        self.email = QtWidgets.QLabel(RegisterWindow)
        self.email.setGeometry(QtCore.QRect(180, 280, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setObjectName("email")

        self.ui_password = QtWidgets.QLineEdit(RegisterWindow)
        self.ui_password.setGeometry(QtCore.QRect(300, 230, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_password.setFont(font)
        self.ui_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui_password.setObjectName("ui_password")

        self.ui_email = QtWidgets.QLineEdit(RegisterWindow)
        self.ui_email.setGeometry(QtCore.QRect(300, 280, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_email.setFont(font)
        self.ui_email.setObjectName("ui_email")

        self.registerBtn = QtWidgets.QPushButton(RegisterWindow)
        self.registerBtn.setGeometry(QtCore.QRect(370, 340, 93, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.registerBtn.setFont(font)
        self.registerBtn.setObjectName("registerBtn")
        self.registerBtn.clicked.connect(self.register_user)
        self.registerBtn.clicked.connect(self.account_created_msg)

        self.label_2 = QtWidgets.QLabel(RegisterWindow)
        self.label_2.setGeometry(QtCore.QRect(130, 430, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.loginBtn1 = QtWidgets.QPushButton(RegisterWindow)
        self.loginBtn1.setGeometry(QtCore.QRect(370, 440, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loginBtn1.setFont(font)
        self.loginBtn1.setObjectName("loginBtn1")

        self.retranslate_ui(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def account_created_msg(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def register_user(self):
        temp_list_info = []

        try:

            username = self.ui_username.text()
            password = self.ui_password.text()
            email = self.ui_email.text()
            res = self.cursor.execute(f"SELECT User FROM test")
            user_list = res.fetchall()

            temp_list = [item for item in map(list, user_list)]
            final_list = sum(temp_list, [])

            while username in final_list:
                print("Username already in use, please choose another one:")
                continue

            else:
                temp_list_info.append(username)
                temp_list_info.append(password)
                temp_list_info.append(email)

            try:
                add_values = f"INSERT INTO {self.filename}({self.column_user},{self.column_pass}," \
                             f"{self.column_email}) VALUES(?,?,?)"
                self.cursor.execute(add_values, temp_list_info)
                self.db.commit()
            except sqlite3.Error as err:
                print('Sql error: %s' % (' '.join(err.args)))
                print("Exception class is: ", err.__class__)

        except ValueError:
            print("Invalid input!")

    def retranslate_ui(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Dialog"))
        self.welcome_label.setText(_translate("RegisterWindow", "Welcome to My Project App"))
        self.username.setText(_translate("RegisterWindow", "Username"))
        self.password.setText(_translate("RegisterWindow", "Password"))
        self.email.setText(_translate("RegisterWindow", "Email"))
        self.registerBtn.setText(_translate("RegisterWindow", "Register"))
        self.label_2.setText(_translate("RegisterWindow", "Already have an account?"))
        self.loginBtn1.setText(_translate("RegisterWindow", "Log In"))


if __name__ == "__main__":
    import sys

    cb = ConnectDB()
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QDialog()
    ui = UiRegisterWindow()
    ui.setup_ui(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
