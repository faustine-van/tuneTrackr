#!/usr/bin/env python3
""" objects that handle all authentication of RestFul API"""
from flasgger import swag_from
from flask import jsonify, request
from models.album import Album
from models.artist import Artist
from models import dbStorage
from api.v1.views import app_views
from api.v1.views.docs.albums_swagger import (
    get_albums,
    get_album,
    update_album,
    delete_album,
    post_album_swagger,
)


@app_views.route("/albums", methods=["GET"], strict_slashes=False)
@swag_from(get_albums)
def view_albums():
    """
    Get all albums
    """
    all_albums = [album.to_json() for album in dbStorage.all(Album).values()]

    formatted_albums = []
    for album_json in all_albums:
        # Access related artist and album information
        artist = dbStorage.get(Artist, album_json["artist_id"])

        # new formatted album dictionary
        new_album_dict = {
            "id": album_json["id"],
            "title": album_json["title"],
            "popularity": album_json["popularity"],
            "artists": {
                "artist_id": album_json["artist_id"],
                "name": artist.name if artist else None,
            },
            "total_tracks": album_json["total_tracks"],
            "release_date": album_json["release_date"],
            "created_at": album_json["created_at"],
            "updated_at": album_json["updated_at"]
        }

        # Append the formatted album dictionary to the list
        formatted_albums.append(new_album_dict)

    return jsonify({"count": len(all_albums), "items": formatted_albums,
                   "url": request.url}), 200


@app_views.route("/albums/<album_id>", methods=["GET"], strict_slashes=False)
@swag_from(get_album)
def view_album(album_id):
    """
    Get  album
    """
    if album_id is None:
        return jsonify({"msg": "album not found"}), 404

    album = dbStorage.get(Album, album_id)
    if not album:
        return jsonify({"msg": "album not found"}), 404


    artist = dbStorage.get(Artist, album.artist_id)
    if not artist:
        return jsonify({"msg": "artist not found"}), 404

    album_json = album.to_json()
    album_dict = album_json
    new_album_dict = {
        "id": album_dict["id"],
        "title": album_dict["title"],
        "popularity": album_dict["popularity"],
        "label": album_dict["label"],
        "total_tracks": album_dict["total_tracks"],
        "artists": {"artist_id": album_dict["artist_id"], "name": artist.name},
        "release_date": album_dict["release_date"],
        "created_at": album_dict["created_at"],
        "updated_at": album_dict["updated_at"]
    }

    return jsonify({"url": request.url, "count": 1, "item": new_album_dict}), 200


@app_views.route("/albums/<album_id>", methods=["PUT"], strict_slashes=False)
@swag_from(update_album)
def updatealbum(album_id):
    """
    Update album
    """
    if album_id is None:
        return jsonify({"msg": "album not found"}), 404

    album = dbStorage.get(Album, album_id)
    if not album:
        return jsonify({"msg": "album not found"}), 404

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    ignore = ["created_at", "updated_at"]

    for key, value in data.items():
        if key not in ignore:
            setattr(Album, key, value)
    album.save()

    return jsonify(album.to_json()), 200


@app_views.route("/albums/<album_id>", methods=["DELETE"], strict_slashes=False)
@swag_from(delete_album)
def deletealbum(album_id):
    """
    Delete all album
    """
    if album_id is None:
        return jsonify({"msg": "album not found"}), 404

    album = dbStorage.get(Album, album_id)
    if not album:
        return jsonify({"msg": "album not found"}), 404

    dbStorage.delete(album)
    dbStorage.save()

    return jsonify({"msg": "album delete successfully"}), 200


@app_views.route("/albums", methods=["POST"], strict_slashes=False)
@swag_from(post_album_swagger)
def post_album():
    """
    Create a album
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    try:
        new_instance = Album(**data)
        new_instance.save()
        # Generate token
        token = new_instance.get_reset_token()
        return jsonify({"msg": "album created successfully", "token": token}), 201
    except Exception as e:
        # Log the exception for debugging
        print(f"Error creating album: {e}")
        return jsonify({"msg": "Can't create album"}), 500
