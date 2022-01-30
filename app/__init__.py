from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes      # imported at the bottom to avoid mutual references error due to circular imports
