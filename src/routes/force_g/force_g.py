from flask_login import login_required
from flask import render_template
from flask.views import MethodView
from . import force_g_bp

class ForceG(MethodView):

    def get(self):
        return render_template("force_g.html")
    
force_g_view = login_required(ForceG.as_view("force_g"))
force_g_bp.add_url_rule("/", view_func=force_g_view, methods=["GET"])