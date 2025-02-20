import os 

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")
    # aca comienza la configuracion para el envio de mails

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    
    #configuracion de ruta para imagenes de noticias
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

    #configuracion de ruta de examnes
    UPLOAD_FOLDER_EXAM  = os.getenv("UPLOAD_EXAM")
    WTF_CSRF_ENABLED = True

config = {
    "development": DevelopmentConfig
}

