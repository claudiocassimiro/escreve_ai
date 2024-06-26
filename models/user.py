# models.py
from app import db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from .template import Template
from .post import Post

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    Templates = relationship(Template, backref="users")
    Posts = relationship(Post, backref="users")

    def json(self):
        return { "id": self.id, "username": self.username, "email": self.email, "password": self.password }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()