from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify
import json
from werkzeug.security import check_password_hash

from apps.models import AccountDimension, RecipeDimension, CommentDimension
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
                return redirect(url_for('auth.main'))
            else:
                return redirect(url_for('auth.login'))
            pass
        else:
            return redirect(url_for('auth.login'))


@BP.route("/account", methods=['GET', 'POST'])
def account():
    user_id = session["user_id"]
    return render_template("account.html")


@BP.route("/Main", methods=['GET', 'POST'])
def main():
    recipes = RecipeDimension.query.order_by(RecipeDimension.recipe_id.desc()).all()
    return render_template("Main.html", recipes=recipes)


@BP.route("/request", methods=['POST'])
def request_recipe():
    category = request.form.get("mealType")
    instructions = request.form.get("request")
    request_data = RecipeDimension(category=category, recipe_name=instructions,
                                   status="Incomplete", user_id=session["user_id"])
    db.session.add(request_data)
    db.session.commit()
    recipes = RecipeDimension.query.all()
    return render_template('Main.html', recipes=recipes)

@BP.route("/comment", methods=['POST'])
def post_comment():
    #Variables
    comment_string = request.form.get("comment")
    recipe_id = request.form.get("recipe_id")
    user_id = session["user_id"]
    username = db.session.query(AccountDimension.username).filter_by(user_id=user_id).first()
    username = username[0]

    #Add data to database
    comment_data = CommentDimension(user_id=user_id, comment=comment_string, recipe_id=recipe_id)
    RecipeDimension.query.filter_by(recipe_id=recipe_id).update({"status": "Complete"})
    db.session.add(comment_data)
    db.session.commit()

    #find the comment id
    comment_id = db.session.query(CommentDimension.comment_id).filter_by(user_id=user_id, recipe_id=recipe_id, comment=comment_string).first()
    comment_id = comment_id[0]

    #return the comment, username and comment id
    comment_data = {"comment": comment_string, "username": username, "comment_id": comment_id}
    return jsonify(comment_data)