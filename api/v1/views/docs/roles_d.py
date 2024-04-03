#!/usr/bin/python3
"""Swagger Documentation Specification"""
get_roles = {
    "tags": ["roles"],
    "operationId": "getRoles",
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
get_role = {
    "tags": ["roles"],
    "operationId": "getRole",
    "parameters": [
        {
            "name": "role_id",
            "in": "path",
            "required": True,
            "description": "ID of the role to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
update_role = {
    "tags": ["roles"],
    "operationId": "updaterole",
    "parameters": [
        {
            "name": "role",
            "in": "body",
            "required": True,
            "description": "role",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "example": {
                    "name": "Producer"
                },
            },
        },
    ],
    "responses": {
        "404": {"description": "role not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
delete_role = {
    "tags": ["roles"],
    "operationId": "deleterole",
    "parameters": [
        {
            "name": "role_id",
            "in": "path",
            "required": True,
            "description": "ID of the role to update",
            "schema": {"type": "string"},
        }
    ],
    "responses": {
        "404": {"description": "role not found!"},
        "201": {"description": "Request executed successfully."},
    },
}
post_role = {
    "tags": ["roles"],
    "operationId": "postRole",
    "parameters": [
        {
            "name": "role",
            "in": "body",
            "required": True,
            "description": "role",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "example": {
                    "name": "Producer"
                },
            },

        },
    ],
    "responses": {
        "404": {"description": "role not found!"},
        "201": {"description": "Request executed successfully."},
    },
}