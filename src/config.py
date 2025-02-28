import os 

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "diegolivera")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD","123456")
    MYSQL_DB = os.getenv("MYSQL_DB", "flask")
    SCHEMA_FILE = os.getenv("SCHEMA_FILE", "src/helpers/schema.sql")
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

