#!/usr/bin/env python3
"""
Initializes the database
"""

import mongoengine

def global_init():
    mongoengine.register_connection(alias='core', name='allocations')


if __name__ == "__main__":
    global_init()
