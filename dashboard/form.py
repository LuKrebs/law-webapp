from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

from dashboard.models import User

class LoginForm(Form):
    email = EmailField('Email', [
        validators.Required(),
        validators.length(min=4, max=25)
    ])
    password = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=4, max=80)
    ])
