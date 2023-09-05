#!/usr/bin/env python3
"""Module that contains insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection based on kwargs"""
    new_doc = kwargs
    inserted_doc = mongo_collection.insert_one(new_doc)    
    return inserted_doc.inserted_id
