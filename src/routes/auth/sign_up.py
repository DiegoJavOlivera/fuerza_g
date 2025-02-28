from flask import request, render_template, redirect, flash, url_for
from models.entities.user import User
from flask.views import MethodView
from extensions.extensions import model_user, email_service, serializer
from . import auth_bp
import os

class SignUp(MethodView):

    def get(self):
        return render_template("auth/sign_up.html")    
    

    def post(self):
        email = request.form["email_address"].strip()
        password = request.form["password"].strip()
        repeat_password = request.form["repeat_password"].strip()
        first_name = request.form["first_name"].capitalize().strip()
        last_name = request.form["last_name"].capitalize().strip()
        gender = request.form["gender"].strip()
        receive_notification = request.form.get("subscribe_to_news") == "True"

        if User.check_password_repeat(password, repeat_password) and User.check_google_mail(email):

            if not model_user.email_exist(email) and not model_user.email_exist_current_user(email):
                model_user.save_temp_user(User(None, email, password, first_name, last_name, gender, receive_notification))
                token = serializer.generate(email)
                confirm_url = url_for("auth.confirm_mail", token = token ,_external = True)
                email_service.sends_emails(render_template("auth/confirm_email.html", confirm_url=confirm_url), email, "Fuerza G - Confirma tu direccion de correo electronico.") 
                flash("El mail de confirmacion se a enviado a su correo electronico, verificalo tienes hasta 1 HORA PARA PODER HACERLO.")
                return redirect(url_for("auth.login"))
                
            
            flash("El correo electrónico que intentas registrar ya se encuentra registrado, verifique su casilla de correo para activar su cuenta o si olvido su contraseña puede recuperarla desde el login.")
            return redirect(url_for("auth.login"))
    
        flash("Las contraseñas ingresadas no coinciden o el tipo de email es incorrecto, debe ser GMAIL. Por favor, asegúrate de que ambas contraseñas sean iguales y el email GMAIL.")
        return redirect(url_for("auth.sign_up"))
    
sign_up_view = SignUp.as_view("sign_up")
auth_bp.add_url_rule("/sign_up",view_func=sign_up_view, methods=["GET", "POST"])
       
    