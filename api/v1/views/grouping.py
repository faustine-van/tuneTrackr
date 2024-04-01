#!/usr/bin/env python3
""" similar artists and tracks"""
import pandas as pd
from flask import jsonify, abort, request
from flasgger import swag_from
from api.v1.views import app_views
from api.v1.views.trains.cluster import get_recommendations
from api.v1.views.docs.get_swagger import (
    get_cluster,
    get_top_popular,
    get_similar_artists,
    get_similar_tracks,
)
from models.artist import Artist
from models.track import Track
from models import dbStorage
from api.v1.views.helper import search_items
from api.v1.views.trains.cluster import get_cluster_artists


@app_views.route("/similar_artists", methods=["GET"], strict_slashes=False)
@swag_from(get_similar_artists)
def similar_artists():
    """return similar artists"""

    artist_id = request.args.get("id")
    if not artist_id:
        return jsonify({"status": 400, "msg": "Missing id of artist"}), 400
    try:
        num_items = int(request.args.get("item_count", default=0))
    except ValueError:
        return jsonify({"msg": "Invalid 'item_count' value"}), 400

    data = dbStorage.all(Artist).values()
    if not data:
        return jsonify({"msg": "artists not found"})

    items_data = [item.to_json() for item in data]

    artist = dbStorage.get(Artist, artist_id)
    if not artist:
        return jsonify({"id": artist_id, "status": 400, "msg": "artist not found"}), 400

    df = pd.DataFrame(items_data)

    if num_items == 0:
        ids = get_recommendations(df, artist.name, ["popularity", "follower"])
    else:
        ids = get_recommendations(
            df, artist.name, ["popularity", "follower"], num_items
        )

    remaining_ids = set(ids)

    results = search_items(Artist, remaining_ids)

    res = [item.to_json() for item in results]
    return jsonify({"count": len(res), "items": res}), 200


@app_views.route("/similar_tracks", methods=["GET"], strict_slashes=False)
@swag_from(get_similar_tracks)
def similar_tracks():
    """return similar tracks"""

    track_id = request.args.get("id")
    if not track_id:
        return jsonify({"status": 400, "msg": "Missing id of track"}), 400

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
        return jsonify({"id": track_id, "status": 400, "msg": "track not found"}), 400

    df = pd.DataFrame(items_data)

    if num_items == 0:
        ids = get_recommendations(df, track.name, ["popularity"])
    else:
        ids = get_recommendations(df, track.name, ["popularity"], num_items)

    remaining_ids = set(ids)

    results = search_items(Track, remaining_ids)

    res = [item.to_json() for item in results]
    return jsonify({"count": len(res), "items": res}), 200


@app_views.route("/cluster_artists", methods=["GET"], strict_slashes=False)
@swag_from(get_cluster)
def cluster_artists():
    """return clusters for artists"""

    try:
        n_clusters = int(request.args.get("num_clusters", default=0))
    except ValueError:
        return jsonify({"msg": "Invalid 'item_count' value"}), 400

    data = dbStorage.all(Artist).values()
    if not data:
        return jsonify({"status": 400, "msg": "artists not found"}), 400

    items_data = [item.to_json() for item in data]

    df = pd.DataFrame(items_data)

    features = ["popularity", "follower", "nb_album"]
    clusters = get_cluster_artists(df, features, n_clusters)
    list_ids = [ids for ids in clusters.values()]

    items = {}
    for i, ids in enumerate(list_ids):
        remaining_ids = set(ids)
        results = search_items(Artist, remaining_ids)
        res = [item.to_json() for item in results]
        items[f"cluster {i}"] = res
    return jsonify({"count": len(list_ids), "items": items}), 200
