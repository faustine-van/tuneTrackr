"""get"""
get_top_popular = {
    "tags": ["artists, albums, tracks"],
    "operationId": "getPopular",
    "parameters": [
        {
            "name": "item_type",
            "in": "path",
            "required": True,
            "description": "get item_type(artist, albums or tracks",
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
