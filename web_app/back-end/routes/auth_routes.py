from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if username == "admin" and password == "password":  # Simplified check
        token = create_access_token(identity={"username": username})
        return jsonify(access_token=token)
    return jsonify({"msg": "Invalid credentials"}), 401
