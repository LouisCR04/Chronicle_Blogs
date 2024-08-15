"""
Creates MongoDb Connection
"""

from pymongo import MongoClient

client = MongoClient("localhost", 27017)

commodities = db["commodities"]
entities = db["entitiies"]
