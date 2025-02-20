from flask.views import MethodView
from flask import render_template
from flask_login import login_required
from . import view_news_bp
from extensions.extensions import news_manager

class ViewNew(MethodView):

    def get(self, news_id):
        found_news = news_manager.get_one_news(news_id)
        if found_news:
            return render_template("view_news.html", news=found_news)
        else:
            return "estas buscando cualquier cosa papu", 404

view_new_view = login_required(ViewNew.as_view("view_new"))
view_news_bp.add_url_rule("/<int:news_id>", view_func=view_new_view, methods=["GET"])