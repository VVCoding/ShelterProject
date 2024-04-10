import json


f1 = open("data/ShelterData.csv", "r")
lines = f1.readlines()

# Create the dictionary here
dictionary ={}
dict_yearly_avg = {} # Add a dictionary specifically for yearly average, maybe also add one for monthyl

for date in lines:
    data_shelter = date.split(',')

    dict_input = data_shelter[1:]
    dictionary[data_shelter[0]] = dict_input

f1.close()

#Save the json object to a file
f2 = open("data/ShelterData.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()