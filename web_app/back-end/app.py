from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config
from routes import blueprints  # Import dynamically managed blueprints
from models import User  # Assuming you have a User model for database interactions
from werkzeug.security import generate_password_hash

def create_app():
    """Factory to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize JWT for authentication
    jwt = JWTManager(app)

    # Dynamically register blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    @app.route('/api/update-user', methods=['PUT'])
    @jwt_required()
    def update_user():
        """Endpoint for users to update their profile information."""
        data = request.get_json()
        user_id = get_jwt_identity()  # Get the current user's ID from the JWT

        # Retrieve the user from the database
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return jsonify({"message": "User not found"}), 404

        # Update user's name if provided
        if 'name' in data and data['name']:
            user.name = data['name']

        # Update user's password if provided
        if 'password' in data and data['password']:
            hashed_password = generate_password_hash(data['password'])
            user.password = hashed_password

        # Commit changes to the database
        try:
            user.save_to_db()  # Assuming you have a method to save the user
            return jsonify({"message": "User updated successfully"}), 200
        except Exception as e:
            return jsonify({"message": "An error occurred updating the user"}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
