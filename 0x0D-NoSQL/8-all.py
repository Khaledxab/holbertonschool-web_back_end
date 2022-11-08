#!/usr/bin/env python3
"""
Lists all documents in a collection
with python
"""


def list_all(mongo_collection):
    """ List all documents in Python """
    if mongo_collection:
        return mongo_collection.find()
    return []
