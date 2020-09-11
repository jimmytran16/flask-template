from flask import Flask #import flask

app = Flask(__name__) #initialize a Flask instance

from .routes.routes import * #import all of the routes
