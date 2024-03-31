#!usr/bin/env python3
"""Helper functions"""
import numpy as np


def get_popular(item_type: str, data: dict, n: int = 10) -> list:
    """return top artists, tracks or albums"""
    drop_list = ["created_at", "updated_at"]
    # remove unused feature
    data = data.drop(drop_list, axis=1)
    # remove None data
    data = data.dropna(axis=0, subset=['popularity'])
    data = data.sort_values(by="popularity", ascending=False).head(n)

    top = None

    items = []
    if item_type is None:
        items.append([data["name"]])
        items.append([data["title"]])
        top = items

    if item_type == "artists" or item_type == "tracks":
        top = data["id"]
    elif item_type == "albums":
        top = data["id"]

    top = np.array(top)

    return top



def get_top_artists(meta_type: str, data: dict, n: int =10) -> list:
    """get top followers and listeners"""
    drop_list = ["created_at", "updated_at"]
    # remove unused feature
    data = data.drop(drop_list, axis=1)
    # remove None data
    data = data.dropna(axis=0, subset=['popularity'])

    if meta_type == "followers":
        data = data.sort_values(by="follower", ascending=False).head(n)
    elif meta_type == "monthly_listeners":
        data = data.sort_values(by="monthly_listener", ascending=False).head(n)

    print(data.to_string())

    top = np.array(data['id'])

    return top

def get_new_albums(data, n=5):
    """get new albums"""
    drop_list = ["created_at", "updated_at"]
    # remove unused feature
    data = data.drop(drop_list, axis=1)
    # remove None data
    data = data.dropna(axis=0, subset=['popularity'])

    data = data.sort_values(by="release_date", ascending=False).head(n)

    top = np.array(data["id"])

    return top
