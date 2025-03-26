
from flask import Flask ,redirect, url_for
from config import config

from dotenv import load_dotenv
from extensions.extensions import my_sql_db, csrf, login_manager_app, mail, db_manager
from routes import create_blueprints
from middleware.store_next_url import store_next_url

load_dotenv()

app = Flask(__name__)

app.config.from_object(config["development"])

my_sql_db.init_app(app)
csrf.init_app(app)
login_manager_app.init_app(app)
mail.init_app(app)

with app.app_context():
    db_manager.initialize_database()


app.before_request(store_next_url)
create_blueprints(app)


def status_401(error):
    return redirect(url_for("login"))

def status_404(error):
    return "<h1>Pagina no encontrada</h1>", 404

app.register_error_handler(401,status_401)
app.register_error_handler(404,status_404)

