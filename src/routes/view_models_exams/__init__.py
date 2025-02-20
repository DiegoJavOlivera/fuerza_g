from flask import Blueprint

view_models_exams_bp = Blueprint("uploads_models_exams", __name__, url_prefix="/uploads_models_exams", static_folder="static", template_folder="templates")

from .view_exam import *
from .view_models_exams import *