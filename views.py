from main import app
from flask import render_template
from flask import jsonify, request
import requests


@app.route("/")
def homepage():
    get = request.args.get("q")
    
    params ={
        "q" : get,
        "index": 0,
        "limit": 2,
        "output": "json"
    }
    api = "https://api.deezer.com/search/artist"
    response = requests.get ('api', params = params)



    return jsonify(response.json())