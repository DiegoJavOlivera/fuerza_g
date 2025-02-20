from . import auth_bp
from extensions.extensions import model_user
from extensions.extensions import serializer
from flask import flash, redirect, url_for, request, render_template
from flask.views import MethodView
from models.entities.user import User


class UpdateForgotPassword(MethodView):

    def get(self, token):
        
        if serializer.deserialize(token):
            return render_template("auth/update_password.html", token=token)
        
        flash(f"Error al deserializar.")
        return redirect(url_for("auth.login"))

    def post(self, token):
        
        password = request.form["password"].strip()
        repeat_password = request.form["repeat_password"].strip()
        
        if User.check_password_repeat(password,repeat_password):
            if model_user.update_password(serializer.deserialize(token), password):            
                flash("La contraseña ha sido restablecida con éxito.")
                return redirect(url_for("auth.login"))
            
            flash("No se ha podido restablecer la contraseña, inténtelo nuevamente.")
            return render_template("auth/update_password.html", token=token)
        
        flash("Las contraseñas no coinciden, por favor intente nuevamente.")
        return render_template("auth/update_password.html", token=token)
    
update_forgot_password_view = UpdateForgotPassword.as_view("update_forgot_password")
auth_bp.add_url_rule("/login/change_password/<token>", view_func=update_forgot_password_view, methods=["GET", "POST"])

        
    
