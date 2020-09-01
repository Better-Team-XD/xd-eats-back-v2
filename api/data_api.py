from flask import Blueprint
from flask import request
import service.data_service as data_service
from api.response_json import parse_json

data_api = Blueprint('data_api', __name__, url_prefix='/api/v1')


@data_api.route('/recipes', methods=['GET', 'POST'])
def recipes():
    try:
        if request.method == 'POST':
            content = request.get_json()
            return parse_json(message=data_service.add_recipe(content), status="SUCCESS")
        else:
            return parse_json(message="data loaded", status="SUCCESS", content=data_service.get_all_recipes())
    except Exception as e:
        return parse_json(message=e, status="ERROR")


@data_api.route('/ingredients')
def ingredients():
    try:
        return parse_json(message="data loaded", status="SUCCESS", content=data_service.get_all_ingredients())
    except Exception as e:
        return parse_json(message=e, status="ERROR")


@data_api.route('/matches', methods=['POST'])
def matches():
    try:
        content = request.get_json()
        return parse_json(message="data loaded", status="SUCCESS", content=data_service.get_all_matches(content))
    except Exception as e:
        return parse_json(message=e, status="ERROR")