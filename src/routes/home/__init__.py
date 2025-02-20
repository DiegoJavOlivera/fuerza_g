from flask import Blueprint

home_bp = Blueprint("home", __name__, static_folder="static", template_folder="tenplate", url_prefix="/home")

from .home import *