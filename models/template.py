# models.py
from app import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Template(db.Model):
    __tablename__ = "templates"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    
    def json(self):
        return { "id": self.id, "content": self.content }
    
    def list_all(self): 
        return self.query.all()
    
    @classmethod
    def get_template_by_user_id(cls, user_id):
        templates = cls.query.filter_by(user_id=user_id).all()
        templates_json = [template.json() for template in templates] 

        return templates_json

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()