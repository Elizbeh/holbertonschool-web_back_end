#!/usr/bin/env python3
""" 12-log_stats.py """
from pymongo import MongoClient

def log_stats():
    """ Display statistics from Nginx logs stored in MongoDB """
    client = MongoClient()
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\t{} method: {}".format(method, count))

    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status checks".format(status_check_count))

if __name__ == "__main__":
    log_stats()
