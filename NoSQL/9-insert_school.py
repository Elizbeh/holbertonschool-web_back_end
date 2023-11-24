#!/usr/bin/env python3
""" pymongo """
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document into the collection using keyword arguments """
    inserted_document = mongo_collection.insert(kwargs)
    return inserted_document

