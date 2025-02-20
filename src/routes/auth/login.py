from flask import request, flash, render_template, redirect, url_for
from flask.views import MethodView
from flask_login import  login_user
from . import auth_bp
from models.entities.user import User
from extensions.extensions import model_user


class Login(MethodView):

    
    def get(self):
        return render_template("auth/login.html")
    
    def post(self):
        user = User(None,request.form["emailAddress"],request.form["password"])
        logged_user = model_user.login(user)
    
        if logged_user and user.check_password_repeat(user.password,logged_user[2]) :
            login_user(logged_user)
            next_url = request.args.get('next')
            return redirect(next_url or url_for('home'))
        flash("Email o Contraseña no encontrados")
        return render_template("auth/login.html")

login_view = Login.as_view("login")
auth_bp.add_url_rule("/login", view_func=login_view, methods=["GET","POST"])
