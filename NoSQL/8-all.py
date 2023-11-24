#!/usr/bin/env python3
""" List all documents in Python """
from pymongo import MongoClient

def list_all(mongo_collection):
    """ Retrieve all documents from the collection """
    documents = mongo_collection.find()
    return list(documents) if documents else []
