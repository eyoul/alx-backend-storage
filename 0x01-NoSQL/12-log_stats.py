#!/usr/bin/env python3
""" lists all documents with name starting by Holberton"""

from pymongo import MongoClient


def log_stats():
    """
    Display log
    """
    client = MongoClient('mogodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    total = log_collection.count_documents({})
    get = log_collection.count_documents({"method": "GET"})
    post = log_collection.count_documents({"method": "POST"})
    put = log_collection.count_documents({"method": "PUT"})
    patch = log_collection.count_documents({"method": "PATCH"})
    delete = log_collection.count_documents({"method": "DELETE"})
    path = log_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
    
