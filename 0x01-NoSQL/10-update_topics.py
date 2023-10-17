#!/usr/bin/env python3
"""
Function changes all topics of a school document based on the name
Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection is the pymongo object
name (String) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    Prototype: def update_topics(mongo_collection, name, topics):
    Changes all topics of a school document based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
