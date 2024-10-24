#!/usr/bin/env python3
"""
Module that provides a function to list all documents in a MongoDB collection
"""
def list_all(mongo_collection):
    """
    Lists all documents in a Mongobd collection
    Args:
        mongo_collection: pymongo collection object
    Returns:
        List of documents in the collection, or empty list if none
    """
    documents = mongo_collection.find()
    return [doc for doc in documents]
