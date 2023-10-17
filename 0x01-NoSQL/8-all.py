#!/usr/bin/env python3
"""
python function List all documents in a collection
"""


def list_all(mongo_collection):
    """
    function lists all documents in a collection

    :param is mongo_collection:
    :returns list of documents:
    """
    documents = mongo_collection.find()
    return documents
