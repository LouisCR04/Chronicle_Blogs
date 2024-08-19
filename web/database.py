"""
Database Engine
"""

from mongoengine import Document, StringField, DictField, BooleanField
from datetime import datetime

class Post(Document):
    author = StringField(required=True)
    title = StringField(required=True)
    content = StringField(required=True)
    date_posted = DateTimeField(required=True)
