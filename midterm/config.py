"""Application configuration"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """Configuration keys and their values"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'lux.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'midtermquiz'
    # list of all the ids
    OBJECT_IDS = []
