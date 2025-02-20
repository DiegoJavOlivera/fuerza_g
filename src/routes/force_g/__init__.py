from flask import Blueprint

force_g_bp = Blueprint("force_g", __name__, static_folder="static", template_folder="templates", url_prefix="/force_g")

from .force_g import *