import matplotlib.pylab as plt
import matplotlib.dates as mdates
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import datetime as dt
import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float, Text, Date
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine("sqlite:///hawaii.sqlite", echo = False)
conn = engine.connect()
station_df = pd.DataFrame(conn.execute('SELECT station FROM stations').fetchall())
station_df.columns = ['station']
_ = conn.execute('SELECT date, station, tobs FROM measurements \
                  WHERE date >= \'2016-08-23\' AND station == \'USC00519397\' \
                  GROUP BY date, station').fetchall()
temp_df = pd.DataFrame(_)
temp_df.columns = ['date', 'station', 'tobs']
temp_data = pd.read_sql('measurements', conn, parse_dates={'date': {'format': '%Y-%m-%d'}}, columns=['date', 'tobs'])

app = Flask(__name__)

@app.route('/')
def start():
    return (
        f"Options:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
        )

@app.route('/api/v1.0/precipitation')
def Precipitation():
    precipitation = temp_df[['date', 'tobs']]
    precipitation_table = []
    for i in range(precipitation.shape[0]):
        dic = {}
        dic['date'] = precipitation.date[i]
        dic['tobs'] = int(precipitation.tobs[i])
        precipitation_table.append(dic)
    return(jsonify(precipitation_table))

@app.route('/api/v1.0/stations')
def Station():
    return(jsonify(station_df.to_dict()))

@app.route('/api/v1.0/tobs')
def Temperature():
    temperature = temp_df[['tobs']]
    return(jsonify(emperature.to_dict()))

@app.route('/api/v1.0/<start>')
def show_start(start):
    def temp_range(start_date):
        df = temp_data[temp_data.date >= start_date]
        dic = {}
        dic['min'] = df.temp.min()
        dic['avg'] = df.temp.mean()
        dic['max'] = df.temp.max()
        return(dic)
    new_temps = temp_range(start)
    new = {}
    new['TMIN'] = float(new_temps['min'])
    new['TAVG'] = float(new_temps['avg'])
    new['TMAX'] = float(new_temps['max'])
    return(jsonify(new))

@app.route('/api/v1.0/<start>/<end>')
def show_start_end(start, end):
    def calc_temps(start_date, end_date):
        df = temp_data[(temp_data.date >= start_date) & (temp_data.date <= end_date)]
        dic = {}
        dic['min'] = df.tobs.min()
        dic['avg'] = df.tobs.mean()
        dic['max'] = df.tobs.max()
        return(dic)
    temps = calc_temps(start, end)
    di = {}
    di['TMIN'] = float(temps['min'])
    di['TAVG'] = float(temps['avg'])
    di['TMAX'] = float(temps['max'])
    return(jsonify(di))

if __name__ == '__main__':
    app.run(debug=True)