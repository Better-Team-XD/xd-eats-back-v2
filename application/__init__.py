from flask import Flask
from flask_cors import CORS

from api.data_api import data_api


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/v1/*": {"origins": "http://localhost:3000"}})

    app.register_blueprint(data_api)

    return app
