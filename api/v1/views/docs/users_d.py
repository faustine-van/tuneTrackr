#!/usr/bin/python3
"""Swagger Documentation Specification"""
get_users = {
    "tags": ["users"],
    "operationId": "getStatus",
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
get_user = {
    "tags": ["users"],
    "operationId": "getStats",
    "parameters": [
      {
        "name": "user_id",
        "in": "path",
        "required": True,
        "description": "ID of the user to update",
        "schema": {"type": "string"},
      }
  ],
    "responses": {
        "200": {
            "description": "Request executed successfully.",
        },
    },
}
update_user = {
  "tags": ["users"],
  "operationId": "updateUser",
  "parameters": [
      {
        "name": "user_id",
        "in": "path",
        "required": True,
        "description": "ID of the user to update",
        "schema": {"type": "string"},
      },
      {
        "name": "user",
        "in": "body",
        "required": True,
        "description": "login",
        "schema": {
            "type": "object",
            "required": ["email", 'password'],
            "properties": {
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                },
                "password": {
                    "type": "string"
                }
                },
                "example": {
                "first_name": "Ex",
                "last_name": "amples",
                "email": "examples@gmail.com",
                "password": "examples1234"
                }
        }
    }
  ],
  "responses": {
    "404": {
      "description": "User not found!"
    },
    "201": {
      "description": "Request executed successfully."
    }
  }
}
delete_user = {
  "tags": ["users"],
  "operationId": "deleteUser",
  "parameters": [
      {
        "name": "user_id",
        "in": "path",
        "required": True,
        "description": "ID of the user to update",
        "schema": {"type": "string"},
      }
  ],
  "responses": {
    "404": {
      "description": "User not found!"
    },
    "201": {
      "description": "Request executed successfully."
    }
  }
}
