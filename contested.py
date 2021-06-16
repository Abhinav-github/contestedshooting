from flask import Flask, jsonify, request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
import requests
from flask_marshmallow import Marshmallow

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
