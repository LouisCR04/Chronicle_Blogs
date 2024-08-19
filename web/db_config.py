"""
Database init file
"""
from mongoengine import connect

mon_con = connect('db_blogs')
