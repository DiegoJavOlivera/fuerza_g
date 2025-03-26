from flask.views import MethodView
from flask_login import login_required
from flask import render_template
from extensions.extensions import exam_model_manager
from . import view_models_exams_bp

class ViewExam(MethodView):

    def get(self, exam_id):        
        found_exam = exam_model_manager.get_one_exam(exam_id)
        if found_exam:
            return render_template("/subjects/view_subject_exam.html", element_exam = found_exam)
        return "estas buscando cualquier cosa papu", 404
        

view_exam_view = login_required(ViewExam.as_view("view_exam"))
view_models_exams_bp.add_url_rule("/view_exam/<int:exam_id>", view_func=view_exam_view, methods=["GET"])


#@app.route("/upload_models_exam/view_exam/<int:exam_id>")
#@login_required
#def view_exam(exam_id):