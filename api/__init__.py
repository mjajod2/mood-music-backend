from flask import Flask, request, jsonify, Blueprint
import os
from .mood_to_genre import moodToGenre

from flask_cors import CORS

'''
This function creates the app and registers the blueprint
'''
def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.register_blueprint(moodToGenre, url_prefix='/moodToGenre')
    return app