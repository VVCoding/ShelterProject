from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime
import json


app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/index')
def index():    
    f = open("data/ShelterData.json", "r")
    data = json.load(f)
    f.close()
    
    years = []
    years.append(list(data.keys())[-1])
    years.append(list(data.keys())[-2])
    years.append(list(data.keys())[-3])
    years.append(list(data.keys())[-4])
    
    dates = []
    dates.append(list(data.keys())[1:-4])
    
    return render_template("index.html", years = years, dates = dates)


@app.route('/')
def home():
    f = open("data/ShelterData.json", "r")
    data = json.load(f)
    f.close()
    
    years = []
    for i in range(1,13):
        years.append(list(data.keys())[-i])
    
    dates = []
    dates.append(list(data.keys())[1:])
    
    all_dates = []
    for date in dates:
       all_dates.append(date) 
    
    return render_template("index.html", years = years, all_dates = all_dates)

@app.route('/about')
def about(): 
    f = open("data/ShelterData.json", "r")
    data = json.load(f)
    f.close()   
    return render_template("about.html")

@app.route("/date/<currDate>")
def date(currDate):
    f = open("data/ShelterData.json", "r")
    data = json.load(f)
    f.close()
    
    
    runbool = False
    
    dates = list(data.keys())[1:]
    if dateToDate(currDate) in dates:
        runbool = True
    else:
        runbool = False

    return render_template("date.html", date=currDate, numDate = dateToDate(currDate),runbool = runbool, totalAdultsInShelter = int(data[dateToDate(currDate)][0]), totalChildrenInShelter = int(data[dateToDate(currDate)][1]), totalIndividualsInShelter = int(data[dateToDate(currDate)][2]), singleAdultMenInShelter = int(data[dateToDate(currDate)][3]), singleAdultWomenInShelter = int(data[dateToDate(currDate)][4]), totalSingleAdultsInShelter = int(data[dateToDate(currDate)][5]), familiesWithChildrenInShelter = int(data[dateToDate(currDate)][6]), adultsInFamiliesWithChildrenInShelter = int(data[dateToDate(currDate)][7]), childrenInFamiliesWithChildrenInShelter = int(data[dateToDate(currDate)][8]), totalIndividualsInFamiliesWithChildrenInShelter=int(data[dateToDate(currDate)][9]))

def dateToDate(date):
    date = date.replace("%20","")
    datestr = ""
    month_dict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
    for month in month_dict.keys():
        if month in date:
            datestr = datestr + month_dict[month]
    
    days_list = ["01 ","02 ","03 ","04 ","05 ","06 ","07 ","08 ","09 ","10 ","11 ","12 ","13 ","14 ","15 ","16 ","17 ","18 ","19 ","20 ","21 ","22 ","23 ","24 ","25 ","26 ","27 ","28 ","29 ","30 ","31 "]
    days_list.reverse()
    count = 0
    for day in days_list:
        if day in date and count ==0:
            datestr = datestr + "/"+ day.replace(" ","")
            count+=1
            
    year_list = ["2013", "2014","2015", "2016","2017", "2018","2019", "2020","2021", "2022","2023", "2024"]
    for year in year_list:
        if year in date:
            datestr = datestr + "/"+year
    
    return datestr

app.run(debug=True, port =  5500)


# Use MatPlot Lib for the rest of the graphs
# Round Decimals
# Add CSS for Navbar and anything else
# Make Video
# DONE

"""Total Adults in Shelter",
        "Total Children in Shelter",
        "Total Individuals in Shelter",
        "Single Adult Men in Shelter",
        "Single Adult Women in Shelter",
        "Total Single Adults in Shelter",
        "Families with Children in Shelter",
        "Adults in Families with Children in Shelter",
        "Children in Families with Children in Shelter",
        "Total Individuals in Families with Children in Shelter",
        "Adult Families in Shelter",
        "Individuals in Adult Families in Shelter"""