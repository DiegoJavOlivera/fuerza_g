from flask.views import MethodView
from flask import render_template
from flask_login import login_required
from extensions.extensions import exam_model_manager
from . import view_models_exams_bp

class ViewModelsExams(MethodView):

    def get(self, subject):
        list_exams = exam_model_manager.get_all_exams(subject)
        print(subject)
        return render_template("/subjects/subject.html", list_exams = list_exams)

view_models_exams_view = login_required(ViewModelsExams.as_view("view_models_exams"))
view_models_exams_bp.add_url_rule("/<string:subject>", view_func=view_models_exams_view, methods=["GET"])