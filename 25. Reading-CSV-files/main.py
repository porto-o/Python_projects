# with open("weather_data.csv") as file:
#     files_read = file.readlines()
# #     print(files_read)
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
max_temp = data["temp"].max()

print(data[data["temp"] == max_temp])