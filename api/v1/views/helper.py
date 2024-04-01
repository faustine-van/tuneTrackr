#!/usr/bin/env python3
"""search artists, tracks"""
from models import dbStorage


def search_items(cls, remaining_ids):
    """
    Search for items in the database using the provided IDs.

    Args:
        cls: class.
        remaining_ids (list): A list of items IDs to search for.

    Returns:
        list: A list of item objects found in the database.

    """
    results = []
    for item_id in remaining_ids.copy():
        search_results = dbStorage.search(cls, {"id": item_id}).values()
        if search_results:
            results.extend(search_results)
            remaining_ids.remove(item_id)
    return results
