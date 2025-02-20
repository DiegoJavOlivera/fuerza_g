from flask import request, flash, redirect, url_for
from flask_login import current_user




def store_next_url():
    if (not current_user.is_authenticated 
        and request.endpoint  # Asegúrate de que request.endpoint no sea None
        and request.endpoint not in ("auth.login", "auth.sign_up", "auth.forgot_password", "auth.index", "auth.update_forgot_password","auth.confirm_mail")
        and not request.endpoint.startswith('static')):
        
        next_url = request.url
        flash("Debe iniciar sesión primero")
        return redirect(url_for('auth.login', next=next_url))