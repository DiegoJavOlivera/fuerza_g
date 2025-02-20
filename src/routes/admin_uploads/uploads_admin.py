from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required
from flask.views import MethodView
from models.entities.exams import Exams
from datetime import datetime
from extensions.extensions import email_service, model_user_admin, image_handler
from models.entities.news import News

from . import uploads_admin_bp

class UploadNews(MethodView):

    def get(self, admin_select):
        return render_template("admin.html", subject=admin_select)

    def post(self, admin_select):
        if admin_select == "Subir_noticias":
            return self.handle_news_upload()
        elif admin_select == "Subir_examen":
            return self.handle_exam_upload()
        else:
            flash("Opción no válida.")
            return redirect(url_for("admin_uploads.upload_news", admin_select="Subir_noticias"))

    def handle_news_upload(self):
        try:
            title = request.form["title"].strip()
            news_content = request.form["content"].strip()
            image = request.files.get("image")
            date = datetime.now()
            mail_title_news = request.form["subject_news_title"].strip()
            content_email_news = request.form["content_email"]

            if not (title and news_content and image):
                flash("Todos los campos son obligatorios.")
                return redirect(url_for("admin_uploads.upload_news", admin_select="Subir_noticias"))

            image_relative_path = image_handler.save_news_image(image)
            email_service.sends_emails(content_email_news, email_service.get_all_users_receive_not(), mail_title_news, mass_send=True)

            if model_user_admin.save_news(News(None, title, news_content, date, image_relative_path)):
                flash("La noticia se guardó, publicó con éxito y se envió la notificación por email.")
                return redirect(url_for("admin_uploads.upload_news", admin_select="Subir_noticias"))

            flash("No se pudo guardar y publicar la noticia.")
        except Exception as e:
            flash(f"Error al procesar la noticia: {e}")
        return redirect(url_for("admin_uploads.upload_news", admin_select="Subir_noticias"))

    def handle_exam_upload(self):
        try:
            title_exam = request.form["title_exam"].strip()
            image_exam = request.files.get("image_exam")
            date_exam = datetime.now()
            content_exam = request.form["content_exam"]
            subject_exam = request.form["sub_exam"]
            subject_mail_exam = request.form["subject_mail_exam"]
            content_email_exam = request.form["content_email"]

            if not (title_exam and content_exam and image_exam):
                flash("Todos los campos son obligatorios.")
                return redirect(url_for("admin_uploads.upload_news", admin_select="Subir_examen"))

            image_relative_path_exam = image_handler.save_exam_image(image_exam)
            email_service.sends_emails(content_email_exam, email_service.get_all_users_receive_not(), subject_mail_exam, mass_send=True)

            if model_user_admin.save_subject_exam(Exams(None, title_exam, image_relative_path_exam, date_exam, content_exam, subject_exam)):
                flash("El examen se guardó, publicó con éxito y se envió la notificación por email.")
                return redirect(url_for("admin_uploads.upload_news", admin_select="Subir_examen"))

            flash("No se pudo guardar y publicar el examen.")
        except Exception as e:
            flash(f"Error al procesar el examen: {e}")
        return redirect(url_for("admin_uploads.upload_news", admin_select="Subir_examen"))


upload_news_view = login_required(UploadNews.as_view("upload_news"))
uploads_admin_bp.add_url_rule("/<admin_select>", view_func=upload_news_view, methods=["GET", "POST"])
