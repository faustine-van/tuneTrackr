#!/usr/bin/env python3
""" objects that handle all authentication of RestFul API"""
from flasgger import swag_from
from flask import jsonify, request
from models.album import Album
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
    return jsonify(all_albums), 200


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

    return jsonify(album.to_json()), 200


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
