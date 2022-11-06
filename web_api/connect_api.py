import pandas as pd
import requests


class ConnectToApi:
    def __init__(self):
        pass

    @staticmethod
    def start():
        connect.get_df_make_csv()
        # "https://geocoding-api.open-meteo.com/v1/search" -This is the geo link to api(get the lat and long)
        # "https://api.open-meteo.com/v1/forecast" - this is the weather info to api(get weather info)

    @staticmethod
    def get_df_make_csv():
        df = weather.get_weather_info()
        df.to_csv("D:\\PROGRAMARE\\PORTOFOLIO\\PandasDataFrame\\input_data\\raw_data.csv")
        print("File was saved as CSV format")

    @staticmethod
    def connection_info():
        url = str(input("Enter the API  LINK - URL :"))
        return url


class WeatherApi(ConnectToApi):
    def __init__(self):
        super(WeatherApi, self).__init__()

    @staticmethod
    def get_city_name():
        city_name = str(input("Enter city name: "))
        return city_name

    @staticmethod
    def connect():
        url = connect.connection_info()
        city_name = weather.get_city_name()
        request_url = f"{url}?name={city_name}&count=1"
        response = requests.get(request_url)
        if response.status_code == 200:
            print("Connection successful to API")
            return response
        else:
            print("Error, could not connect to API")

    @staticmethod
    def get_json_data():
        data_coord = weather.connect().json()
        lat = float(data_coord["results"][0]["latitude"]).__round__(2)
        long = float(data_coord["results"][0]["longitude"]).__round__(2)
        my_lst = [lat, long]
        return my_lst

    @staticmethod
    def get_weather_info():
        my_lst = weather.get_json_data()
        latitude = my_lst[0]
        longitude = my_lst[1]
        url = connect.connection_info()
        request_url = f"{url}?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        response = requests.get(request_url)
        if response.status_code == 200:
            print("Connection successful to API.DataFrame created...")
            data_weather = response.json()
            df = pd.DataFrame(data_weather)
            return df
        else:
            print("Error, could not connect to API")




connect = ConnectToApi()
weather = WeatherApi()
