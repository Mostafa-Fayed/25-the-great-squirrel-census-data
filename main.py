import pandas as pd

data = pd.read_csv("Central_Park_Squirrel_Census_Data.csv")
# print(data.keys())

# Method-1
# fur_color = data["Primary Fur Color"].tolist()
# print(fur_color)
#
# red_count = 0
# gray_count = 0
# black_count = 0
#
# for color in fur_color:
#     if color == "Cinnamon":
#         red_count += 1
#     if color == "Gray":
#         gray_count += 1
#     if color == "Black":
#         black_count += 1
# data = [["red", red_count], ["gray", gray_count], ["black", black_count]]

# Method-2
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red = data[data["Primary Fur Color"] == "Cinnamon"]
print(type(red))
red_count = len(red)
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_data = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}

# df = pd.DataFrame(squirrel_data)
# df.to_csv("squirrel_count.csv")



