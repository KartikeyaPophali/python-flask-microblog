import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):   # extensible config settings - can be subclassed later
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'placeholder-key'  # used by Flask-WTF to prevent CSRF
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # if True, send a signal to the application when a DB change is made
