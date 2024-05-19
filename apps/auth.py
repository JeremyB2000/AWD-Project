from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify, flash
import json
from werkzeug.security import check_password_hash

from apps.models import AccountDimension, RecipeDimension, CommentDimension
from apps import db
from apps.form import LoginForm, SearchForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

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
            user = AccountDimension.query.filter_by(username=username).first()
            if not user:
                return redirect(url_for('auth.login'))
            if check_password_hash(user.password, password):
                session["username"] = username
                session["user_id"] = user.user_id
                return redirect(url_for('auth.main'))
            else:
                return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('auth.login'))

@BP.route("/account", methods=['GET', 'POST'])
def account():
    user_id = session.get("user_id")
    if not user_id:
        flash('You need to log in to access the account page.', 'danger')
        return redirect(url_for('auth.login'))

    username = session.get("username")
    email = db.session.query(AccountDimension.email).filter_by(user_id=user_id).first()[0]
    recipes = RecipeDimension.query.order_by(RecipeDimension.recipe_id.desc()).filter_by(user_id=user_id).all()
    return render_template("account.html", username=username, email=email, recipes=recipes)

@BP.route("/main", methods=['GET', 'POST'])
def main():
    form = SearchForm()
    recipes = RecipeDimension.query.order_by(RecipeDimension.recipe_id.desc()).all()
    return render_template("Main.html", recipes=recipes, form=form)

@BP.route("/request", methods=['POST'])
def request_recipe():
    category = request.form.get("mealType")
    ingredients = request.form.get("request")
    title = request.form.get("request-title")
    request_data = RecipeDimension(category=category, recipe_name=title, ingredients=ingredients,
                                   status="Incomplete", user_id=session["user_id"])
    db.session.add(request_data)
    db.session.commit()
    return redirect(url_for('auth.main'))

@BP.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegistrationForm(request.form)
        print(form.validate())
        if form.validate():
            user = AccountDimension(username=form.username.data, email=form.email.data, password=generate_password_hash(form.password.data))
            print(user)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You have been logged in', 'success')
            return redirect(url_for('auth.login'))
    return render_template('login.html')

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


@BP.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        print('yes')
        search_query = form.search_input.data.split(',')
        print(search_query)
        meal_type = form.recipe_category.data.strip()
        ingredients = [ingredient.strip().lower() for ingredient in search_query]
        print(meal_type)
        recipes = db.session.query(RecipeDimension).filter(
            RecipeDimension.category.ilike(meal_type),  # Filter by meal type
            *[RecipeDimension.ingredients.ilike(f'%{ingredient}%') for ingredient in ingredients]  # Unpack ingredient filters
        ).all()
        return render_template('main.html', recipes=recipes, form=form)
    else:
        print('no')
    