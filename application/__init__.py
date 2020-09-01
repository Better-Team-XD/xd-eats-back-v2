from flask import Flask

from api.data_api import data_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(data_api)

    return app
