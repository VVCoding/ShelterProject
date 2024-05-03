from imaplib import Int2AP
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask
import json



def getYears():
    f = open("data/ShelterData.json", "r")
    data = json.load(f)
    f.close()
    
    years = []
    for i in range(1,13):
        years.append(list(data.keys())[-i])
    
    return years

def getData():
    f = open("data/ShelterData.json", "r")
    data = json.load(f)
    f.close()
    
    ind = []
    for i in range(1,13):
        ind.append(data[(list(data.keys())[-i])][2])
    
    return ind

fig, ax = plt.subplots()
xpoints = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
ypoints = np.array([50716.9,54487.5, 57223, 58781, 59474.9, 60023.4, 59504.8, 56044, 47974.4, 51686.8, 80087.9, 78978.5])
plt.plot(xpoints, ypoints)

plt.ylabel("Individuals in Shelters ")
plt.xlabel("Years ")
       
image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'templates/line_graph.svg'

fig.savefig(image_name, format=image_format, dpi=1200)