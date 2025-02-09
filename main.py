from flask import Flask
from flask import render_template
import requests
import json


app = Flask(__name__)

from views import * 
from server import *






if __name__ == "__main__":
    app.run()
