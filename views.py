from main import app
from flask import render_template
import requests


@app.route("/")
def homepage():
    api = "https://api.deezer.com/album/302127"
    informaçoe = requests.get(api)
    info = informaçoe.json()
    return render_template("index.html",info)