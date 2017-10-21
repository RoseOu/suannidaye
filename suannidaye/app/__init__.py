# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)

config_name = 'default'
app.config.from_object(config[config_name])
config[config_name].init_app(app)


db = SQLAlchemy(app)


# admin site
from . import suan



