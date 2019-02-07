from flask import Flask, render_template, request

from env.models.user import User

from env.db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:postgres@localhost:5433/flaskmovie"
db.init_app(app)


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
