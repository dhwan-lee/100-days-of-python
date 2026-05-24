# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()


# print(data)

# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

#     print(temperature)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))

# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()


# avg_temp = sum(temp_list) / (len(temp_list))

# print(avg_temp)
# print(data["temp"].mean())

# max_temp = data["temp"].max()
# print(max_temp)

# print(data["condition"])
# print(data.condition)

# Get Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == max_temp])
# monday = data[data.day == "Monday"]
# cel_to_fahrenheit = (monday["temp"] * 9 / 5) + 32

# print(cel_to_fahrenheit)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "black"])

data_dict = {
    "Fur Color": ["gray", 'cinnamon', "black"], 
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")