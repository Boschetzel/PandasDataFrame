import pandas as pd
import requests


class ConnectToApi:
    def __init__(self):
        city_name = input("City name: ")
        self.df = pd.read_csv("D:\\PROGRAMARE\\PORTOFOLIO\\WebAPI-Python\\final_Weather_results.csv")
        self.url = "https://geocoding-api.open-meteo.com/v1/search"
        self.request_url = f"{self.url}?name={city_name}&count=1"
        self.get_response = ""

    def connect_to_api(self):
        pass


class WeatherApi(ConnectToApi):
    def __init__(self):
        super(WeatherApi, self).__init__()

    def get_city_coordinates(self):
        city_name = input("City name: ")
        self.url = "https://geocoding-api.open-meteo.com/v1/search"
        self.request_url = f"{self.url}?name={city_name}&count=1"
        # Send the request and get the response
        self.get_response = requests.get(self.request_url)
        # Store data to json
        data_coord = self.get_response.json()
        lat = float(data_coord["results"][0]["latitude"]).__round__(2)
        long = float(data_coord["results"][0]["longitude"]).__round__(2)
        my_lst = [lat, long, city_name]
        return my_lst

    def get_weather_info(self):
        # Get the latitude and longitude
        my_lst = weather.get_city_coordinates()
        latitude = my_lst[0]
        longitude = my_lst[1]
        city_name = my_lst[2]
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.request_url = f"{self.url}?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        # Send the request and get the response
        self.get_response = requests.get(self.request_url)
        # Store info to json
        data_weather = self.get_response.json()
        # Make the info a DF
        df = pd.DataFrame(data_weather)
        # Save the data to .csv
        weather_csv = df.to_csv("raw_data_input.csv")
        return weather_csv

    def split_data(self):
        df_copy = self.df.copy(True)
        # Split a column into multiple columns
        split_hours = df_copy["hourly"].str.split(",", expand=True)
        select_columns = split_hours.loc[:, "0":"23"]
        df_split = pd.DataFrame(select_columns)
        df_split.to_csv("split_by_hour.csv")
        print(df_split)

    def rename_columns(self):
        hours_columns_new = {"0": "00:00 am ",
                             "1": "01:00 am ",
                             "2": "02:00 am",
                             "3": "03:00 am",
                             "4": "04:00 am",
                             "5": "05:00 am",
                             "6": "06:00 am",
                             "7": "07:00 am",
                             "8": "08:00 am",
                             "9": "09:00 am",
                             "10": "10:00 am",
                             "11": "11:00 am",
                             "12": "12:00 am",
                             "13": "13:00 pm",
                             "14": "14:00 pm",
                             "15": "15:00 pm",
                             "16": "16:00 pm",
                             "17": "17:00 pm",
                             "18": "18:00 pm",
                             "19": "19:00 pm",
                             "20": "20:00 pm",
                             "21": "21:00 pm",
                             "22": "22:00 pm",
                             "23": "23:00 pm",
                             }

        df_copy = self.df.copy(True)
        # Rename columns
        df_copy = df_copy.rename(columns=hours_columns_new)
        df_copy.to_csv("renamed_columns.csv")

    def split_temperature(self):
        df_copy = self.df.copy(True)
        del df_copy["Unnamed: 0.1"]
        del df_copy["Unnamed: 0"]
        df_copy.loc[0] = "2022-11-03"
        df_copy.to_csv("final_data.csv")

    def transpose_data(self):
        df_copy = self.df.copy(True)
        del df_copy["Unnamed: 0"]
        df_trans = df_copy.transpose()
        xx = pd.DataFrame(df_trans)
        xx.to_csv("final_Weather_results.csv")

    def convert_str_to_int(self):
        df_copy = self.df.copy(True)
        df_copy.loc[0] = 1
        df_copy = df_copy.rename(columns={"1": "Temperature"})
        df_copy = df_copy.rename(columns={"0": "Date"})
        df_copy = df_copy.rename(columns={"Unnamed: 0": "Hour"})
        df_copy["Temperature"] = df_copy["Temperature"].astype(float)
        df_copy.loc[0] = ["1", "2022-11-03", 14.4]
        df_out = pd.DataFrame(df_copy)
        df_out.to_csv("final.csv")


collect = ConnectToApi()
weather = WeatherApi()
