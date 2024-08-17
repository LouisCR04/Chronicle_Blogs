#!/usr/bin/env python3
"""
Main Flask Router
"""
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegForm, LoginForm
app = Flask(__name__)

"""
import os
SECRET_KEY = os.urandom(32)
"""
app.config['SECRET_KEY'] = '06a0233352eacd9d1c3133047eef7c10'

posts = [
    {
        'author': 'Ichibe Hyosube',
        'title': 'Zanpakuto',
        'content': 'First Zanpakuto',
        'date_posted': 'January 1, 2020'
    },
    {
        'author': 'Aizen Souske',
        'title': 'Hogyoku',
        'content': 'First Hogyoku',
        'date_posted': 'January 14, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='login', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
