import wtforms
from wtforms.validators import Email, DataRequired, Length


class LoginForm(wtforms.Form):
    username = wtforms.StringField()
    password = wtforms.PasswordField()
    checkbox = wtforms.Field()
