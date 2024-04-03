#!/usr/bin/python3
"""Swagger Documentation Specification"""
get_genres = {
    "tags": ["genres"],
    "operationId": "getGenres",
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
get_genre = {
    "tags": ["genres"],
    "operationId": "getGenre",
    "parameters": [
        {
            "name": "genre_id",
            "in": "path",
            "required": True,
            "description": "ID of the genre to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
    "security": [{"Bearer": []}]
}
update_genre = {
    "tags": ["genres"],
    "operationId": "updategenre",
    "parameters": [
        {
            "name": "genre_id",
            "in": "path",
            "required": True,
            "description": "ID of the genre to update",
            "schema": {"type": "string"},
        },
        {
            "name": "genre",
            "in": "body",
            "required": True,
            "description": "login",
            "schema": {
                "type": "object",
                "required": [],
                "properties": {"name": {"type": "string"}},
                "example": {"name": "Pop"},
            },
        },
    ],
    "responses": {
        "404": {"description": "genre not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
delete_genre = {
    "tags": ["genres"],
    "operationId": "deletegenre",
    "parameters": [
        {
            "name": "genre_id",
            "in": "path",
            "required": True,
            "description": "ID of the genre to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "404": {"description": "genre not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
post_genre_swagger = {
    "tags": ["genres"],
    "operationId": "createGenre",
    "parameters": [
        {
            "name": "genre",
            "in": "body",
            "required": True,
            "description": "Genre to be created",
            "schema": {
                "type": "object",
                "required": [],
                "properties": {"name": {"type": "string"}},
                "example": {"name": "Rock"},
            },
        }
    ],
    "responses": {
        "404": {"description": "Genre not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
