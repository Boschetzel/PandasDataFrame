import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GUI.account_created import Ui_Form_Acc
from GUI.login_window import Ui_Form
from GUI.login_succes import Ui_Log_in_success
from GUI.login_failed import Ui_log_in_failed
from GUI.main_menu_window import Ui_MainWindow
from GUI.username_taken import Ui_Username_taken

"""A very basic Class to connect and create a table in sqlite database """


class ConnectDB:
    def __init__(self):
        self.db = sqlite3.connect("D:\\PROGRAMARE\\PORTOFOLIO\\PandasDataFrame\\test.sqlite")
        self.cursor = self.db.cursor()
        self.column_user = "User"
        self.column_pass = "Password"
        self.column_email = "Email"
        self.filename = "test"

    # Method to create a table in sqlite database
    def create_table(self):
        try:
            table = f"CREATE TABLE IF NOT EXISTS {self.filename} ({self.column_user} TEXT ,{self.column_pass} TEXT ," \
                    f" {self.column_email} TEXT)"
            self.cursor.execute(table)
            self.db.commit()

        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            print("Exception class is: ", err.__class__)


"""A Class which contains the pyqt5 window and methods to allows user 
to register an account and login based on info from the database.
The code for the GUI is generated with QT Designer
"""


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
        self.ui = Ui_Form_Acc()
        self.ui2 = Ui_Form()
        self.ui3 = Ui_MainWindow()
        self.Log_in_success = QtWidgets.QWidget()
        self.log_in_failed = QtWidgets.QWidget()
        self.MainWindow = QtWidgets.QMainWindow()
        self.Dialog = QtWidgets.QDialog()
        self.view = QtWidgets.QTableView()

    # GUI Window for Register and Login user
    def setup_ui(self, RegisterWindow1):
        RegisterWindow1.setObjectName("RegisterWindow")
        RegisterWindow1.resize(797, 499)
        self.welcome_label = QtWidgets.QLabel(RegisterWindow1)
        self.welcome_label.setGeometry(QtCore.QRect(180, 80, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        # Username input LineEdit object
        self.ui_username = QtWidgets.QLineEdit(RegisterWindow1)
        self.ui_username.setGeometry(QtCore.QRect(300, 180, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_username.setFont(font)
        self.ui_username.setObjectName("ui_username")
        # Username label
        self.username = QtWidgets.QLabel(RegisterWindow1)
        self.username.setGeometry(QtCore.QRect(180, 180, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setObjectName("username")
        # Password label
        self.password = QtWidgets.QLabel(RegisterWindow1)
        self.password.setGeometry(QtCore.QRect(180, 230, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")
        # Email label
        self.email = QtWidgets.QLabel(RegisterWindow1)
        self.email.setGeometry(QtCore.QRect(180, 280, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setObjectName("email")
        # Password input LineEdit object
        self.ui_password = QtWidgets.QLineEdit(RegisterWindow1)
        self.ui_password.setGeometry(QtCore.QRect(300, 230, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_password.setFont(font)
        self.ui_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui_password.setObjectName("ui_password")
        # Email input LineEdit object
        self.ui_email = QtWidgets.QLineEdit(RegisterWindow1)
        self.ui_email.setGeometry(QtCore.QRect(300, 280, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_email.setFont(font)
        self.ui_email.setObjectName("ui_email")
        # Register button object
        self.registerBtn = QtWidgets.QPushButton(RegisterWindow1)
        self.registerBtn.setGeometry(QtCore.QRect(370, 340, 93, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.registerBtn.setFont(font)
        self.registerBtn.setObjectName("registerBtn")
        self.registerBtn.clicked.connect(self.register_user)
        # Already have and account label
        self.label_2 = QtWidgets.QLabel(RegisterWindow1)
        self.label_2.setGeometry(QtCore.QRect(130, 430, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # Login button object
        self.loginBtn1 = QtWidgets.QPushButton(RegisterWindow1)
        self.loginBtn1.setGeometry(QtCore.QRect(370, 440, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loginBtn1.setFont(font)
        self.loginBtn1.setObjectName("loginBtn1")
        self.loginBtn1.clicked.connect(self.show_login_window)

        self.retranslate_ui(RegisterWindow1)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow1)

    # A method to allow user to register an account into the database
    def register_user(self):
        # Creating a list to store the user input info( username,password,email)
        temp_list_info = []
        try:
            # Get the user input info
            username = self.ui_username.text()
            password = self.ui_password.text()
            email = self.ui_email.text()
            # Execute the sqlite command to check if username already exists in database
            res = self.cursor.execute(f"SELECT User FROM test")
            user_list = res.fetchall()
            # Cleaning the list from the fetchall function
            temp_list = [item for item in map(list, user_list)]
            final_list = sum(temp_list, [])
            # Check if username is in list
            while username in final_list:
                self.show_username_already_in_use()
                break

            # Add the user input info to the list
            else:
                temp_list_info.append(username)
                temp_list_info.append(password)
                temp_list_info.append(email)
                # Show the main window (GUI) for  PandasDataFrame
                self.show_account_created_window()
                self.show_main_window()

            # Add the user input info to the sqlite database
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

    # Method to allow user to login base on data stored in the sqlite database
    def login_user(self):
        # Gets the user input for username and password
        username = self.ui2.ui_username.text()
        password = self.ui2.ui_password.text()
        # Execute the sqlite command to select the users from DB
        res = self.cursor.execute(f"SELECT User,Password FROM {self.filename}")
        users_list = res.fetchall()
        # Cleaning the list from the fetchall function
        temp_list = [item for item in map(list, users_list)]
        final_list = sum(temp_list, [])
        # Check if username and password are in the list
        while True:
            if username and password in final_list:
                # Show the main window (GUI) for  PandasDataFrame
                self.show_main_window()
                break
            else:
                # Show the login failed window
                self.show_login_failed_window()
                break

    # Method to show the login succes window
    def show_login_success_window(self):
        self.Log_in_success = QtWidgets.QWidget()
        self.ui = Ui_Log_in_success()
        self.ui.setupUi(self.Log_in_success)
        self.Log_in_success.show()

    # Method to show the login failed window
    def show_login_failed_window(self):
        self.log_in_failed = QtWidgets.QWidget()
        self.ui = Ui_log_in_failed()
        self.ui.setupUi(self.log_in_failed)
        self.log_in_failed.show()

    # Method to show the login window
    def show_login_window(self):
        self.Form = QtWidgets.QWidget()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.Form)
        self.Form.show()
        self.ui2.loginBtn2.clicked.connect(self.login_user)

    # Method to show the account created window
    def show_account_created_window(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form_Acc()
        self.ui.setupUi(self.Form)
        self.Form.show()

    # Method to show the main window of PandasDataFrame project
    def show_main_window(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui3 = Ui_MainWindow()
        self.ui3.setupUi(self.MainWindow)
        self.MainWindow.show()

    def show_username_already_in_use(self):
        self.Username_taken = QtWidgets.QDialog()
        self.ui_taken = Ui_Username_taken()
        self.ui_taken.setupUi(self.Username_taken)
        self.Username_taken.show()





    # PYGT5 method -auto generated by Qt Designer
    def retranslate_ui(self, RegisterWindow1):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow1.setWindowTitle(_translate("RegisterWindow", "Dialog"))
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
