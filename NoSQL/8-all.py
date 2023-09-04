#!/usr/bin/env python3
"""Module that contains the list_all function"""


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    return list(mongo_collection.find())


    
