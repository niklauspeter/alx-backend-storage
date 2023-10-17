#!/usr/bin/env python3
"""
python function returns all students sorted by average score
Prototype: def top_students(mongo_collection):
The top must be ordered
average score must be part of each item with key = averageScore
"""


def top_students(mongo_collection):
    """
    Prototype: def top_students(mongo_collection):
    Returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ])
