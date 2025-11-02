from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('config.Config')
    mongo = PyMongo(app)
    jwt = JWTManager(app)
    return app, mongo
