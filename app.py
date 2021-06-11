#Flask & dependencies modules
from flask import Flask, jsonify, render_template, request, redirect
import pymongo
from flask_pymongo import PyMongo
import pandas as pd
import json

# from sqlalchemy import create_engine

# #SQL Use Tool
# engine = create_engine("sqlite:///mappingmambas.sqlite")

#Reflect database into new model
 # Base = automap_base()

#Reflect the tables and pass in the engine
# Base.prepare(engine, reflect=True)

#Label tables from classes
# Championships = Base.classes.championships

#Create a session and bind it to the engine
# session = Session(engine)

################
#Flask Setup
################

#Create an app for Flask setup
app = Flask(__name__)



################
#Database Setup
################
mongo = pymongo.MongoClient("mongodb+srv://jeopardy:jeopardy@jeopardy.n13te.mongodb.net/jeopardy?retryWrites=true&w=majority")

db = mongo['jeopardy']

################
#Flask Routes
################

#List all available api routes
@app.route("/")
def welcome():
    return render_template("index.html")

# @app.route("/championshipdata")
# def championshipdata():

#     championshipdata = pd.read_sql("select * from championships",engine)
    
#     championshipjson = championshipdata.to_dict(orient="records")

#     return jsonify(championshipjson)

@app.route("/projectoverview")
def projectoverview():
    return render_template("whatis.html")

@app.route("/tableau")
def tableau():
    return render_template("tableau.html")

@app.route("/mlresearch")
def mlresearch():
    return render_template("mlresearch.html")

@app.route("/originaldata")
def originaldata():
    return render_template("originaldata.html")

@app.route("/editeddata")
def editeddata():
    return render_template("editeddata.html")

#Define main behavior
if __name__ == "__main__":
    app.run()