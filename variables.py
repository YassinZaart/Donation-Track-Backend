from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from donation_track_backend import config

app = Flask(__name__)
api = Api(app)
app.config[config.sql_alchemy_uri] = config.db_location
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)