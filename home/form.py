from flask_wtf import Form
from wtforms import validators, StringField, TextAreaField
from flask_wtf.file import FileField, FileAllowed

from home.models import History, Area

class HistoryForm(Form):
    short_description = TextAreaField('Descrição Curta', validators=[validators.Required()])
    complete_description = TextAreaField('Descrição Completa', validators=[validators.Required()])
    office_name = StringField('Nome', validators=[validators.Required()])

class AreaForm(Form):
    name = StringField('Área', validators=[validators.Required()])
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only')
    ])
