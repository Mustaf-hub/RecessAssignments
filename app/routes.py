from flask import redirect, render_template, url_for

from app import app


@app.route('/')
def index():
    return redirect(url_for('signin'))

@app.route('/signin')
def signin():
    return render_template('signin.html',title='Sign In')

@app.route('/signup')
def signup():
    return render_template('signup.html',title='Sign Up')