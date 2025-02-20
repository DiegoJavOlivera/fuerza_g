from flask import Blueprint

index_bp = Blueprint("index", __name__, static_folder="static", template_folder="template", url_prefix="/")

from .index import *