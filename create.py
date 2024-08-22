#!/usr/bin/env python3
"""
Mock data creation for the database
"""
from models.engine.database import User, Post
from models.engine.db_config import mon_con
import json
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

with open('USER_MOCK_DATA.json', 'r') as file:
    users = json.load(file)

for user in users:
    hashed_password = bcrypt.generate_password_hash(user['password']).decode('utf-8')
    user = User(username=user['username'], 
                password=hashed_password, 
                email=user['email']).save()
