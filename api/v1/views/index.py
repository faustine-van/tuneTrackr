#!/usr/bin/env python3
"""index module"""
from flask import jsonify
from flasgger import swag_from
from api.v1.views import app_views
from api.v1.views.docs.indexs import stats, status
from models import dbStorage
from models.user import User, Role


@app_views.route("/status", methods=["GET"], strict_slashes=False)
@swag_from(status)
def index():
    """Get status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
@swag_from(stats)
def stats():
    """Get statistics for the entities."""

    entity_classes = [User, Role]
    entity_names = ["users", "roles"]

    counts = {}
    # Count the number of objects for each entity
    for i in range(len(entity_classes)):
        counts[entity_names[i]] = dbStorage.count(entity_classes[i])

    return jsonify(counts)
