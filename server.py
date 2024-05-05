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

@app.route('/map')
def map(): 
    f = open("data/LocationData.json", "r")
    data = json.load(f)
    f.close() 
    
    locationDict = {}
    
    for borough in data.keys():
        locationDict[borough] = int(data[borough])
    
    boroughs = list(data.keys())[:5]
      
    return render_template("map.html", locationDict = locationDict, boroughs= boroughs)


@app.route("/date/<currDate>")
def date(currDate):
    f = open("data/ShelterData.json", "r")
    data = json.load(f)
    f.close()

    close = []
    
    runbool = False
    listData=[]
    
    dates = list(data.keys())[1:]
    if dateToDate(currDate) in dates:
        runbool = True
        for elt in data[dateToDate(currDate)]:
            listData.append(int(elt))
    else:
        runbool = False
    
    yearAvg = {}
    for i in range(1,13):
        yearAvg[list(data.keys())[-i]] = []
        for elt in data[list(data.keys())[-i]]:
            yearAvg[list(data.keys())[-i]].append(int(elt))
        
    year_list = ["2013", "2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"]
    for year in year_list:
        if runbool == True and year in dateToDate(currDate):
            currYear = year 
        else:
            currYear = "2024"
            
    if runbool == True:  
        for index in range(0,10):
            if int(listData[index])/int(yearAvg[currYear][index]) <= 0.96:
                close.append("significantly lower than") 
            elif int(listData[index])/int(yearAvg[currYear][index]) <= 0.98:
                close.append("a little lower than")
            elif int(listData[index])/int(yearAvg[currYear][index]) <= 1.000:
                close.append("about the same as")
            elif int(listData[index])/int(yearAvg[currYear][index]) <= 1.005:
                close.append("a little higher than")
            elif int(listData[index])/int(yearAvg[currYear][index]) >= 1.005:
                close.append("significantly higher than")
    


    return render_template("date.html", date=currDate, numDate = dateToDate(currDate),runbool = runbool, listData=listData, yearAvg = yearAvg, currYear = currYear, close = close)


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
        if day in date and count == 0:
            datestr = datestr + "/"+ day.replace(" ","")
            count+=1
            
    year_list = ["2013", "2014","2015", "2016","2017", "2018","2019", "2020","2021", "2022","2023", "2024"]
    for year in year_list:
        if year in date:
            datestr = datestr + "/"+year
        else:
            datestr = date
    
    return datestr

app.run(debug=True, port =  5500)


# Add CSS for Navbar and anything else
# Make Video
# DONE

