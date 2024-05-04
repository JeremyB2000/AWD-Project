from flask import flash, redirect, render_template, request, url_for
from app import flaskApp, db
from app.models import RecipeDimension

@flaskApp.route('/')
def login():
    recipes = RecipeDimension.query.all()
    return render_template('cards.html', recipes = recipes)

@flaskApp.route('/main')
def main():
    return render_template('main.html')

@flaskApp.route('/account')
def account():
    return render_template('account.html')