from flask.views import MethodView
from flask_login import logout_user
from flask import redirect, flash, url_for
from . import log_out_bp

class LogOut(MethodView):

    def post(self):
        logout_user()
        flash("Sesión cerrada correctamente.")
        return redirect(url_for("auth.login"))

log_out_view = LogOut.as_view("log_out")
log_out_bp.add_url_rule("/", view_func=log_out_view, methods=["POST"])

