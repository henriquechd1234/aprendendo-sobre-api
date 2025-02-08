from main import app
from flask import render_template
import requests

informaçoe = requests.get("https://api.deezer.com/version/service/id/method/?parameters")
informaçoe = informaçoe.json()

@app.route("/")
def homepage():
    return render_template("index.html",informaçoe=informaçoe )