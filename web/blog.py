#!/usr/bin/env python3
"""
Main Flask Router
"""
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegForm, LoginForm
from flask_mongoengine import MongoEngine
from database import Post


app = Flask(__name__)
"""
import os
SECRET_KEY = os.urandom(32)
"""
app.config['SECRET_KEY'] = '06a0233352eacd9d1c3133047eef7c10'
app.config['MONGODB_SETTINGS'] = {
    'db': 'f_blog',
    'host': 'localhost',
    'port': 27017
}


"""Init MongoEngine"""
db = MongoEngine(app)

@app.route("/")
@app.route("/home")
def home():
    posts = Post.objects.all()
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About Seiretei')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template("reg.html", title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'aizen@gmail.com' and form.password.data\
            == '1234':
            flash('Login successful!', 'success')
            return redirect('home')
        else:
            flash("Login unsuccessful! Check email or password.", 'danger')
    return render_template("login.html", title='login', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
