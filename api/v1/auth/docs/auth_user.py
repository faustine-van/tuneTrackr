#!/usr/bin/python3
"""Swagger Documentation Specification"""
register_swagger = {
    "tags": ["auth"],
    "operationId": "createUser",
    "parameters": [
        {
            "name": "user",
            "in": "body",
            "required": True,
            "description": "User to be created",
            "schema": {
                "type": "object",
                "required": ["email", "password"],
                "properties": {
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                    "role": {"type": "string"}
                },
                "example": {
                    "first_name": "Ex",
                    "last_name": "amples",
                    "email": "examples@gmail.com",
                    "password": "examples1234",
                    "role": "'standard' | 'admin' | 'analyst'| 'artist' | 'manager'"
                },
            },
        }
    ],
    "responses": {
        "404": {"description": "User not found!"},
        "201": {"description": "Request executed successfully."},
    },
}

login_swagger = {
    "tags": ["auth"],
    "operationId": "login",
    "parameters": [
        {
            "name": "user",
            "in": "body",
            "required": True,
            "description": "login",
            "schema": {
                "type": "object",
                "required": ["email", "password"],
                "properties": {
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                },
                "example": {"email": "examples@gmail.com", "password": "examples1234"},
            },
        }
    ],
    "responses": {
        "404": {"description": "User not found!"},
        "201": {"description": "Request executed successfully."},
    },
}

logout_swagger = {
    "tags": ["auth"],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}

profile_swagger = {
    "tags": ["auth"],
    "operationId": "profile",
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
    "security": [{"Bearer": []}],
}

refresh_swagger = {
    "tags": ["auth"],
    "operationId": "refresh_token",
    "responses": {
        "404": {"description": "User not found!"},
        "201": {"description": "Request executed successfully."},
    },
    "security": [{"Bearer": []}],
}

revoke_access_swagger = {
    "tags": ["auth"],
    "operationId": "revoke_access_token",
    "responses": {
        "404": {"description": "User not found!"},
        "201": {"description": "Request executed successfully."},
    },
    "security": [{"Bearer": []}],
}

revoke_refresh_swagger = {
    "tags": ["auth"],
    "operationId": "revoke_refresh_token",
    "responses": {
        "404": {"description": "User not found!"},
        "201": {"description": "Request executed successfully."},
    },
    "security": [{"Bearer": []}],
}

forget_password_swagger = {
    "tags": ["auth"],
    "operationId": "forget_password",
    "parameters": [
        {
            "name": "user",
            "in": "body",
            "required": True,
            "description": "User to be created",
            "schema": {
                "type": "object",
                "required": ["email"],
                "properties": {"email": {"type": "string"}},
                "example": {"email": "examples@gmail.com"},
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}

reset_password_swagger = {
    "tags": ["auth"],
    "operationId": "reset_pssword",
    "parameters": [
        {
            "name": "reset_token",
            "in": "query",
            "required": True,
            "description": "reset password",
            "schema": {
                "type": "string",
            },
        },
        {
            "name": "user",
            "in": "body",
            "required": True,
            "description": "reset password",
            "schema": {
                "type": "object",
                "required": ["password"],
                "properties": {"password": {"type": "string"}},
                "example": {"password": "examples@gmail.com"},
            },
        },
    ],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
