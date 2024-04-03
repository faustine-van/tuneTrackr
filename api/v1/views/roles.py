#!/usr/bin/python3
""" objects that handle all authentication of RestFul API"""
from flasgger import swag_from
from flask import jsonify, request
from models.user import Role
from models import dbStorage
from api.v1.views import app_views
from api.v1.views.docs.roles_d import (
    get_roles,
    get_role,
    update_role,
    delete_role,
    post_role,

)
from flask_jwt_extended import jwt_required
from api.v1.auth.decorators import auth_role


@app_views.route("/roles", methods=["GET"], strict_slashes=False)
@swag_from(get_roles)
def view_roles():
    """
    Get all roles
    """
    items = [role.to_json() for role in dbStorage.all(Role).values()]
    return jsonify({"url": request.url,
                    "count": len(items),
                    "items": items
                    }
                ), 200


@app_views.route("/roles/<role_id>", methods=["GET"], strict_slashes=False)
@swag_from(get_role)
def view_role(role_id):
    """
    Get  role
    """
    if role_id is None:
        return jsonify({"msg": "role not found"}), 404

    role = dbStorage.get(Role, role_id)
    if not role:
        return jsonify({"msg": "role not found"}), 404

    return jsonify({"url": request.url,
                    "count": 1,
                    "item": role.to_json()
                   }), 200


@app_views.route("/roles/<role_id>", methods=["PUT"], strict_slashes=False)
@swag_from(update_role)
def updaterole(role_id):
    """
    Update role
    """
    if role_id is None:
        return jsonify({"msg": "role not found"}), 404

    role = dbStorage.get(Role, role_id)
    if not role:
        return jsonify({"msg": "role not found"}), 404

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    ignore = ["created_at", "updated_at"]

    for key, value in data.items():
        if key not in ignore:
            setattr(role, key, value)
    role.save()

    return jsonify({"msg": "role updated successfully"}), 200


@app_views.route("/roles/<role_id>", methods=["DELETE"], strict_slashes=False)
@swag_from(delete_role)
def deleterole(role_id):
    """
    Delete all role
    """
    if role_id is None:
        return jsonify({"msg": "role not found"}), 404

    role = dbStorage.get(Role, role_id)
    if not role:
        return jsonify({"msg": "role not found"}), 404

    dbStorage.remove(role)
    dbStorage.save()

    return jsonify({"msg": "role delete successfully"}), 200


@app_views.route("/roles", methods=["POST"], strict_slashes=False)
@swag_from(post_role)
def post_role():
    """
    Create a role
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Not a JSON"}), 400

    new_instance = Role(**data)
    new_instance.save()
    return jsonify({"msg": "Role created successfult"}), 201
