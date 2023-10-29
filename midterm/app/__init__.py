"""Flask application initialization"""
import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Check if the SQLite database file exists
if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite:///'):
    db_path = os.path.join(basedir, app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))

    # Print the contents of the folder where the lux.sqlite file is expected to be located
    folder_path = os.path.dirname(db_path)

    if not os.path.isfile(db_path):
        print(f"\nError: The database file '{db_path}'\
        does not exist. Please make sure\
        it exists before running the application.", file=sys.stderr)
        sys.exit(1)

from app import routes
# from app import models
