#!/usr/bin/env python3
"""Script to get stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['logs']
collection = db['nginx']
total_logs = collection.count_documents({})

print(f"{total_logs} logs")
print("Methods:")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    method_count = collection.count_documents({"method": method})
    print(f"\t{method}: {method_count}")

status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_count} status check")
