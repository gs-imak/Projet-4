from flask import jsonify

def handle_error(e):
    response = {
        "error": str(e),
        "message": "An error occurred. Please try again later."
    }
    return jsonify(response), 500
