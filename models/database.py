"""
Defines collections in the Database
"""

from mongoengine import Document, StringField, DictField, BooleanField

class Commodity(Document):
    type = StringField(required=True, max_length=50) #e.g. room/finances
    name = StringField(required=True, max_length=100) #e.g. room101
    description = StringField(max_length=500) #optional
    factors = DictField() # Store attributes like capacity and location
    available = BooleanField(default=True)
