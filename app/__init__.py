from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   # Flask-Migrate- extension to make updates to DB as app grows and needs changes

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)      # Flask-Migrate: wrapper over Alembic migration framework for SQLAlchemy

from app import routes, models      # imported at the bottom to avoid mutual references error due to circular imports
