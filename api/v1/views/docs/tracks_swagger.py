#!/usr/bin/python3
"""Swagger Documentation Specification"""
get_tracks = {
    "tags": ["tracks"],
    "operationId": "getTracks",
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
get_track = {
    "tags": ["tracks"],
    "operationId": "getTrack",
    "parameters": [
        {
            "name": "track_id",
            "in": "path",
            "required": True,
            "description": "ID of the track to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
update_track = {
    "tags": ["tracks"],
    "operationId": "updatetrack",
    "parameters": [
        {
            "name": "track_id",
            "in": "path",
            "required": True,
            "description": "ID of the track to update",
            "schema": {"type": "string"},
        },
        {
            "name": "track",
            "in": "body",
            "required": True,
            "description": "updated",
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "name": {"type": "string"},
                    "artist_id": {"type": "string"},
                    "album_id": {"type": "string"},
                    "release_date": {"type": "timestamp"},
                    "popularity": {"type": "integer"},
                    "track_rank": {"type": "integer"},
                    "track_position": {"type": "integer"},
                },
                "example": {
                    "name": "Pop",
                    "track_position": 1,
                    "popularity": 90,
                },
            },
        },
    ],
    "responses": {
        "404": {"description": "track not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
delete_track = {
    "tags": ["tracks"],
    "operationId": "deletetrack",
    "parameters": [
        {
            "name": "track_id",
            "in": "path",
            "required": True,
            "description": "ID of the track to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "404": {"description": "track not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
post_track_swagger = {
    "tags": ["tracks"],
    "operationId": "createtrack",
    "parameters": [
        {
            "name": "track",
            "in": "body",
            "required": True,
            "description": "track to be created",
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "name": {"type": "string"},
                    "artist_id": {"type": "string"},
                    "album_id": {"type": "string"},
                    "release_date": {"type": "timestamp"},
                    "popularity": {"type": "integer"},
                    "track_rank": {"type": "integer"},
                    "track_position": {"type": "integer"},
                },
                "example": {
                    "name": "Pop",
                    "track_position": 1,
                    "popularity": 90,
                },
            },
        }
    ],
    "responses": {
        "404": {"description": "track not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
