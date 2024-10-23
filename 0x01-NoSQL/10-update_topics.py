#!/usr/bin/env python3
def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    Args:
        mongo_collection (pymongo.collection.Collection): MongoDB collection
        name: (string) school name to update
        topics: (list of strings) new topics for the school
    """
    if not isinstance(name, str) or not isinstance(topics, list):
        return
    
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
