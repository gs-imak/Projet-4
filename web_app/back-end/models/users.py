
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def save_to_db(self):
        """Save user to the database."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, user_id):
        """Find user by ID."""
        return cls.query.filter_by(id=user_id).first()

    def verify_password(self, password):
        """Verify password against stored hash."""
        return check_password_hash(self.password, password)
