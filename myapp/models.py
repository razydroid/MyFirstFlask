from .settings import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

# db = SQLAlchemy(app)

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def json(self):
        return {
            'email' : self.email,
            'password' : self.password,
            'firstname' : self.firstname,
            'lastname': self.lastname
        }

    def __init__(self,firstname,lastname, email, password):

        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        # self.password = generate_password_hash(password)
        self.encrypt_password(password)

    def find_all_users(self):
        return [User.json(user) for user in User.query.all()]

    def find_user_by_username(_email):
        return User.json(User.query.filter_by(email=_email).first())

    def register_user(_email,_password):
        new_user = User(email=_email,password=_password)
        db.session.add(new_user)
        db.session.commit()

    def encrypt_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)