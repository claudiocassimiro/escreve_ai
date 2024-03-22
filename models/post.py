# models.py
from app import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    theme = db.Column(db.String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    
    def json(self):
        return { "id": self.id, "theme": self.theme, "content": self.content }
    
    def list_all(self): 
        return self.query.all()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()