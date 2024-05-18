import wtforms
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo, ValidationError
from flask_wtf import FlaskForm
from apps.models import AccountDimension


class LoginForm(wtforms.Form):
    username = wtforms.StringField()
    password = wtforms.PasswordField()
    checkbox = wtforms.Field()

class SearchForm(FlaskForm):
    recipe_category = SelectField('Category:', choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Other', 'Other')], validators=[DataRequired()])
    search_input = StringField('Ingredients:', validators=[DataRequired()])
    submit = SubmitField('Search')


class LoginForm(wtforms.Form):
    username = wtforms.StringField('username', validators=[DataRequired()])
    password = wtforms.PasswordField('password', validators=[DataRequired()])


class RegistrationForm(wtforms.Form):
    username = wtforms.StringField('username', validators=[DataRequired()])
    email = wtforms.StringField('email', validators=[Email()])
    password = wtforms.PasswordField('password', validators=[DataRequired()])
    confirmPassword = wtforms.PasswordField(validators=[EqualTo('password')])

    def validate_username(self, username):
        user = AccountDimension.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different one.')

    def validate_email(self, email):
        user = AccountDimension.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use. Please choose a different one or login.')
