#!/usr/bin/python3
"""Swagger Documentation Specification"""
get_albums = {
    "tags": ["albums"],
    "operationId": "getStatus",
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
get_album = {
    "tags": ["albums"],
    "operationId": "getAlbum",
    "parameters": [
        {
            "name": "album_id",
            "in": "path",
            "required": True,
            "description": "ID of the album to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
update_album = {
    "tags": ["albums"],
    "operationId": "updateAlbum",
    "parameters": [
        {
            "name": "album_id",
            "in": "path",
            "required": True,
            "description": "ID of the album to update",
            "schema": {"type": "string"},
        },
        {
            "name": "album",
            "in": "body",
            "required": True,
            "description": "updated",
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "title": {"type": "string"},
                    "artist_id": {"type": "string"},
                    "label": {"type": "string"},
                    "release_date": {"type": "timestamp"},
                    "popularity": {"type": "integer"},
                    "total_tracks": {"type": "integer"},
                },
                "example": {
                    "name": "Pop",
                    "album_position": 1,
                    "popularity": 90,
                },
            },
        },
    ],
    "responses": {
        "404": {"description": "album not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
delete_album = {
    "tags": ["albums"],
    "operationId": "deleteAlbum",
    "parameters": [
        {
            "name": "album_id",
            "in": "path",
            "required": True,
            "description": "ID of the album to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "404": {"description": "album not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
post_album_swagger = {
    "tags": ["albums"],
    "operationId": "createalbum",
    "parameters": [
        {
            "name": "album",
            "in": "body",
            "required": True,
            "description": "album to be created",
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "title": {"type": "string"},
                    "artist_id": {"type": "string"},
                    "label": {"type": "string"},
                    "release_date": {"type": "timestamp"},
                    "popularity": {"type": "integer"},
                    "total_tracks": {"type": "integer"},
                },
                "example": {
                    "name": "Pop",
                    "popularity": 90,
                },
            },
        }
    ],
    "responses": {
        "404": {"description": "Album not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
