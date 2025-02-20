from . import about_us_bp
from flask import render_template

from flask.views import MethodView
from flask_login import login_required

class AboutUs(MethodView):


    def get(self):
        return render_template("about_us.html")



about_us_view = login_required(AboutUs.as_view("about_us"))
about_us_bp.add_url_rule("/", view_func=about_us_view, methods=["GET"])