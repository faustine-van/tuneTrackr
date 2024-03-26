#!/usr/bin/python3
""" objects that handle all authentication of RestFul API"""
from flasgger import swag_from
from flask import jsonify
from models.user import User
from models import dbStorage
from api.v1.views import app_views
from api.v1.views.docs.users_d import (
    get_users,
    get_user,
    update_user,
    delete_user,
)

@app_views.route("/users", methods=["GET"], strict_slashes=False)
@swag_from(get_users)
def view_users():
    """
    Get all users
    """
    all_users = [user.to_json() for user in dbStorage.all(User).values()]
    return jsonify(all_users), 200


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
@swag_from(get_user)
def view_user(user_id):
    """
    Get  user
    """
    if user_id is None:
        return jsonify({"msg": "User not found"}), 404

    user = dbStorage.get(User, user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    return jsonify(user.to_json()), 200


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
@swag_from(update_user)
def updateuser(user_id):
    """
    Update user
    """
    if user_id is None:
        return jsonify({"msg": "User not found"}), 404

    user = dbStorage.get(User, user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404
    
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400
    
    ignore = ['created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()

    return jsonify(user.to_json()), 200


@app_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
@swag_from(delete_user)
def deleteuser(user_id):
    """
    Delete all user
    """
    if user_id is None:
        return jsonify({"msg": "User not found"}), 404

    user = dbStorage.get(User, user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    dbStorage.delete(user)
    dbStorage.save()

    return jsonify({"msg": "User delete successfully"}), 200
