from flask import Flask, render_template, jsonify, request
from postgres import *
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

#https://flask-cors.readthedocs.io/en/latest/
#import mysql.connector
import logging
from mail_dbb import send_email

app = Flask(__name__)

print("connexion")


host = os.environ["host"]
dbname = os.environ["db"]
#user = os.environ["user"]
#password = os.environ["pw"]
#sslmode = "require" 

conn_string = "host={0} dbname={1}".format(host, dbname)
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

@app.route('/', methods=['GET'])
def welcome(): 
    return render_template("index.html")

@app.route('/', methods=['POST'])
def retrieve_mail():
    try:
        mail_user = request.form.get('user_mail')
        print(mail_user)

        #conn.execute("SELECT * FROM carpet ORDER BY carpet_date DESC LIMIT 5")

        send_email("hello", mail_user)
        return render_template("index.html")
        #return render_template("sucess.html")
    except Exception as e:
        print ("error is %s" %e)
        #return render_template("fail.html")


if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3050, debug = True)
    

     
    
    