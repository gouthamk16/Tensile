from app import app, store
from flask import request, jsonify
from models import Test

# get all details
@app.route("/api/test", methods=["GET"])
def get_friends():
    get_result = store.to_json()
    return jsonify(get_result)

@app.route("/api/test", methods=["POST"])
def add_friend():
    data = request.get_json()
    store.from_json(data)
    store.save("data.json")
    return store.to_json()