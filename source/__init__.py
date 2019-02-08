import flask
from .db import db
app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:postgres@localhost:5433/flaskmovie"
db.init_app(app)