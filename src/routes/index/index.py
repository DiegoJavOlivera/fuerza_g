from . import index_bp
from flask.views import MethodView
from flask import render_template

class Index(MethodView):

    def get(self):
        return render_template("auth/login.html")

index_view = Index.as_view("index")
index_bp.add_url_rule("/", view_func=index_view, methods=["GET"])
