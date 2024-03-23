from os import environ
from flask import Flask
from utils.extensions import db, jwt
from routes import auth, template, post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth.auth_bp)
app.register_blueprint(template.template_bp)
app.register_blueprint(post.post_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
