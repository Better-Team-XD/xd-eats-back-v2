from db.config import db


def insert_recipe(recipe):
    for ingredient in recipe["ingredients"]:
        if db.ingredients.count({"name": ingredient}) == 0:
            db.ingredients.insert_one({
                "name": ingredient
            })

    return db.recipes.insert_one(recipe).inserted_id


def find_all_recipes():
    return list(db.recipes.find({}))


def find_all_ingredients():
    return list(db.ingredients.find({}))


def find_all_matches(ingredient_list, category):
    return list(filter(lambda recipe: recipe["missing"] != len(recipe["ingredients"]), list(db.recipes.aggregate([
        {"$unset": "_id"},
        {"$match": {"category": category}},
        {"$addFields": {"missing": {"$size": {"$setDifference": ["$ingredients", ingredient_list]}}}},
        {"$sort": {"missing": 1}}
    ]))))
