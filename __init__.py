from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flaskext.markdown import Markdown


app = Flask(__name__)
app.config.from_object("settings")
db = SQLAlchemy(app)

migrate = Migrate(app, db)

Markdown(app)

from home import views
from dashboard import views


def default_alt_image():
    return "Slompo de Lara & Barbosa da Cunha Advogados Associados"
app.jinja_env.globals["default_alt_image"] = default_alt_image
