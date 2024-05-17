from wtforms import StringField, Field, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    checkbox = Field('Remember me')
