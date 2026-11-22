from flask import Blueprint, request, jsonify
from config.db import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():

    data = request.json

    db.users.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    })

    return jsonify({
        "message": "User Registered Successfully"
    })


@auth.route("/login", methods=["POST"])
def login():

    data = request.json

    user = db.users.find_one({
        "email": data["email"]
    })

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    if user["password"] != data["password"]:
        return jsonify({
            "message": "Invalid password"
        }), 401

    return jsonify({
        "message": "Login Successful"
    })