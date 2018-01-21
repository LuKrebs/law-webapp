from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flaskext.markdown import Markdown
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config.from_object("settings")
db = SQLAlchemy(app)

migrate = Migrate(app, db)

Markdown(app)

uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)

from home import views
from dashboard import views


def default_alt_image():
    return "Slompo de Lara & Barbosa da Cunha Advogados Associados"
app.jinja_env.globals["default_alt_image"] = default_alt_image

def formated_alt_image(image_name):
    image_name = image_name.replace(".jpg", "").replace(".png", "").replace("_", " ")
    return image_name
app.jinja_env.globals["formated_alt_image"] = formated_alt_image
