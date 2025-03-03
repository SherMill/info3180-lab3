from flask import Flask
"""Adding other necessary imports"""
from flask_mail import Mail
from .config import Config

app = Flask(__name__)

"""Importing and Initalising Flask application and mail"""

app.config.from_object(Config)
mail = Mail(app)
from app import views