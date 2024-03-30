#!/usr/bin/env python3
"""top artists, tracks, or albums routes"""
import pandas as pd
from flask import jsonify, request, abort
from flasgger import swag_from
from api.v1.views import app_views
from api.v1.views.helper.get_top import (
    get_top, get_new_albums, get_top_artists
)
from api.v1.views.docs.get_swagger import get_top_popular
from models.album import Album
from models.artist import Artist
from models.track import Track
from models import dbStorage


@app_views.route("/popular/<item_type>", methods=["GET"], strict_slashes=False)
@swag_from(get_top_popular)
def top_popular(item_type):
    """top artists, albums, tracks"""
    try:
        request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    if item_type is None:
        abort(404)

    num_items = request.get_json().get("num_items")
    data = []
    item_types = [Album, Artist, Track]

    # if item_type == 'all':
    #    for itype in item_types:
    #        items = dbStorage.all(itype).values()
    #        data.append(items)
    if item_type == "artists":
        data = dbStorage.all(Artist).values()
    elif item_type == "albums":
        data = dbStorage.all(Album).values()
    elif item_type == "tracks":
        data = dbStorage.all(Track).values()

    # print(data)
    if not data:
        abort(404)

    items_data = [item.to_json() for item in data]
    print(items_data)
    df = pd.DataFrame(items_data)

    if item_type == "":
        item_type = None

    # Check if num_items is specified
    if num_items == 0:
        # Call get_top without num_items
        listOfIds = get_top(item_type, df)
    else:
        # Always pass num_items as an argument
        listOfIds = get_top(item_type, df, num_items)
    # print(listOfIds)
    results = []
    remaining_ids = set(listOfIds)

    # print(remaining_ids)
    for itype in item_types:
        if not remaining_ids:
            break
    for id in remaining_ids.copy():
        for itype in item_types:
            search_results = dbStorage.search(itype, {"id": id}).values()
            if search_results:
                results.extend(search_results)
                remaining_ids.remove(id)
    res = [item.to_json() for item in results]
    # print(res)
    return jsonify({"count": len(res), "items": res}), 200


@app_views.route("artists/top_artists", methods=["GET"], strict_slashes=False)
def top_artists():
    """top artists, albums, tracks"""
    try:
        request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    itype = request.get_json().get("item_type")
    num_items = request.get_json().get("num_items")

    data = dbStorage.all(Artist).values()
    if not data:
        abort(404)
    items_data = [item.to_json() for item in data]
    # print(items_data)
    df = pd.DataFrame(items_data)

    if num_items == 0:
        listOfIds = get_top_artists(itype, df)
    else:
        listOfIds = get_top_artists(itype, df, num_items)
    print(listOfIds)
    remaining_ids = set(listOfIds)
    results = []
    for id in remaining_ids.copy():
        search_results = dbStorage.search(Artist, {"id": id}).values()
        if search_results:
            results.extend(search_results)
            remaining_ids.remove(id)
    res = [item.to_json() for item in results]
    # print(res)
    return jsonify({"count": len(res), "items": res}), 200


@app_views.route("albums/new_albums", methods=["GET"], strict_slashes=False)
def new_albums():
    """new albums"""
    try:
        request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    num_items = request.get_json().get("num_items")

    data = dbStorage.all(Album).values()
    if not data:
        abort(404)
    items_data = [item.to_json() for item in data]
    # print(items_data)
    df = pd.DataFrame(items_data)

    if num_items == 0:
        listOfIds = get_new_albums(df)
    else:
        listOfIds = get_new_albums(df, num_items)
    print(listOfIds)
    remaining_ids = set(listOfIds)
    results = []
    for id in remaining_ids.copy():
        search_results = dbStorage.search(Album, {"id": id}).values()
        if search_results:
            results.extend(search_results)
            remaining_ids.remove(id)
    res = [item.to_json() for item in results]
    # print(res)
    return jsonify({"count": len(res), "items": res}), 200
