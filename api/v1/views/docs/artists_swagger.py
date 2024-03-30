#!/usr/bin/python3
"""Swagger Documentation Specification"""
get_artists = {
    "tags": ["artists"],
    "operationId": "getStatus",
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
get_artist = {
    "tags": ["artists"],
    "operationId": "getStats",
    "parameters": [
        {
            "name": "artist_id",
            "in": "path",
            "required": True,
            "description": "ID of the artist to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
update_artist = {
    "tags": ["artists"],
    "operationId": "updateartist",
    "parameters": [
        {
            "name": "artist_id",
            "in": "path",
            "required": True,
            "description": "ID of the artist to update",
            "schema": {"type": "string"},
        },
        {
            "name": "artist",
            "in": "body",
            "required": True,
            "description": "updated",
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "name": {"type": "string"},
                    "follower": {"type": "integer"},
                    "popularity": {"type": "integer"},
                    "nb_albums": {"type": "integer"},
                    "monthly_listener": {"type": "integer"},
                    "genre_id": {"type": "string"},
                },
                "example": {
                    "name": "Pop",
                    "follower": 300,
                    "popularity": 90,
                },
            },
        },
    ],
    "responses": {
        "404": {"description": "artist not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
delete_artist = {
    "tags": ["artists"],
    "operationId": "deleteartist",
    "parameters": [
        {
            "name": "artist_id",
            "in": "path",
            "required": True,
            "description": "ID of the artist to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "404": {"description": "artist not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
post_artist_swagger = {
    "tags": ["artists"],
    "operationId": "createartist",
    "parameters": [
        {
            "name": "artist",
            "in": "body",
            "required": True,
            "description": "artist to be created",
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "name": {"type": "string"},
                    "follower": {"type": "integer"},
                    "popularity": {"type": "integer"},
                    "nb_albums": {"type": "integer"},
                    "monthly_listener": {"type": "integer"},
                    "genre_id": {"type": "string"},
                },
                "example": {
                    "name": "Pop",
                    "follower": 300,
                    "popularity": 90,
                },
            },
        }
    ],
    "responses": {
        "404": {"description": "artist not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
