from flask import Flask, render_template, redirect, url_for
from apps.auth import BP as auth_bp
from apps import db
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from apps.models import AccountDimension

app = Flask(__name__) #may need (, template_folder='/templates', static_folder='/static')
login = LoginManager(app)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)

@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for("auth.login"))

@login.user_loader
def load_user(id):
    return db.session.get(AccountDimension, int(id))


if __name__ == '__main__':
    app.run()
