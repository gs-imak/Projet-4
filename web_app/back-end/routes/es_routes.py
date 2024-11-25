from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.elasticsearch_service import query_elasticsearch

bp = Blueprint('elasticsearch', __name__)

@bp.route('/search', methods=['POST'])
@jwt_required()
def search():
    query = request.json.get("query")
    results = query_elasticsearch(query)
    return jsonify(results)
