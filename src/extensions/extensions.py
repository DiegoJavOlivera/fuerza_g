from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_mail import Mail
from models.dataBaseManager import DataBaseManager
from models.modelUser import ModelUser
from models.modelUserAdmin import ModelUserAdmin
from models.emailService import EmailService
from models.newsManager import NewsManager
from models.imagehandler import ImageHandler
from models.examModelManager import ExamModelManager
from models.token_serializer import TokenSerializer
from models.entities.user import User
from dotenv import load_dotenv

import os

load_dotenv()


my_sql_db = MySQL()
csrf = CSRFProtect()
db_manager = DataBaseManager(my_sql_db, os.getenv("SCHEMA_FILE"))
login_manager_app = LoginManager()
mail = Mail()
model_user = ModelUser(db_manager)
model_user_admin = ModelUserAdmin(db_manager)
email_service = EmailService(db_manager, mail)
news_manager = NewsManager(db_manager)
image_handler = ImageHandler()
exam_model_manager = ExamModelManager(db_manager)
serializer = TokenSerializer(os.getenv("SECRET_KEY"), os.getenv("SALT"))


@login_manager_app.user_loader
def load_user(id)-> User | None:
    """
    Loads a user by their ID.

    This function is used by Flask-Login to retrieve a user object during 
    authentication. It calls the 'get_by_id' method from the user model to 
    fetch the user data.

    Args:
    -------
        id (str): The user's ID provided by Flask-Login.

    Returns:
    --------
        User | None: The authenticated user object if found, otherwise None.
    """
    return model_user.get_by_id(id)


