import json


f1 = open("data/LocationData.csv", "r")
lines = f1.readlines()

# Create the dictionary here
dictionary ={}

for pair in lines:
    data_location = pair.split(',')

    individuals = data_location[1]
    dictionary[data_location[0]] = individuals

f1.close()

#Save the json object to a file
f2 = open("data/LocationData.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()