from flask import Flask, request, session, redirect, url_for, render_template, flash
from .forms import SignupForm, LoginForm
from .models import db, User
from .settings import app

# Secret key for csrf forgery protection
# app.secret_key = "development"

# database confiuration & details

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Projects\\Flask\\database.db'
# app.config['SQLALCHEMY_DEBUG'] = 'True'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

# Initialize the database
# db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('register.html', form=form)
        else:
            newuser = User(form.firstname.data,form.lastname.data,form.email.data,form.password.data)
            db.session.add(newuser)
            db.session.commit()
            session['email'] = newuser.email
            return redirect(url_for('profile'))
    else:
        return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template('login.html', form=form)
        else:
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = user.email
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
    else:
        return render_template('login.html', form=form)

@app.route("/profile")
def profile():
    return render_template('profile.html')


@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/add_post")
def add_post():
    return "TODO"


@app.route("/like_post/<post_id>")
def like_post(post_id):
    return "TODO"


# @app.route("/profile/<username>")
# def profile(username):
#     return "TODO"
#

@app.route("/logout")
def logout():
    return "TODO"