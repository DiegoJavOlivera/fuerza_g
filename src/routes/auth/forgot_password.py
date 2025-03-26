from flask import request, url_for, render_template, redirect, flash
from flask.views import MethodView
from models.entities.user import User
from extensions.extensions import model_user, email_service, serializer
from . import auth_bp


class ForgotPassword(MethodView):

    def get(self):
        return render_template("auth/forgot_password.html")

    def post(self):
        email = request.form["email_address"].strip()
        if User.check_google_mail(email):
            if model_user.email_exist(email):
                token = serializer.generate(email)
                confirm_url = url_for("auth.update_forgot_password", token = token, _external = True)
                email_service.sends_emails(render_template('auth/link_password.html', confirm_url= confirm_url),email , "Fuerza G - Recupera el acceso a tu cuenta: Cambia tu contraseña")
                flash("¡Listo! Te enviamos un correo con los pasos para cambiar tu contraseña. Revisa tu bandeja de entrada y sigue las instrucciones.")
                return redirect(url_for("auth.login"))
            flash("No encontramos una cuenta asociada con ese correo electrónico.")
            return redirect(url_for("auth.sign_up"))
        flash("Recuerda que el email debe ser Gmail, intentalo nuevamente")
        return redirect(url_for("auth.sign_up"))
    
forgot_password_view = ForgotPassword.as_view("forgot_password")
auth_bp.add_url_rule("/login/forgot_password", view_func=forgot_password_view, methods=["GET", "POST"])
        
