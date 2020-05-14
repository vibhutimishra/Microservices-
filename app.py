from flask import Flask,jsonify
import requests

import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.environ.get('MYAPP_NAME', 'MyApp')
    print(name)
    r={
    "Brand": "BIOTRONIC",
    "Longevity": "5 years",


    "Weight": "21.5 grams",

    "Size": "4.57*4.45*0.75 cm",

    "Voltage": "2.8 V",


    "Average Projected Capacity" : "1.28 Ah"
    }
    # extracting data in json format
    return jsonify(r)
    # return '<br\><h3><center>Hello, Welcome to Dockerized Flask (' + name + ') !!!<center></h3>'

if __name__ == '__main__':
    port = int(os.environ.get('MYAPP_PORT', 5001))
    app.run(host='0.0.0.0', port=port)
