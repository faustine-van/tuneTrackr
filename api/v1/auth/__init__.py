from flask import Blueprint

auth_s = Blueprint("auth_s", __name__, url_prefix="/api/v1/auth")

from api.v1.auth.auth import *
