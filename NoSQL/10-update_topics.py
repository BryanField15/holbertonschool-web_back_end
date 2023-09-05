#!/usr/bin/env python3
"""Module that contains update_topics function"""


def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school document based on the name"""
    myquery = { "name": name }
    new_topics = { "$set": { "topics": topics } }
    mongo_collection.update_many(myquery, new_topics)
    
