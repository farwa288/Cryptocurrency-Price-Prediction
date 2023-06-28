from flask import Flask,render_template,request,jsonify
from utils import RegressionModel
import numpy as np
from flask_mysqldb import MySQL
import config

app = Flask(__name__)

############################## MYSQL CONFIGURATION STEP####################
# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "Shubham0306"
# app.config["MYSQL_DB"] = "db_pumpkeen_seeds"
# mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["GET","POST"])
def get_prediction():
    data = request.form
    
    coin_name = str(data["name"])
    high_value = eval(data["high"])
    low_value = eval(data["low"])
    open_value = eval(data["open"])
    volume_shared = eval(data["volume"])
    marketcap = eval(data["marketcap"])
    date_year = eval(data["date_year"])
    date_month = eval(data["date_month"])
    date_day = eval(data["date_day"])

    obj = RegressionModel (coin_name,high_value,low_value,open_value,volume_shared,marketcap,date_year,date_month,date_day)
    r = obj.get_predict()
    print(r)

    #### Adding Values Into Database ####
    # cursor = mysql.connection.cursor()
    # querry = "CREATE TABLE IF NOT EXISTS pumpkeen_seeds(Area varchar(30),Perimeter varchar(30),Major_Axis_Length varchar(30),Minor_Axis_Length varchar(30),Convex_Area varchar(30),Equiv_Diameter varchar(30),Eccentricity varchar(30),Solidity varchar(30),Extent varchar(30),Roundness varchar(30),Aspect_Ration varchar(30),Compactness varchar(30),Seed_class varchar(30))"
    # cursor.execute(querry)
    # cursor.execute("INSERT INTO pumpkeen_seeds(Area,Perimeter,Major_Axis_Length,Minor_Axis_Length,Convex_Area,Equiv_Diameter,Eccentricity,Solidity,Extent,Roundness,Aspect_Ration,Compactness,Seed_class) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Area,Perimeter,Major_Axis_Length,Minor_Axis_Length,Convex_Area,Equiv_Diameter,Eccentricity,Solidity,Extent,Roundness,Aspect_Ration,Compactness,r))
    
    # mysql.connection.commit()
    # cursor.close()

    return render_template("index1.html",r=r)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.port_number)