from flask.views import MethodView
from flask import render_template
from flask_login import login_required
from extensions.extensions import news_manager
from . import view_news_bp



class ViewNews(MethodView):

    def get(self):
        news_list = news_manager.get_all_news()
        return render_template("news.html", news_list = news_list)


view_news_view = login_required(ViewNews.as_view("view_news"))
view_news_bp.add_url_rule("/", view_func=view_news_view, methods=["GET"])
