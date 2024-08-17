"""
Defines collections in the Database
"""

from mongoengine import Document, StringField, DictField, BooleanField

class Commodity(Document):
    type = StringField(required=True, max_length=50) #e.g. room/finances
    name = StringField(required=True, max_length=100) #e.g. room101
    description = StringField(max_length=500) #optional
    factors = DictField()
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
    def clean(self, Commodity.type):
        corresponding_commodity = Commodity.type
        
        if corresponding_commodity:
            valid_keys = set(corresponding_commodity.factors.keys())
            entity_keys = set(self.factors.keys())
            
            # Ensure entity factors match commodity factors
            if not entity_keys.issubset(valid_keys):
                invalid_keys = entity_keys - valid_keys
                raise ValidationError(
                    f"Invalid factor keys: {invalid_keys}. Allowed keys are: {valid_keys}."
                )
            
            # Ensure all required factors are provided
            for key in valid_keys:
                if key not in self.factors:
                    raise ValidationError(
                        f"Missing factor: {key}. All factors in {valid_keys} must be provided."
                    )
        else:
            raise ValidationError(f"No corresponding Commodity found for type {self.type}.")

