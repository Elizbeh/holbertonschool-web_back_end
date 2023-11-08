#!/usr/bin/env python3
""" 11-schools_by_topic """
from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """ Retrieve a list of schools that focus on a
    specific topic
    """
    query = {"topics": topic}
    matching_schools = mongo_collection.find(query)
    return list(matching_schools)
