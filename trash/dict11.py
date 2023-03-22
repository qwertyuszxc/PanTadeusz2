import json

with open("data.json") as file:
    data = json.load(file)
for data_item in data:
    for k,v in data_item.items():
        print(k,":",v)
