#!/usr/bin/env python3
"""
Module that inserts a new document in a collection basedx kwargs.
"""
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new school document into the MongoDB collection.
    Args:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection to insert the document into.
    **kwargs: The school document fields and values to insert.
    Returns:
    _id of the newly inserted document
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

    