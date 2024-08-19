"""
Database init file
"""
from mongoengine import connect, disconnect

disconnect()
mon_con = connect('db_blogs')
