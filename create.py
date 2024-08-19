#!/usr/bin/env python3
"""
Mock data creation for the database
"""
from models.engine.database import User, Post
from models.engine.db_config import mon_con

# Create a new user
user = User(username='Aizen Souske', password='password1', email='aizen@demo.com').save()

# Create a new post
post = Post(author=user, title='Hogyoku', content='Infinite Reiatsu, True power').save()
