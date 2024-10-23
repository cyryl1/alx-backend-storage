#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB

"""
from pymongo import MongoClient

def get_nginx_stats():
    """
    Connect to MongoDB and retrieve statistics about Nginx logs
    """

    client = MongoClient('mongodb://127.0.0.1:27017')

    db = client.logs.nginx

    total_logs = db.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = db.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = db.nginx.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")

if __name__ == "__main__":
    get_nginx_stats()
