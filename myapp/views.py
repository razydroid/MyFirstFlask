from flask import Flask, request, session, redirect, url_for, render_template, flash
from .forms import SignupForm, LoginForm
from .models import db, User
from .settings import app
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Secret key for csrf forgery protection
# app.secret_key = "development"

# database confiuration & details

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Projects\\Flask\\database.db'
# app.config['SQLALCHEMY_DEBUG'] = 'True'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

# Initialize the database
# db.init_app(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if 'email' in session:
        return redirect(url_for('home'))
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('register.html', form=form)
        else:
            userStatus = User.find_user_by_email(form.email.data)
            if userStatus == True:
                newuser = User(form.firstname.data,form.lastname.data,form.email.data,form.password.data)
                db.session.add(newuser)
                db.session.commit()
                session['email'] = newuser.email
                flash("You have successfully Registered.")
                return redirect(url_for('login'))
            else:
                flash("User with the same email address already exists.")
                return render_template('register.html', form=form)

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
                login_user(user)
                session['email'] = user.email
                return redirect(url_for('home'))
            else:
                flash("Invalid Credentials...")
                return redirect(url_for('login'))
    else:
        return render_template('login.html', form=form)

@app.route("/profile")
@login_required
def profile():
# if 'email' not in session:
#     return redirect(url_for('login'))
# else:
    user = User.get_user_by_email(session['email']).values()
    # print(user.get('firstname') + ' '+ user.get('lastname'))
    # firstname = user.get('firstname')
    # lastname = user.get('lastname')
    return render_template('profile.html',user=user)

@app.route("/home")
@login_required
def home():
    # if 'email' not in session:
    #     return redirect(url_for('login'))
    # else:
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
@login_required
def logout():
    # session.pop("email",None)
    logout_user()
    return redirect(url_for('index'))
