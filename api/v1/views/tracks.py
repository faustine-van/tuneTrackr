#!/usr/bin/env python3
""" objects that handle all authentication of RestFul API"""
from flasgger import swag_from
from flask import jsonify
from models.track import Track
from models import dbStorage
from api.v1.views import app_views
from api.v1.views.docs.tracks_swagger import (
    get_tracks,
    get_track,
    update_track,
    delete_track,
    post_track_swagger,
)


@app_views.route("/tracks", methods=["GET"], strict_slashes=False)
@swag_from(get_tracks)
def view_tracks():
    """
    Get all tracks
    """
    all_tracks = [track.to_json() for track in dbStorage.all(Track).values()]
    return jsonify({"count": len(all_tracks), "items": all_tracks}), 200


@app_views.route("/tracks/<track_id>", methods=["GET"], strict_slashes=False)
@swag_from(get_track)
def view_track(track_id):
    """
    Get  track
    """
    if track_id is None:
        return jsonify({"msg": "track not found"}), 404

    track = dbStorage.get(Track, track_id)
    if not track:
        return jsonify({"msg": "track not found"}), 404

    return jsonify(track.to_json()), 200


@app_views.route("/tracks/<track_id>", methods=["PUT"], strict_slashes=False)
@swag_from(update_track)
def updatetrack(track_id):
    """
    Update track
    """
    if track_id is None:
        return jsonify({"msg": "track not found"}), 404

    track = dbStorage.get(Track, track_id)
    if not track:
        return jsonify({"msg": "track not found"}), 404

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    ignore = ["created_at", "updated_at"]

    for key, value in data.items():
        if key not in ignore:
            setattr(Track, key, value)
    track.save()

    return jsonify(track.to_json()), 200


@app_views.route("/tracks/<track_id>", methods=["DELETE"],
                 strict_slashes=False)
@swag_from(delete_track)
def deletetrack(track_id):
    """
    Delete all track
    """
    if track_id is None:
        return jsonify({"msg": "track not found"}), 404

    track = dbStorage.get(Track, track_id)
    if not track:
        return jsonify({"msg": "track not found"}), 404

    dbStorage.delete(track)
    dbStorage.save()

    return jsonify({"msg": "track delete successfully"}), 200


@app_views.route("/tracks", methods=["POST"], strict_slashes=False)
@swag_from(post_track_swagger)
def post_track():
    """
    Create a track
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    try:
        new_instance = Track(**data)
        new_instance.save()
        # Generate token
        token = new_instance.get_reset_token()
        return jsonify({"msg": "track created successfully",
                        "token": token}), 201
    except Exception as e:
        # Log the exception for debugging
        print(f"Error creating track: {e}")
        return jsonify({"msg": "Can't create track"}), 500
