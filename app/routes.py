from flask import render_template

from app import app

@app.route('/signin')
def signin():
    return render_template('signin.html',title='Sign In')

@app.route('/signup')
def signup():
    return render_template('signup.html',title='Sign Up')