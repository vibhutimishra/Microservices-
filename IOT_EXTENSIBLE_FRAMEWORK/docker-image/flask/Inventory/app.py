from flask import Flask,jsonify
import requests

import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.environ.get('MYAPP_NAME', 'MyApp')
    print(name)
    URL = "https://04fd9ea0.ngrok.io/inventory"
    r = requests.get(url = URL) 
    # extracting data in json format 
    data = r.json() 
    return jsonify(data)
    # return '<br\><h3><center>Hello, Welcome to Dockerized Flask (' + name + ') !!!<center></h3>'

if __name__ == '__main__':
    port = int(os.environ.get('MYAPP_PORT', 5001))

    app.run(host='0.0.0.0', port=port)
