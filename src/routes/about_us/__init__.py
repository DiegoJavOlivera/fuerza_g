from flask import Blueprint

about_us_bp = Blueprint("about_us", __name__,url_prefix="/about_us" , static_folder="static", template_folder="templates")

from .about_us import *