#!/usr/bin/env python3
"""
Main Flask Router
"""
from flask import Flask, render_template, url_for, flash, redirect
from forms.forms import RegForm, LoginForm, PostsForm
from flask_mongoengine import MongoEngine
from models.engine.database import User, Post
from models.engine.db_config import mon_con
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager, login_required 


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
bcrypt = Bcrypt(app)
db = mon_con


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
        hashed_password = bcrypt.generate_password_hash(\
        form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password).save()
        flash(f"Account created. You are now able to log in.", 'success')
        return redirect(url_for('login'))
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


@app.route("/new/post", methods=['GET', 'POST'])
#login_required
def posts():
    form = PostsForm()
    if form.validate_on_submit():
        """post = Post(title=form.title.data, content=form.content.data,
                    author=current_user)"""
        flash('Post successfuly created', 'success')
        return redirect(url_for('home'))
    return render_template("posts.html", title='Post', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
