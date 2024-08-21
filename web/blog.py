#!/usr/bin/env python3
"""
Main Flask Router
"""
import os
from flask import Flask, render_template, url_for, flash, redirect, \
abort, request
from flask_login import LoginManager, login_user, current_user, \
logout_user, login_required
from forms.forms import RegForm, LoginForm, PostsForm, UpdateAcctForm
from flask_mongoengine import MongoEngine
from models.engine.database import User, Post
from models.engine.db_config import mon_con
from flask_bcrypt import Bcrypt


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
login_manager = LoginManager(app)
login_manager.login_view = 'login'
db = mon_con

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful! Check email or password.", 'danger')
    return render_template("login.html", title='login', form=form)


@app.route("/new/post", methods=['GET', 'POST'])
#login_required
def posts():
    form = PostsForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,
                    author=current_user).save()
        flash('Post successfuly created', 'success')
        return redirect(url_for('home'))
    return render_template("c_post.html", title='Post', form=form,
                           legend='New Post')

@app.route("/logedin")
def loged_in():
    if current_user.is_authenticated:
        return f"{ current_user.email } is logged in" 
    else:
        return "Not logged in"

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
    
def save_pic(form_picture, username):
    _, f_ext = os.path.splitext(form_picture.filename)
    pic_name = username + f_ext
    pic_path = os.path.join(app.root_path, 'static/prof_pics', pic_name)
    form_picture.save(pic_path)
    return pic_name


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAcctForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.picture.data:
            pic_file = save_pic(form.picture.data, current_user.username)
            current_user.image_file = pic_file
        current_user.save()
        flash('Account Updated Successfully', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    img_file = url_for('static', filename='prof_pics/' + current_user.image_file)
    return render_template("account.html", title='Profile',
                           form=form, image_file=img_file)

@app.route("/post/int: <post_id>")
def post(post_id):
    post = Post.objects(id=post_id).first()
    if not post:
        return "Post not found", 404
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/int: <post_id>/update", methods=['GET', 'POST'])
@login_required
def upd_post(post_id):
    post = Post.objects(id=post_id).first()
    if not post:
        return "Post not found", 404
    if post.author != current_user:
        abort(403)
    form = PostsForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.save()
        flash('Post has successfully been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('c_post.html', title='Update Post',
                           form=form, legend='Update Post')

@app.route("/post/int: <post_id>/delete", methods=['POST'])
@login_required
def del_post(post_id):
    post = Post.objects(id=post_id).first()
    if not post:
        return "Post not found", 404
    if post.author != current_user:
        abort(403)
    post.delete()
    flash('Post has been deleted!', 'success')
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
