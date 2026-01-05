
import json

with open('catalog.json', encoding="utf8") as file:
    data_dict = json.load(file)

    for item in data_dict:
        print(item["CodeName"])

#Can parse out all the names of codename and prints to console