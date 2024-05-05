from flask import Flask, render_template, redirect, url_for
from apps.auth import BP as auth_bp
from apps import db
from config import Config
from apps.models import AccountDimension, RecipeDimension
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)


@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for("auth.login"))


if __name__ == '__main__':
    app.run()
