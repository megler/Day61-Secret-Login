# secretLogin.py
#
# Python Bootcamp Day 61 - Secret Login
# Usage:
#      A Flask App using Flask-WTForms that leads to a fun surprise.
#      Day 61 Python Bootcamp
#
# Marceia Egler January 6, 2022


from flask import Flask, render_template, redirect, request, url_for
from forms import MyForm
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
import secrets

secret_key = secrets.token_hex(16)

app = Flask(__name__)
Bootstrap(app)
csrf = CSRFProtect(app)

app.config.update(TESTING=True, SECRET_KEY=secret_key)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/denied")
def denied():
    return render_template("denied.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "POST":
        if (
            form.validate()
            and form.email.data == "admin@email.com"
            and form.password.data == "12345678"
        ):
            return redirect("/success")
        else:
            return redirect("/denied")

    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
