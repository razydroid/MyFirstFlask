from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/hari/PycharmProjects/MyFirstProject/database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:\\account-verification-flask\\src\\example.db'
# sqlite:///absolute path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
# app.config['SECRET_KEY'] = 'meow'
app.config['SQLALCHEMY_DEBUG'] = 'True'

app.secret_key = "development"