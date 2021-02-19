from flask import Flask, render_template, jsonify, request 
import mysql.connector
import json

app = Flask(__name__)

conn = mysql.connector.connect( host='scrap_sql',
                                database='my_db',
                                user='root',
                                password='123',
                                )
sql_query = conn.cursor()

logging.basicConfig(filename = "flask_api.log", 
level= logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')



@app.route('/', methods=['GET'])
def welcome(): 
    return "Welcome to Maison Du Monde's API ! "  

@app.route('/api', methods=['GET'])
def api():
    sql_query.execute("""SELECT * FROM carpet, mirror WHERE carpet.id = mirror.id GROUP BY carpet.id""")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_carpet', methods=['GET'])
def api_carpet(): 

    sql_query.execute("SELECT * FROM carpet")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_mirror', methods=['GET'])
def api_mirror(): 

    sql_query.execute("SELECT * FROM Mirror")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_carpet_lowest_to_highest_price', methods=['GET', 'POST'])
def carpet_lowest_to_highest_price():

    #https://stackoverflow.com/questions/8887760/order-by-price-returns-a-weird-order-in-mysql

    sql_query.execute(f"SELECT * FROM carpet ORDER BY CAST(carpet_price AS DECIMAL(10,2)) ASC")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_carpet_highest_to_lowest_price', methods=['GET', 'POST'])
def carpet_highest_to_lowest_price():

    sql_query.execute(f"SELECT * FROM carpet ORDER BY CAST(carpet_price AS DECIMAL(10,2)) DESC")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_mirror_lowest_to_highest_price', methods=['GET', 'POST'])
def mirror_lowest_to_highest_price():

    sql_query.execute(f"SELECT * FROM mirror ORDER BY CAST(mirror_price AS DECIMAL(10,2)) ASC")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_mirror_highest_to_lowest_price', methods=['GET', 'POST'])
def mirrro_highest_to_lowest_price():

    sql_query.execute(f"SELECT * FROM mirror ORDER BY CAST(mirror_price AS DECIMAL(10,2)) DESC")
    output = sql_query.fetchall()
    return jsonify(output)

# URL A SAISIR == http://localhost:4050/api_carpet_price?name=carpet&price=200
@app.route('/api_carpet_price', methods=['GET', 'POST'])
def carpet_price():

    carpet_name = request.args.get('name')
    carpet_price = request.args.get('price')


    sql_query.execute(f"SELECT * FROM {carpet_name} WHERE carpet_price <= {carpet_price}")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_mirror_price', methods=['GET', 'POST'])
def mirror_price():
    mirror_name = request.args.get('name')
    mirror_price = request.args.get('price')

    sql_query.execute(f"SELECT * FROM {mirror_name} WHERE mirror_price <= {mirror_price}")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_carpet_texture', methods=['GET', 'POST'])
def type_carpet():
    carpet_desc = request.args.get('matiere')

    sql_query.execute(f'SELECT * FROM carpet WHERE carpet_description LIKE "%{carpet_desc}%" ')
    output = sql_query.fetchall()
    return jsonify(output)


@app.route('/api_mirror_type', methods=['GET', 'POST'])
def type_mirror():
    mirror_type = request.args.get('type')

    sql_query.execute(f'SELECT * FROM mirror WHERE mirror_description LIKE "%{mirror_type}%" ')
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_mirror_color', methods=['GET', 'POST'])
def color_mirror():
    mirror_color = request.args.get('color')

    sql_query.execute(f'SELECT * FROM mirror WHERE mirror_description LIKE "%{mirror_color}%" ')
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/href', methods=['GET'])
def links():
    href = ['http://localhost:4050/', 'http://localhost:4050/api', 'http://localhost:4050/api_carpet','http://localhost:4050/api_mirror','http://localhost:4050/api_carpet_lowest_to_highest_price','http://localhost:4050/api_mirror_lowest_to_highest_price', 'http://localhost:4050/api_carpet_highest_to_lowest_price', 'http://localhost:4050/api_mirror_highest_to_lowest_price', 'http://localhost:4050/api_carpet_price?name=carpet&price=', 'http://localhost:4050/api_mirror_price?name=mirror&price=', 'http://localhost:4050/api_carpet_texture?matiere=', 'http://localhost:4050/api_mirror_type?type=', 'http://localhost:4050/api_mirror_color?color=']

    return jsonify(href)

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3050, debug = True)