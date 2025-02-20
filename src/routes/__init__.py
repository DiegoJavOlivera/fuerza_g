from flask import Flask
from routes.auth import auth_bp
from routes.admin_uploads import uploads_admin_bp
from routes.about_us import about_us_bp
from routes.view_models_exams import view_models_exams_bp
from routes.view_news import view_news_bp
from routes.home import home_bp
from routes.force_g import force_g_bp
from routes.log_out import log_out_bp
from routes.index import index_bp

#En este archivo solo debe ir los blueprints
#rutas blueprint
def create_blueprints(app: Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(uploads_admin_bp)
    app.register_blueprint(about_us_bp)
    app.register_blueprint(view_models_exams_bp)
    app.register_blueprint(view_news_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(force_g_bp)
    app.register_blueprint(log_out_bp)
    app.register_blueprint(index_bp)