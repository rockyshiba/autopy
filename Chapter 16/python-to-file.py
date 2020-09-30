import json

profile = {
    "name": "jane doe",
    "dob": "2000-11-11",
    "balance": 987654321
}

lucky = [9,8,7,6,5,4,3,2,1]

# dictionary to json file
with open("person.json", "w") as new_file:
    json.dump(profile, new_file)

# list to json file
with open("lucky.json", "w") as new_file:
    json.dump(lucky, new_file)