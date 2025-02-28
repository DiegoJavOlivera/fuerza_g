from flask import flash, redirect, url_for
from flask.views import MethodView
from extensions.extensions import model_user, serializer

from . import auth_bp



class ConfirmMail(MethodView):

    def get(self, token):
        deserialized_email = serializer.deserialize(token)
        if deserialized_email:
            if model_user.move_to_active_user(deserialized_email):
                flash("El usuario se registro con exito")
                return redirect(url_for("auth.login"))

            flash("El correo electrónico que intentas registrar ya se encuentra registrado.")
            return redirect(url_for("auth.login"))
        flash('El enlace de confirmación ha expirado. Por favor, regístrate de nuevo.')
        return redirect(url_for("auth.sign_up"))
      

confirm_mail_view = ConfirmMail.as_view("confirm_mail")
auth_bp.add_url_rule("/confirm/<token>", view_func=confirm_mail_view, methods=["GET"])





