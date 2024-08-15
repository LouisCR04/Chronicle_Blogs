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
    meta = {
        'db_alias': 'core' # Which db conn to use
        'collection':'commodity'
    }


class Entity(Document):
    type = StringField(required=True, max_length=50) #e.g. student/camp
    name = StringField(required=True, max_length=100) #e.g. Aizen/Gaza
    description = StringField(max_length=500) #optional
    factors = DictField() #Factors like financial_need to help calc weights
    available = BooleanField(default=True)
    meta = meta = {
        'db_alias': 'core'
        'collection':'entity'
    }
