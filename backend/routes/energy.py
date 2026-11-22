from flask import Blueprint, request, jsonify
from config.db import db

energy = Blueprint("energy", __name__)

@energy.route("/consumption", methods=["POST"])
def consumption():

    data = request.json

    if (
        not data.get("temperature") or
        not data.get("buildingSize") or
        not data.get("unitsConsumed") or
        not data.get("renewableUsage")
    ):
        return jsonify({
            "message": "All fields are required"
        }), 400

    db.consumption.insert_one({
        "temperature": data["temperature"],
        "buildingSize": data["buildingSize"],
        "unitsConsumed": data["unitsConsumed"],
        "renewableUsage": data["renewableUsage"]
    })

    return jsonify({
        "message": "Consumption Data Saved Successfully"
    })