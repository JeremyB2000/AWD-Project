from flask import flash, redirect, render_template, request, url_for
from app import flaskApp, db

@flaskApp.route('/')
def login():
    return render_template('login.html')

@flaskApp.route('/main')
def main():
    return render_template('main.html')

@flaskApp.route('/account')
def account():
    return render_template('account.html')