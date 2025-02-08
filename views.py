from main import app
from flask import render_template
from flask import jsonify
import requests


@app.route("/")
def homepage():
    api = "https://api.deezer.com/album/"
    informaçoe = requests.get(api)
    info = informaçoe.json()




    return render_template("index.html",info=info)