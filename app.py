import os

from flask import Flask, render_template, redirect, request
from models.database import db

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config.update(SECRET_KEY=os.urandom(64),
                ENV='development')

db.init_app(app)

from routes import *