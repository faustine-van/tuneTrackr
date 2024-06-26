#!/usr/bin/python3
""" objects that handle all authentication of RestFul API"""
from flasgger import swag_from
from flask import jsonify, request
from models.genre import Genre
from models import dbStorage
from api.v1.views import app_views
from api.v1.views.docs.genres_swagger import (
    get_genres,
    get_genre,
    update_genre,
    delete_genre,
    post_genre_swagger,
)


@app_views.route("/genres", methods=["GET"], strict_slashes=False)
@swag_from(get_genres)
def view_genres():
    """
    Get all genres
    """
    items = [genre.to_json() for genre in dbStorage.all(Genre).values()]
    
    return jsonify({"url": request.url,
                    "count": len(items),
                    "items": items
                    }
                ), 200


@app_views.route("/genres/<genre_id>", methods=["GET"], strict_slashes=False)
@swag_from(get_genre)
def view_genre(genre_id):
    """
    Get  genre
    """
    if genre_id is None:
        return jsonify({"msg": "genre not found"}), 404

    genre = dbStorage.get(Genre, genre_id)
    if not genre:
        return jsonify({"msg": "genre not found"}), 404

    return jsonify(genre.to_json()), 200


@app_views.route("/genres/<genre_id>", methods=["PUT"], strict_slashes=False)
@swag_from(update_genre)
def updategenre(genre_id):
    """
    Update genre
    """
    if genre_id is None:
        return jsonify({"msg": "genre not found"}), 404

    genre = dbStorage.get(Genre, genre_id)
    if not genre:
        return jsonify({"msg": "genre not found"}), 404

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    ignore = ["created_at", "updated_at"]

    for key, value in data.items():
        if key not in ignore:
            setattr(genre, key, value)
    genre.save()

    return jsonify(genre.to_json()), 200


@app_views.route("/genres/<genre_id>", methods=["DELETE"], strict_slashes=False)
@swag_from(delete_genre)
def deletegenre(genre_id):
    """
    Delete all genre
    """
    if genre_id is None:
        return jsonify({"msg": "genre not found"}), 404

    genre = dbStorage.get(Genre, genre_id)
    if not genre:
        return jsonify({"msg": "genre not found"}), 404

    dbStorage.remove(genre)
    dbStorage.save()

    return jsonify({"msg": "genre delete successfully"}), 200


@app_views.route("/genres", methods=["POST"], strict_slashes=False)
@swag_from(post_genre_swagger)
def post_genre():
    """
    Create a genre
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    new_instance = Genre(**data)
    new_instance.save()
    return jsonify({"msg": "Genre created successfult"}), 201