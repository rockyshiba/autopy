import json

'''
Dictionaries are a type in Python.
'''

# strings
fruit = 'apple'
print(type(fruit))
# <class 'str'>

# int
winner = 14
print(type(winner))
# <class 'int'>

# lists
laundry = [1, 'shirt', 'pants', ['a', 'b', 'c'], winner]
print(type(laundry))
# <class 'list'>

# dictionary
pet = {
    'type': 'dog',
    'breed': 'shiba',
    'name': 'rocky',
    133: 'something'
}

pet2 = {
    133: 'something',
    'type': 'dog',
    'breed': 'shiba',
    "name": 'rocky'
}
print(type(pet))
# <class 'dict'>

'''
Dictionaries are like lists. They can hold data on multiple levels.
Dictionaries are different than lists by not ordering the data within a dictionary.
'''
print("Second item of the laundry list: " + laundry[1])
# print("First item of the pet dictionary: " + pet[0]) # this results in an error because information in dictionary is not referenced by index but by key

'''
Retrieving information by an int is possible in a python dictionary only if it is a key
'''
print("pet[133] refers to: " + pet[133])

'''
Information in python is stored in key:value pairs
'''
print(pet['type'] + pet['breed'] + pet['name'])

'''
Remember, python dictionaries are unordered. This also means the keys can be defined in any order in a dictionary while still considered the same as another dictionary object with the same keys in different order. 
'''
print(pet == pet2) # This will evaluate to true, even though the keys are in different order

'''
Why use a dictionary over a list?
'''
# When information is defined
# When information is large
# Information is multidimensional

'''
Why use a list over a dictionary
'''
# When information is simple
# When information is ordered
# Information has fewer dimensions
# Loop over information

'''
Example: JSON file
'''
with open('maps.json') as map_file:
    data = json.load(map_file)
    for marker in data["markers"]:
        print(marker['name'])
