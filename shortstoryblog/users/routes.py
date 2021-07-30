from flask import Blueprint, render_template, url_for, flash, redirect
from shortstoryblog.users.forms import RegistrationForm, LoginForm

users = Blueprint("users", __name__)


@users.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!", "success")
        return redirect(url_for("main.home"))
    return render_template("register.html", title="Register", form=form)
