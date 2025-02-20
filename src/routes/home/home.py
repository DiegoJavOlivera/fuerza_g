from flask_login import login_required
from flask import render_template
from flask.views import MethodView
from . import home_bp

class Home(MethodView):

    def get(self):
        return render_template("home.html")

home_view = login_required(Home.as_view("home"))
home_bp.add_url_rule("/",view_func=home_view, methods=["GET"])