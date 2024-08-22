#!/usr/bin/env python3
"""
Mock data creation for the database
"""
from models.engine.database import User, Post
from models.engine.db_config import mon_con
import json

with open('USER_MOCK_DATA.json', 'r') as file:
    users = json.load(file)

for user in users:
    user = User.objects(username=user['username'], email=user['email']).first()
    if user:
        user.delete()
