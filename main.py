import pandas as pd

from dataframe_operations import DataSorting, DataOperations


class Main:
    def __init__(self):
        pass

    @staticmethod
    def show_menu():
        print("1.DataFrame info")
        print("2.Filter DataFrame based on min an max value of a column")
        print("3.Filter DataFrame based on a single colum values")
        print("4.Add new columns and sort data based on existent columns")
        print("5.Search any value based on column name  ")
        print("6.Sum up columns values and store them into a new column")
        print("0.Exit the program")

    @staticmethod
    def save_csv(file_csv):
        file_output = pd.DataFrame(file_csv)
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


if __name__ == "__main__":
    play = Main()
    ds = DataSorting()
    do = DataOperations()

    while True:
        play.show_menu()
        menu_choice = input("Please choose an option from the menu :")
        match menu_choice:
            case "1":
                do.dataframe_info()
            case "2":
                a = do.filter_data()
                play.save_csv(a)
            case "3":
                b = do.find_column_values()
            case "4":
                b = do.add_new_columns_and_sort()
                play.save_csv(b)
            case "5":
                c = do.find_row_values()
                play.save_csv(c)
            case "6":
                d = do.sum_up_columns()
                play.save_csv(d)
            case "0":
                break
            case _:
                print("Please choose a valid option:")
