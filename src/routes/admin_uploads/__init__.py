from flask import Blueprint

uploads_admin_bp = Blueprint("uploads_admin", __name__, static_folder="static", template_folder="templates" ,url_prefix="/upload_admin")

from .uploads_admin import *