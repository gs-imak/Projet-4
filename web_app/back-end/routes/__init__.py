from flask import Blueprint

# Import individual route blueprints
from .auth_routes import bp as auth_bp
from .es_routes import bp as es_bp
from .hadoop_routes import bp as hadoop_bp

# Create a list of blueprints for easy registration
blueprints = [auth_bp, es_bp, hadoop_bp]
