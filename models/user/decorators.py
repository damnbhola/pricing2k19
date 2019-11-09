import functools
from typing import Callable
from flask import flash, session, redirect, url_for, current_app


def requires_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if session["email"]:
                pass
            elif not session['email']:
                flash("You need to Log In to access this page.", "danger")
                return redirect(url_for("users.login_user"))
        except KeyError:
            flash("You need to Log In to access this page.", "danger")
            return redirect(url_for("users.login_user"))
        return f(*args, **kwargs)
    return decorated_function


def requires_admin(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if session["email"] != current_app.config.get('ADMIN', ''):
                print("You need to be admin to access this page.", "danger")
                return redirect(url_for("users.login_user"))
        except KeyError:
            flash("You need to Log In to access this page.", "danger")
            return redirect(url_for("users.login_user"))
        return f(*args, **kwargs)
    return decorated_function
