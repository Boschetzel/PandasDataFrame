import pandas as pd

from dataframe_operations import DataInput, DataOperations
from web_api.connect_api import ConnectToApi, WeatherApi

"""This is the main file( first i will finish the project in console to be sure it is working, then i will make a GUI
"""


class Main:
    def __init__(self):
        pass

    @staticmethod
    def show_menu():
        print("=========================================================")
        print("********CONNECTING TO API********************************")
        print("1.Connect to API and get DataFrame")
        print("********DATAFRAME OPERATIONS******************************")
        print("2.DataFrame info")
        print("3.Filter DataFrame based on min an max value of a column")
        print("4.Filter DataFrame based on a single colum values")
        print("5.Add new columns and sort data based on existent columns")
        print("6.Search any value based on column name  ")
        print("7.Sum up columns values and store them into a new column")
        print("8.Rename a column ")
        print("********DATAFRAME VISUALIZATION**************************")
        print("9.Visualize data based on two columns")
        print("********EXIT PROGRAM*************************************")
        print("0.Exit the program")

    @staticmethod
    def save_to_csv(file_csv):
        file_output = pd.DataFrame(file_csv)
        try:
            while True:
                print("Do you want to save changes to a new .csv file? Y/N :")
                choice = input()
                match choice:
                    case "Y":
                        file_output.to_csv("D:\\PROGRAMARE\\PORTOFOLIO\\PandasDataFrame\\output_data\\report1.csv")
                    case "N":
                        break
                    case _:
                        print("Wrong input")
        except ValueError:
            print("Please enter a valid input")


if __name__ == "__main__":
    play = Main()
    ds = DataInput()
    do = DataOperations()
    weather_api = WeatherApi()
    connect = ConnectToApi()

    while True:
        play.show_menu()
        menu_choice = input("Please choose an option from the menu :")
        match menu_choice:
            case "1":
                connect.start()
            case "2":
                do.dataframe_info()
            case "3":
                a = do.filter_data()
                play.save_to_csv(a)
            case "4":
                b = do.find_column_values()
            case "5":
                c = do.add_new_column_and_sort()
                play.save_to_csv(c)
            case "6":
                d = do.find_row_values()
                play.save_to_csv(d)
            case "7":
                e = do.sum_up_columns()
                play.save_to_csv(e)
            case "8":
                f = do.rename_column()
                play.save_to_csv(f)
            case "9":
                do.visualize_data()

            case "0":
                break
            case _:
                print("Please choose a valid option:")
