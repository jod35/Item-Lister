from flask import Flask
from item.config import DevConfig
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config.from_object(DevConfig)
db=SQLAlchemy(app)

from item import routes