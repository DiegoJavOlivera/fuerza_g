from flask import Blueprint

log_out_bp = Blueprint("logout", __name__, static_folder="static", template_folder="template", url_prefix="/log_out")

from .log_out import *