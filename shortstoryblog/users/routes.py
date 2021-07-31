from flask import Blueprint, render_template, url_for, flash, redirect
from shortstoryblog.users.forms import RegistrationForm, LoginForm
from shortstoryblog import db, bcrypt
from shortstoryblog.models import User, Post

users = Blueprint("users", __name__)


@users.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Your Acccount is created!", "success")
        return redirect(url_for("main.home"))
    return render_template("register.html", title="Register", form=form)
