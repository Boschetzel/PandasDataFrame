import sqlite3
import os


class RegisterAndLogin:
    def __init__(self):
        # Define the database columns
        self.column_user = "User"
        self.column_pass = "Password"
        self.column_email = "Email"
        # Connect to the sqlite database
        try:
            self.filename = str(input("Enter name of db:"))
            self.db_path = os.getcwd()
            self.output_dir = "login"
            self.output_filename = self.db_path + "\\" + self.output_dir + "\\" + self.filename + ".sqlite"
            self.db = sqlite3.connect(self.output_filename)
            self.cursor = self.db.cursor()
        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            print("Exception class is: ", err.__class__)
        self.create_table()

    """A method which will create a table in sqlite3 database"""

    def create_table(self):
        try:
            table = f"CREATE TABLE IF NOT EXISTS {self.filename} ({self.column_user} TEXT ,{self.column_pass} TEXT ," \
                    f" {self.column_email} TEXT)"
            self.cursor.execute(table)
            self.db.commit()

        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            print("Exception class is: ", err.__class__)

    """A method which allows a new use registration and saves the data into the database"""

    def register_user(self):
        temp_list_info = []

        try:

            username = str(input("Choose a Username:"))
            password = str(input("Choose a Password:"))
            email = str(input("Enter your email:"))
            res = self.cursor.execute(f"SELECT User FROM test")  # this needs to have a list as second argument
            user_list = res.fetchall()
            # Refactor the list resulted from the sqlite query, so it can be used further
            temp_list = [item for item in map(list, user_list)]
            final_list = sum(temp_list, [])

            while username in final_list:
                print("Username already in use, please choose another one:")
                username = str(input("Choose a Username:"))
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

    """A method which will allow the user to login based on the info stored in the database"""

    def login_user(self):
        username = str(input("Enter your Username:"))
        password = str(input("Enter your Password:"))

        res = self.cursor.execute(f"SELECT User,Password FROM {self.filename}  ")
        users_list = res.fetchall()
        # Refactor the list resulted from the sqlite query, so it can be used further
        temp_list = [item for item in map(list, users_list)]
        final_list = sum(temp_list, [])
        while True:
            if username and password in final_list:
                print("Logged in")

                break
            else:
                print("Wrong username of password")
                username = str(input("Enter your Username:"))
                password = str(input("Enter your Password:"))
