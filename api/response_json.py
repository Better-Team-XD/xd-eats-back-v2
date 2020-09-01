from flask import jsonify


def parse_json(status=None, message=None, content=None):
    return jsonify({"status": status, "message": str(message), "content": content})
