# json to python
import json

# json array to python list
with open('./numbers.json') as json_file:
    data = json.load(json_file)

    # json arrays are interpretted as lists
    print(data)

# json object to python dictionary
with open('./profile.json') as json_file:
    data = json.load(json_file)

    # json objects are interpretted as dictionaries
    print(data)