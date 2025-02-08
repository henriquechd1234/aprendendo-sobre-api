from flask import Flask
from flask import render_template
import requests
import json


app = Flask(__name__)

from views import * 

informaçoe = requests.get("https://api.deezer.com/version/service/id/method/?parameters")



if __name__ == "__main__":
    app.run()
