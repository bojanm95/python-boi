from datetime import datetime

from flask import Flask, render_template, request

from . import app
from .models.user import User


@app.route("/", methods=["GET","POST"])
def home():
    if request.form:
        user = User(username=request.form.get("username"), email=request.form.get("email"))
        db.session.add(user)
        db.session.commit()
    users = User.query.all()
    return render_template("home.html", users = users)


@app.route("/about")
def about():
    return render_template("about.html")
    

@app.route("/contact")
def contact():
    return render_template("contact.html")
