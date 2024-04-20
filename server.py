from flask import Flask
from flask import request
from flask import render_template
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

    return render_template("date.html", date=currDate)

app.run(debug=True, port =  5500)

# Add a grid for svgs in bootstrap