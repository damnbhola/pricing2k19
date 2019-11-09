from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user import User, UserErrors
from models.user import requires_login

user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/index")
def index():
    return redirect(url_for(".login_user"))


@user_blueprint.route('/<string:anything>')
def page(anything):
    if anything:
        return render_template("404.html", message=f"Post with ID: /users/{anything} not found!")


@user_blueprint.route("/")
@user_blueprint.route("/home")
@requires_login
def home():
    try:
        if session['email']:
            return render_template("users/home.html")
        else:
            raise KeyError
    except KeyError:
        return redirect(url_for("users.login_user"))


@user_blueprint.route("/login", methods=["GET", "POST"])
def login_user():
    try:
        if session["email"]:
            flash("You are already Logged In!", "warning")
            return redirect(url_for("users.home"))
        else:
            raise KeyError
    except KeyError:
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            try:
                if User.is_login_valid(email, password):
                    session["email"] = email
                    flash(f"Welcome Back {email}!", "success")
                    return redirect(url_for("alerts.index"))
            except UserErrors.UserError as e:
                flash(f"{e.message}", "danger")
                return redirect(url_for("users.login_user"))
        return render_template("users/login.html")


@user_blueprint.route("/register", methods=["GET", "POST"])
def register_user():
    try:
        if session["email"]:
            flash("You are already Logged In!", "warning")
            return redirect(url_for("users.home"))
        else:
            raise KeyError
    except KeyError:
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]

            try:
                User.register_user(name, email, password)
                session["email"] = email
                flash(f"Registration Successful!", "success")
                return redirect(url_for("alerts.index"))
            except UserErrors.UserError as e:
                flash(f"{e.message}", "danger")
                if e.message == "The  e-mail you used already exists!":
                    return redirect(url_for("users.login_user"))
                return redirect(url_for("users.register_user"))

        return render_template("users/register.html")


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    flash("logout successful!", "success")
    return redirect(url_for('home'))
