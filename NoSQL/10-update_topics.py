#!/usr/bin/env python3
""" 10. Change school topics """
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """ Modify school topics """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)

