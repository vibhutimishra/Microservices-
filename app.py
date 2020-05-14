from flask import Flask,jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.environ.get('MYAPP_NAME', 'MyApp')
    print(name)
    r = {
        "Status": "Active",
        "Last Active":"23-02-2020",
        "Packet Error Rate": "3%",
        "Sensitivity ": "-123dB"
    }
    # extracting data in json format
    return jsonify(r)
    # return '<br\><h3><center>Hello, Welcome to Dockerized Flask (' + name + ') !!!<center></h3>'

if __name__ == '__main__':
    port = int(os.environ.get('MYAPP_PORT', 5002))

    app.run(host='0.0.0.0', port=port)
