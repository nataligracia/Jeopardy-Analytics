#Flask & dependencies modules
from flask import Flask, jsonify, render_template
import pandas as pd
from sqlalchemy import create_engine

#SQL Use Tool
engine = create_engine("sqlite:///mappingmambas.sqlite")

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
#Flask Routes
################

#List all available api routes
@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/championshipdata")
def championshipdata():

    championshipdata = pd.read_sql("select * from championships",engine)
    
    championshipjson = championshipdata.to_dict(orient="records")

    return jsonify(championshipjson)

@app.route("/championships")
def championships():
    return render_template("whatis.html")

@app.route("/bubblechart")
def bubblechart():
    return render_template("tableau.html")

@app.route("/bubblechart")
def bubblechart():
    return render_template("mlresearch.html")

@app.route("/bubblechart")
def bubblechart():
    return render_template("originaldata.html")

@app.route("/bubblechart")
def bubblechart():
    return render_template("editeddata.html")

#Define main behavior
if __name__ == "__main__":
    app.run()