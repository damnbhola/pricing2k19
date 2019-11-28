import os
from flask import Flask, render_template, session
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


@app.route('/')
def home():
    try:
        if session["email"]:
            return render_template("users/home.html")
        else:
            raise KeyError
    except KeyError:
        return render_template('home.html')


@app.route('/<string:anything>')
def post(anything):
    if anything != "stores" or "alerts" or "users":
        return render_template("404.html", message=f"Page with ID: /{anything} not found!")


app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix="/users")
