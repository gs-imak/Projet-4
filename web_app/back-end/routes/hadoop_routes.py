from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.hadoop_service import query_hadoop

bp = Blueprint('hadoop', __name__)

@bp.route('/query', methods=['POST'])
@jwt_required()
def query_file():
    file_path = request.json.get("file_path")
    results = query_hadoop(file_path)
    return jsonify(results)
