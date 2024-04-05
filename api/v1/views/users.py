#!/usr/bin/python3
""" objects that handle all authentication of RestFul API"""
from flasgger import swag_from
from flask import jsonify, request
from models.user import User
from models import dbStorage
from api.v1.views import app_views
from api.v1.views.docs.users_d import (
    get_users,
    get_user,
    update_user,
    delete_user,

)
from flask_jwt_extended import jwt_required
from api.v1.auth.decorators import auth_role


@app_views.route("/users", methods=["GET"], strict_slashes=False)
# @jwt_required()
# @auth_role("admin")
@swag_from(get_users)
def view_users():
    """
    Get all Users
    """
    items = [user.to_json() for user in dbStorage.all(User).values()]
    return jsonify({"url": request.url,
                    "count": len(items),
                    "items": items
                    }
                ), 200


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
@jwt_required()
@swag_from(get_user)
def view_user(user_id):
    """
    Get  user
    """
    if user_id is None:
        return jsonify({"msg": "user not found"}), 404

    user = dbStorage.get(User, user_id)
    if not user:
        return jsonify({"msg": "user not found"}), 404

    return jsonify({"url": request.url,
                    "count": 1,
                    "item": user.to_json()
                   }), 200


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
@jwt_required()
@swag_from(update_user)
def updateuser(user_id):
    """
    Update user
    """
    if user_id is None:
        return jsonify({"msg": "user not found"}), 404

    user = dbStorage.get(User, user_id)
    if not user:
        return jsonify({"msg": "user not found"}), 404

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    ignore = ["created_at", "updated_at"]

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()

    return jsonify({"msg": "user updated successfully"}), 200


@app_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
@jwt_required()
@swag_from(delete_user)
def deleteuser(user_id):
    """
    Delete all user
    """
    if user_id is None:
        return jsonify({"msg": "user not found"}), 404

    user = dbStorage.get(User, user_id)
    if not user:
        return jsonify({"msg": "user not found"}), 404

    dbStorage.remove(user)
    dbStorage.save()

    return jsonify({"msg": "user delete successfully"}), 200


@app_views.route("/users", methods=["POST"], strict_slashes=False)
# @swag_from(post_user)
def post_user():
    """
    Create a user
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    try:
        new_instance = User(**data)
        new_instance.save()
        # Generate token
        token = new_instance.get_reset_token()
        return jsonify({"msg": "user created successfully", "token": token}), 201
    except Exception as e:
        # Log the exception for debugging
        print(f"Error creating user: {e}")
        return jsonify({"msg": "Can't create user"}), 500
