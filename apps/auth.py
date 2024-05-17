from flask import Blueprint, flash, render_template, request, url_for, redirect, session, jsonify
import json
from werkzeug.security import check_password_hash
from flask_login import current_user, login_user, logout_user

from apps.models import AccountDimension, RecipeDimension, CommentDimension
from apps import db
from apps.form import LoginForm
from flask_wtf import FlaskForm

BP = Blueprint('auth', __name__, url_prefix='/auth')


@BP.route("/login", methods=['GET', 'POST'])
def login():
    #Provide the login page
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    
    password = form.password.data
    username = form.username.data
    user = AccountDimension.query.get(username)
    print(user)
    #Check username
    if not user:
        flash('Invalid username or password')
        print('check username')
        return render_template('login.html', form=form)
    
    #Check password
    if not user.check_password(password): 
        flash('Invalid username or password')
        print('check pword')
        return render_template('login.html', form=form)
    
    #username and password both correct
    print('correct')
    login_user(user)
    return redirect(url_for('auth.main'))
        

#Connect to a login/logout button at a later point
@BP.route('/logout')
def logout():
        logout_user()
        return redirect(url_for('auth.main'))


@BP.route("/account", methods=['GET', 'POST'])
def account():
    user_id = session["user_id"]
    username = db.session.query(AccountDimension.username).filter_by(user_id=user_id).first()
    username = username[0]
    email = db.session.query(AccountDimension.email).filter_by(user_id=user_id).first()
    email = email[0]
    recipes = db.session.query(RecipeDimension).filter_by(user_id=user_id).all()
    return render_template("account.html", username=username, email=email, recipes=recipes)


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