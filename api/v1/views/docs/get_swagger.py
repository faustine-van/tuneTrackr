#!/usr/bin/env python3
"""API Documentation for GET requests"""

get_top_popular = {
    "tags": ["music-analytics"],
    "operationId": "getPopular",
    "parameters": [
        {
            "name": "item_type",
            "in": "path",
            "required": True,
            "description": "Type of item to retrieve. Valid values include 'artists', 'albums', or 'tracks'.",
            "schema": {"type": "string", "enum": ["artists", "albums", "tracks"]},
        }
    ],
    "responses": {
        "404": {"description": "Item not found."},
        "201": {"description": "Request executed successfully."},
    },
}

get_similar_artists = {
    "tags": ["music-analytics"],
    "operationId": "getSimilarArtists",
    "parameters": [
        {
            "name": "id",
            "in": "query",
            "required": True,
            "description": "ID of the artist to retrieve similar artists.",
            "schema": {"type": "string"},
        },
        {
            "name": "item_count",
            "in": "query",
            "required": False,
            "default": 0,
            "description": "Number of similar artists to retrieve.",
            "schema": {"type": "integer"},
        },
    ],
    "responses": {
        "404": {"description": "Artist not found."},
        "201": {"description": "Request executed successfully."},
    },
}

get_similar_tracks = {
    "tags": ["music-analytics"],
    "operationId": "getSimilarTracks",
    "parameters": [
        {
            "name": "id",
            "in": "query",
            "required": True,
            "description": "ID of the track to retrieve similar tracks.",
            "schema": {"type": "string"},
        },
        {
            "name": "item_count",
            "in": "query",
            "required": False,
            "default": 0,
            "description": "Number of similar tracks to retrieve.",
            "schema": {"type": "integer"},
        },
    ],
    "responses": {
        "404": {"description": "Track not found."},
        "201": {"description": "Request executed successfully."},
    },
}

get_cluster = {
    "tags": ["music-analytics"],
    "operationId": "getCluster",
    "parameters": [
        {
            "name": "num_clusters",
            "in": "query",
            "required": False,
            "description": "Number of clusters to group the artists into.",
            "default": 3,
            "minimum": 2,
            "schema": {"type": "integer"},
        }
    ],
    "responses": {
        "200": {"description": "Request executed successfully."},
    },
}

get_top_artists_swagger  = {
    "tags": ["music-analytics"],
    "operationId": "getTopArtists",
    "parameters": [
        {
            "name": "item_type",
            "in": "query",
            "required": True,
            "description": "Type of item to retrieve. Valid values include 'followers', 'monthly_listeners'.",
            "schema": {"type": "string", "enum": ['followers', 'monthly_listeners']}
        },
        {
            "name": "item_count",
            "in": "query",
            "required": False,
            "description": "Number of top artists to be retrieved.",
            "default": 5,
            "minimum": 2,
            "schema": {"type": "integer"},
        }
    ],
    "responses": {
        "200": {"description": "Request executed successfully."},
    },
}

get_new_albums_swagger = {
    "tags": ["music-analytics"],
    "operationId": "getNewAlbums",
    "parameters": [
        {
            "name": "item_count",
            "in": "query",
            "required": False,
            "description": "Number of new albums realeased soon to be retrieved.",
            "default": 5,
            "minimum": 2,
            "schema": {"type": "integer"},
        }
    ],
    "responses": {
        "200": {"description": "Request executed successfully."},
    },
}
