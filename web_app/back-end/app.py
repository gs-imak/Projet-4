from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from routes import blueprints  # Import dynamically managed blueprints

def create_app():
    """Factory to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize JWT for authentication
    jwt = JWTManager(app)

    # Dynamically register blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app

if __name__ == '__main__':
    # Debug mode for local development
    app = create_app()
    app.run(debug=True)
