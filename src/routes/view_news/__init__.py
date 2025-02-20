from flask import Blueprint

view_news_bp = Blueprint("view_news", __name__, static_folder="static", template_folder="templates", url_prefix="/news")


from .view_new import *
from .view_news import *