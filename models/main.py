"""
Initializes the database
"""

import mongoengine

def global_init():
    mongoengine.register_connection(alias='core', name='allocations')
