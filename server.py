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
    return render_template("about.html")

@app.route("/date/<currDate>")
def date(currDate):

    return render_template("date.html", date=currDate, numDate = dateToDate(currDate))

def dateToDate(date):
    date = date.replace("%20","")
    datestr = ""
    month_dict = {"January":1, "February":2, "March":3, "Apr":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    for month in month_dict.keys():
        if month in date:
            datestr = datestr + str(month_dict[month])
    
    days_list = ["1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10 ","11 ","12 ","13 ","14 ","15 ","16 ","17 ","18 ","19 ","20 ","21 ","22 ","23 ","24 ","25 ","26 ","27 ","28 ","29 ","30 ","31 "]
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

# Add a grid for svgs in bootstrap