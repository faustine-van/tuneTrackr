from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.genres import *
from api.v1.views.artists import *
from api.v1.views.albums import *
from api.v1.views.tracks import *
from api.v1.views.top import *
