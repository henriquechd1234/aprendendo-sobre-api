from main import app
from flask import render_template
import requests

informaçoe = requests.get("https://api.deezer.com/album/302127")
informaçoe = informaçoe.json()

@app.route("/")
def homepage():
    return render_template("index.html",informaçoe=informaçoe )