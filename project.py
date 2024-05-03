from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html', title='Login')

@app.route('/main')
def main():
    return render_template('main.html', title='Main')

@app.route('/account')
def account():
    return render_template('account.html', title='Account')