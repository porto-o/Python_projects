import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
num_grays = len(data["Primary Fur Color"] == "Gray")
num_red = len(data["Primary Fur Color"] == "Cinnamon")
num_black = len(data["Primary Fur Color"] == "Black")

data_dict = {
    "Fur Color": ["Gray","Red","Black"],
    "Count": [num_grays,num_red,num_black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("new_data.csv")