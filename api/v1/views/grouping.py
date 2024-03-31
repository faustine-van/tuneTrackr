#!/usr/bin/env python3
""" similar artists and tracks"""
import pandas as pd
from flask import jsonify, abort, request
from flasgger import swag_from
from api.v1.views import app_views
from api.v1.views.trains.cluster import (
    get_recomendations
)
# from api.v1.views.docs.get_swagger import get_top_popular
from models.artist import Artist
from models.track import Track
from models import dbStorage
from api.v1.views.helper import search_items


@app_views.route('/api/similar_artists', methods=['GET'],
                 strict_slashes=False)
def similar_artists():
    """return similar artists"""

    artist_id = request.args.get('id')
    if not artist_id:
        return jsonify(
            { 'status': 400, "msg": "Missing id of artist"}
        ), 400
    
    try:
        num_items = int(request.args.get("item_count", default=0))
    except ValueError:
        return jsonify({"msg": "Invalid 'item_count' value"}), 400
    
    data = dbStorage.all(Artist).values()
    if not data:
        abort(404)

    items_data = [item.to_json() for item in data]

    artist = dbStorage.get(Artist, artist_id)
    if not artist:
        abort(404)

    df = pd.DataFrame(items_data)

    if num_items == 0:
        ids = get_recomendations(df, artist.name,
                                         ['popularity', 'follower'])
    else:
        ids = get_recomendations(df,artist.name,['popularity', 'follower'],
                                  num_items)

    remaining_ids = set(ids)

    results = search_items(Artist, remaining_ids)

    res = [item.to_json() for item in results]
    return jsonify({"count": len(res), "items": res}), 200


@app_views.route('/api/similar_tracks', methods=['GET'],
                 strict_slashes=False)
def similar_tracks():
    """return similar tracks"""

    track_id = request.args.get('id')
    if not track_id:
        return jsonify(
            { 'status': 400, "msg": "Missing id of track"}
        ), 400
    
    try:
        num_items = int(request.args.get("item_count", default=0))
    except ValueError:
        return jsonify({"msg": "Invalid 'item_count' value"}), 400
    
    data = dbStorage.all(Track).values()
    if not data:
        abort(404)

    items_data = [item.to_json() for item in data]

    track = dbStorage.get(Track, track_id)
    if not track:
        abort(404)

    df = pd.DataFrame(items_data)

    if num_items == 0:
        ids = get_recomendations(df, track.name,
                                         ['popularity', 'follower'])
    else:
        ids = get_recomendations(df,track.name,['popularity', 'follower'],
                                  num_items)

    remaining_ids = set(ids)

    results = search_items(Track, remaining_ids)

    res = [item.to_json() for item in results]
    return jsonify({"count": len(res), "items": res}), 200
