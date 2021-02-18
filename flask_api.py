#from main import *
#rom file_db import *
from flask import Flask, render_template, jsonify 
import mysql.connector
import json

app = Flask(__name__)

conn = mysql.connector.connect( host='scrap_sql',
                                database='my_db',
                                user='root',
                                password='123',
                                )
sql_query = conn.cursor()

sql_query.execute("CREATE TABLE IF NOT EXISTS test (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(100) NOT NULL)")
conn.close()

@app.route('/')
def welcome(): 
    return "Welcome to Maison Du Monde's API ! "  

@app.route('/api')
def api():
    conn = mysql.connector.connect( host='scrap_sql',
                                database='my_db',
                                user='root',
                                password='123',
                                )
    sql_query = conn.cursor()
    sql_query.execute("""SELECT * FROM carpet, mirror WHERE carpet.id = mirror.id ORDER BY carpet.id""")
    output = sql_query.fetchall()
    return jsonify(output)


@app.route('/api_carpet')
def api_carpet(): 
    conn = mysql.connector.connect( host='scrap_sql',
                                database='my_db',
                                user='root',
                                password='123',
                                )
    sql_query = conn.cursor()
    sql_query.execute("SELECT * FROM carpet")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_mirror')
def api_mirror(): 
    conn = mysql.connector.connect( host='scrap_sql',
                                database='my_db',
                                user='root',
                                password='123',
                                )
    sql_query = conn.cursor()
    sql_query.execute("SELECT * FROM Mirror")
    output = sql_query.fetchall()
    return jsonify(output)





if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3050, debug = True)