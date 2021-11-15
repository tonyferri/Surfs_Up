import datetime as dt
import numpy as np
import pandas as pd

# dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import the dependencies that we need for Flask
from flask import Flask, jsonify

# set up our database engine for the Flask application, allows us to access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()

# reflect the database
Base.prepare(engine, reflect=True)

# create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# define our app for our Flask application; This will create a Flask application called "app."
app = Flask(__name__)
# All of your routes should go after the app = Flask(__name__) line of code. Otherwise, your code may not run properly.
# define the welcome route
@app.route("/")

# add the routing information for each of the other routes. 
# For this we'll create a function, and our return statement will have f-strings as a reference to all of the other routes. 
# This will ensure our investors know where to go to view the results of our data.

# First, create a function welcome() with a return statement
# def welcome():
#     return

# Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. 
# We'll use f-strings to display them for our investors:
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. 
# This convention signifies that this is version 1 of our application. 
# This line can be updated to support future versions of the app as well.

# The welcome route is now defined, so let's try to run our code. 
# You can run Flask applications by using the command below, but you'll need a web browser to view the results.

# Let's start by using the command line to navigate to your project folder. Then run your code: flask run

# Every time you create a new route, your code should be aligned to the left in order to avoid errors.
# To create the route, add the following code. Make sure that it's aligned all the way to the left.
@app.route("/api/v1.0/precipitation")

# create the precipitation() function
# def precipitation():
#     return

# First, we want to add the line of code that calculates the date one year ago from the most recent date in the database.
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    return

# Next, write a query to get the date and precipitation for the previous year.
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    precipitation = session.query(Measurement.date, Measurement.prcp).\
#       filter(Measurement.date >= prev_year).all()
#    return

# .\ is used to signify that we want our query to continue on the next line. You can use the combination of .\ to shorten the length of your query line so that it extends to the next line.

# create a dictionary with the date as the key and the precipitation as the value. To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file.

# JSON files are structured text files with attribute-value pairs and array data types. They have a variety of purposes, especially when downloading information from the internet through API calls. 
# We can also use JSON files for cleaning, filtering, sorting, and visualizing data, among many other tasks. 
# When we are done modifying that data, we can push the data back to a web interface, like Flask.

# We'll use jsonify() to format our results into a JSON structured file. When we run this code, we'll see what the JSON file structure looks like. Here's an example of what a JSON file might look like:
# {
# "city" : {
# "name" : "des moines",
#         "region" : "midwest"
# }

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# build the stations route. For this route we'll simply return a list of all the stations.  Begin by defining the route and route name
@app.route("/api/v1.0/stations")

# create a new function called stations()
# def stations():
#     return

# create a query that will allow us to get all of the stations in our database
# def stations():
#     results = session.query(Station.station).all()
#     return

# We want to start by unraveling our results into a one-dimensional array. To do this, we want to use the 'function np.ravel()', with results as our parameter.
# Next, we will convert our unraveled results into a list. 
# To convert the results to a list, we will need to use the list function, which is list(), and then convert that array into a list. 
# Then we'll jsonify the list and return it as JSON.
# to return our list as JSON, we need to add stations=stations
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# build the temperature route
@app.route("/api/v1.0/tobs")

# create a function called temp_monthly()
# def temp_monthly():
#     return

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# minimum, average, and maximum temperatures; this route is different from the previous ones in that we will have to provide both a starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Next, create a function called stats() to put our code in.
# def stats():
#      return

# We need to add parameters to our stats()function: a start parameter and an end parameter. For now, set them both to None.
# def stats(start=None, end=None):
#      return

# With the function declared, we can now create a query to select the minimum, average, and maximum temperatures from our SQLite database. We'll start by just creating a list called sel, with the following code:
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

# Since we need to determine the starting and ending date, add an if-not statement to our code. This will help us accomplish a few things. 
# We'll need to query our database using the list that we just made. 
# Then, we'll unravel the results into a one-dimensional array and convert them to a list. 
# Finally, we will jsonify our results and return them.

# In the following code, take note of the asterisk in the query next to the sel list. 
# # Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures.
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

#     if not end:
#         results = session.query(*sel).\
#             filter(Measurement.date >= start).all()
#         temps = list(np.ravel(results))
#         return jsonify(temps=temps)

# Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. 
# We'll use the sel list, which is simply the data points we need to collect. 
# Let's create our next query, which will get our statistics data.
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

