#!/usr/bin/env python3
""" objects that handle all authentication of RestFul API"""
from flasgger import swag_from
from flask import jsonify, request
from models.artist import Artist
from models import dbStorage
from api.v1.views import app_views
from api.v1.views.docs.artists_swagger import (
    get_artists,
    get_artist,
    update_artist,
    delete_artist,
    post_artist_swagger,
)


@app_views.route("/artists", methods=["GET"], strict_slashes=False)
@swag_from(get_artists)
def view_artists():
    """
    Get all artists
    """
    items = [artist.to_json() for artist in dbStorage.all(Artist).values()]
    return jsonify(items), 200


@app_views.route("/artists/<artist_id>", methods=["GET"], strict_slashes=False)
@swag_from(get_artist)
def view_artist(artist_id):
    """
    Get  artist
    """
    if artist_id is None:
        return jsonify({"msg": "artist not found"}), 404

    artist = dbStorage.get(Artist, artist_id)
    if not artist:
        return jsonify({"msg": "artist not found"}), 404

    return jsonify(artist.to_json()), 200


@app_views.route("/artists/<artist_id>", methods=["PUT"], strict_slashes=False)
@swag_from(update_artist)
def updateartist(artist_id):
    """
    Update artist
    """
    if artist_id is None:
        return jsonify({"msg": "artist not found"}), 404

    artist = dbStorage.get(Artist, artist_id)
    if not artist:
        return jsonify({"msg": "artist not found"}), 404

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    ignore = ["created_at", "updated_at"]

    for key, value in data.items():
        if key not in ignore:
            setattr(Artist, key, value)
    artist.save()

    return jsonify(artist.to_json()), 200


@app_views.route("/artists/<artist_id>", methods=["DELETE"],
                 strict_slashes=False)
@swag_from(delete_artist)
def delete_artist(artist_id):
    """
    Delete all artist
    """
    if artist_id is None:
        return jsonify({"msg": "artist not found"}), 404

    artist = dbStorage.get(Artist, artist_id)
    if not artist:
        return jsonify({"msg": "artist not found"}), 404

    dbStorage.delete(artist)
    dbStorage.save()

    return jsonify({"msg": "artist delete successfully"}), 200


@app_views.route("/artists", methods=["POST"], strict_slashes=False)
@swag_from(post_artist_swagger)
def post_artist():
    """
    Create a artist
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    if not data.get("name"):
        return jsonify({"msg": "Missing name"}), 400
    try:
        new_instance = Artist(**data)
        new_instance.save()
        # Generate token
        token = new_instance.get_reset_token()
        return jsonify({"msg": "artist created successfully",
                        "token": token}), 201
    except Exception as e:
        # Log the exception for debugging
        print(f"Error creating artist: {e}")
        return jsonify({"msg": "Can't create artist"}), 500
