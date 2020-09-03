from flask import Flask
from flask_cors import CORS

from api.data_api import data_api


def create_app():
    app = Flask(__name__)
    CORS(app)
    cors = CORS(app, resources={
        r"/*": {
            "origins": "*"
        }
    })

    app.register_blueprint(data_api)

    return app
