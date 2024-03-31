#!/usr/bin/python3
""" app module """
from flask import Flask, jsonify
from flask_cors import CORS
from flask_mail import Mail
from flasgger import Swagger
from config import Config
from api.v1.views import app_views
from api.v1.auth import auth_s
from models import dbStorage
from exts import jwt


app = Flask(__name__)
# register blueprint
app.register_blueprint(app_views)
app.register_blueprint(auth_s)
# access configuration
app.config.from_object(Config)
# cross allow orgin
cors = CORS(app, resources={r"/api/v1*": {"origins": "*"}})
# jwt
jwt.init_app(app)
# main
mail = Mail(app)
# documentations
URL = "https://github.com/faustine-van/tuneTrackr?tab=MIT-1-ov-file"
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "TuneTrackr API",
        "description": "API Documentation for TuneTrackr API",
        "contact": {
            "name": "Admin",
            "email": "faustinemuhayemariya44@gmail.com",
            "url": "https://github.com/faustine-van",
        },
        "termsOfService": "Terms of services",
        "version": "1.0.0",
        "host": "",  # site
        "basePath": "/api",
        "license": {
         "name": "License of API",
         "url": f'{URL}',
        },
    },
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": '\
             Enter the token. Example: "Bearer {token}"',
        },
    },
    "externalDocs": {
        "description": "Learn more about our API",
        "url": "https://github.com/faustine-van/tuneTrackr?tab=readme-ov-file",
    },
}

swagger_config = {
    "headers": [
        ("Access-Control-Allow-Origin", "*"),
        ("Access-Control-Allow-Methods", "GET, POST"),
    ],
    "specs": [
        {
            "endpoint": "TuneTrackr",
            "route": "/http://localhost:5000/tuneTrackr.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "title": "API - TuneTrackr",
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/",
}
Swagger(app, template=swagger_template, config=swagger_config)


@app.teardown_appcontext
def close(error):
    """close session of database"""
    dbStorage.close()


@app.errorhandler(404)
def page_not_found(error):
    """404 Error
    ---
    responses:
     404:
     description: a resource was not found
    """
    return jsonify({"error": "Page not found"}), 404


if __name__ == "__main__":
    # run app
    host = app.config.get("API_HOST")
    port = app.config.get("API_PORT")
    debug = app.config.get("DEBUG")
    app.run(debug=debug, host=host, port=port)
