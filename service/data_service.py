from db.categories import categories
import db.repository as repository


def _parse_id(document):
    document["_id"] = str(document["_id"])
    return document


def add_recipe(data):
    if type(data) is not dict:
        raise ValueError("data format is incorrect")

    if len(data) != 5:
        raise ValueError("JSON format is incorrect")

    if "name" not in data or type(data["name"]) is not str:
        raise ValueError("name field is incorrect")

    if "category" not in data or data["category"] not in categories:
        raise ValueError("category is incorrect")

    if "ingredients" not in data or type(data["ingredients"]) is not list or len(data["ingredients"]) == 0:
        raise ValueError("ingredients are incorrect")

    if "url" not in data or type(data["url"]) is not str:
        raise ValueError("url field is incorrect")

    if "imageUrl" not in data or type(data["imageUrl"]) is not str:
        raise ValueError("imageUrl field is incorrect")

    return repository.insert_recipe(data)


def get_all_recipes():
    return list(map(lambda doc: _parse_id(doc), repository.find_all_recipes()))


def get_all_ingredients():
    return list(map(lambda doc: _parse_id(doc), repository.find_all_ingredients()))


def get_all_matches(data):
    if type(data) is not dict:
        raise ValueError("data format is incorrect")

    if len(data) != 2:
        raise ValueError("JSON format is incorrect")

    if "ingredients" not in data or type(data["ingredients"]) is not list:
        raise ValueError("ingredients field is incorrect")

    if "category" not in data or data["category"] not in categories:
        raise ValueError("ingredients field is incorrect")

    return repository.find_all_matches(data["ingredients"], data["category"])
