import wtforms
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Email, DataRequired, Length
from flask_wtf import FlaskForm


class LoginForm(wtforms.Form):
    username = wtforms.StringField()
    password = wtforms.PasswordField()
    checkbox = wtforms.Field()

class SearchForm(FlaskForm):
    recipe_category = SelectField('Category:', choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Other', 'Other')], validators=[DataRequired()])
    search_input = StringField('Ingredients:', validators=[DataRequired()])
    submit = SubmitField('Search')