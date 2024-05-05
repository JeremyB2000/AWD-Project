from flask import Blueprint, render_template, request, url_for, redirect, session,jsonify
import json
from werkzeug.security import check_password_hash

from apps.models import AccountDimension, RecipeDimension
from apps import db
from apps.form import LoginForm

BP = Blueprint('auth', __name__, url_prefix='/auth')


@BP.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            checkbox = request.form.get("checkbox")
            user = AccountDimension.query.filter_by(username=username).first()
            if not user:
                return redirect(url_for('auth.login'))
            if user.password == password:
                session["username"] = username
                session["user_id"] = user.user_id
                recipes = RecipeDimension.query.all()
                return render_template("Main.html",recipes=recipes)
            else:
                return redirect(url_for('auth.login'))
            pass
        else:
            return redirect(url_for('auth.login'))


@BP.route("/account", methods=['GET', 'POST'])
def account():
    return render_template("account.html")


@BP.route("/Main", methods=['GET', 'POST'])
def main():
    return render_template("Main.html")


@BP.route("/request", methods=['POST'])
def request_recipe():
    category = request.form.get("mealType")
    instructions = request.form.get("request")
    request_data = RecipeDimension(category=category, recipe_name=instructions,
                                   status="uncompleted", user_id=session["user_id"])
    db.session.add(request_data)
    db.session.commit()
    recipes = RecipeDimension.query.all()
    return render_template('Main.html', recipes=recipes)
