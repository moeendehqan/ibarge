from flask import Flask
from flask_cors import CORS
from app.Resource import api
from config import config

def create_app(environment='default'):
    app = Flask(__name__)
    CORS(app)
    api.init_app(app)
    return app



