import os


class Config(object):   # extensible config settings - can be subclassed later
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'placeholder-key'  # used by Flask-WTF to prevent CSRF
