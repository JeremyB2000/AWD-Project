import wtforms
from wtforms.validators import Email, DataRequired, Length


class LoginForm(wtforms.Form):
    username = wtforms.StringField('username', validators=[DataRequired()])
    password = wtforms.PasswordField('password', validators=[DataRequired()])


