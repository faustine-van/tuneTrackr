#!/usr/bin/env python3
"""top artists, tracks, or albums routes"""
import pandas as pd
from flask import jsonify, abort, request
from flasgger import swag_from
from api.v1.views import app_views
from api.v1.views.trains.get_top import get_popular, get_new_albums, get_top_artists
from api.v1.views.docs.get_swagger import (
    get_top_popular, get_top_artists_swagger,
    get_new_albums_swagger,
)
from models.album import Album
from models.artist import Artist
from models.track import Track
from models import dbStorage
from api.v1.views.helper import search_items


@app_views.route("/popular/<item_type>", methods=["GET"], strict_slashes=False)
@swag_from(get_top_popular)
def top_popular(item_type):
    """top artists, albums, tracks"""
    if item_type is None:
        abort(404)

    try:
        num_items = int(request.args.get("item_count", default=0))
    except ValueError:
        return jsonify({"msg": "Invalid 'item_count' value"}), 400

    data = []

    item_types = [Album, Artist, Track]
    if item_type == "artists":
        data = dbStorage.all(Artist).values()
    elif item_type == "albums":
        data = dbStorage.all(Album).values()
    elif item_type == "tracks":
        data = dbStorage.all(Track).values()

    if not data:
        abort(404)

    items_data = [item.to_json() for item in data]

    df = pd.DataFrame(items_data)

    if item_type == "":
        item_type = None

    # Check if num_items is specified
    if num_items == 0:
        # Call get_top without num_items
        ids = get_popular(item_type, df)
    else:
        # Always pass num_items as an argument
        ids = get_popular(item_type, df, num_items)
    # print(ids)
    results = []
    remaining_ids = set(ids)

    # print(remaining_ids)
    for itype in item_types:
        if not remaining_ids:
            break
    for item_id in remaining_ids.copy():
        for itype in item_types:
            search_results = dbStorage.search(itype, {"id": item_id}).values()
            if search_results:
                results.extend(search_results)
                remaining_ids.remove(item_id)
    res = [item.to_json() for item in results]
    # print(res)
    return jsonify({"count": len(res), "items": res}), 200


@app_views.route("/artists/top_artists", methods=["GET"], strict_slashes=False)
@swag_from(get_top_artists_swagger)
def top_artists():
    """top artists, albums, tracks"""
    itype = request.args.get("item_type")
    if itype is None:
        return jsonify({"msg": "Missing 'item_type'"}), 400
    elif itype == "":
        return jsonify({"msg": "Missing 'item_type' value"}), 400

    try:
        num_items = int(request.args.get("item_count", default=0))
    except ValueError:
        return jsonify({"msg": "Invalid 'item_count' value"}), 400

    data = dbStorage.all(Artist).values()
    if not data:
        abort(404)
    items_data = [item.to_json() for item in data]

    # print(items_data)
    df = pd.DataFrame(items_data)

    if num_items == 0:
        ids = get_top_artists(itype, df)
    else:
        ids = get_top_artists(itype, df, num_items)

    remaining_ids = set(ids)

    results = search_items(Artist, remaining_ids)

    res = [item.to_json() for item in results]

    return jsonify({"count": len(res), "items": res}), 200


@app_views.route("albums/new_albums", methods=["GET"], strict_slashes=False)
@swag_from(get_new_albums_swagger)
def new_albums():
    """new albums"""
    try:
        num_items = int(request.args.get("item_count", default=0))
    except ValueError:
        return jsonify({"msg": "Invalid 'item_count' value"}), 400

    data = dbStorage.all(Album).values()
    if not data:
        abort(404)
    items_data = [item.to_json() for item in data]
    # print(items_data)
    df = pd.DataFrame(items_data)

    if num_items == 0:
        ids = get_new_albums(df)
    else:
        ids = get_new_albums(df, num_items)

    remaining_ids = set(ids)

    results = search_items(Album, remaining_ids)

    res = [item.to_json() for item in results]
    # print(res)
    return jsonify({"count": len(res), "items": res}), 200
