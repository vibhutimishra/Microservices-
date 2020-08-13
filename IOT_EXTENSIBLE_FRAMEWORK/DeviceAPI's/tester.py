from flask import Flask,jsonify
import requests


app = Flask(__name__)

@app.route('/')
def hello():
    
    URL = "https://04fd9ea0.ngrok.io/inventory"
    r = requests.get(url = URL) 
    # extracting data in json format 
    data = r.json() 
    print(data)
    return jsonify(data)
    # return '<br\><h3><center>Hello, Welcome to Dockerized Flask (' + name + ') !!!<center></h3>'

if __name__ == '__main__':
    

    app.run(port=5005)