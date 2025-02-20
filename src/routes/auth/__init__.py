from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth", static_folder="static", template_folder="templates")


from .confirm_mail import *
from .forgot_password import *
from .sign_up import *
from .login import *
from .change_password import *