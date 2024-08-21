"""
forms file
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,\
TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models.engine.database import User, Post
from flask_login import current_user

class PostsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RegForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                           Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_p = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                     EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        from blog import db
        user = User.objects(username=username.data).first()
        if user:
            raise ValidationError('User already exists')
    
    def validate_email(self, email):
        from blog import db
        email = User.objects(email=email.data).first()
        if email:
            raise ValidationError('Email already exists')


class UpdateAcctForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                           Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Prof Pic', validators=\
    [FileAllowed(['jpg', 'png'], '.jpg and .png only')])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            from blog import db
            user = User.objects(username=username.data).first()
            if user:
                raise ValidationError('User already exists')

    def validate_email(self, email):
        if email.data != current_user.email:
            from blog import db
            email = User.objects(email=email.data).first()
            if email:
                raise ValidationError('Email already exists')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
