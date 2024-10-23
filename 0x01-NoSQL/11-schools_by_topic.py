#!/usr/bin/env python3
def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools in a given topic.
    Args:
        mongo_collection: pymongo collection
        topic: str (school topic)
    """
    # Query the collection for schools with the given topic
    schools = mongo_collection.find({'topics': topic})
    
    # Convert the query results into a list of school names
    return list(schools)
